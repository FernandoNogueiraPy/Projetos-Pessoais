from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd 
import random
from anticaptchaofficial.recaptchav2proxyless import *
import time
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread
from replaces import altera_placa
from logs import save_logs

# Set the Chrome options to disable some features that could interfere with the CAPTCHA solving
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

# Function to split the input data into roughly equal parts
def separar_lista(lista: list, quantidade: int):
    new_list = []
    for index in range(0, len(lista), quantidade):
        new_list.append(lista[index:index+quantidade])
    return new_list

# Arquivo a ser lido.
df = pd.read_excel(r"TesteComPadrao2.xlsx")

# Divide o dataframe em um número X.
numero_raw = len(df)  / 1# < Número que deve ser trocado para divisão < 

lista_separada = separar_lista(df,int(numero_raw))
url_do_forms = "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx"

def pega_debitos(lista):

    # Launch Chrome and navigate to the website
    chrome = webdriver.Chrome(ChromeDriverManager().install())    
    chrome.get(url_do_forms)
    dataframe = pd.DataFrame(lista)

    for index,row in dataframe.iterrows():
        print("index: " + str(index) + " o nome é " + row ["CONTRATO"])
        
        # Add a random delay to mimic human behavior
        time.sleep(random.uniform(1, 3))

        renavam = row["RENAVAM"]
        placa = row["PLACA"]

        # Try up to 2 times to get the information for each row
        for i in range(0,2):
           # try:
                # Set the implicit wait time to 10 seconds
                chrome.implicitly_wait(10)

                # Find the input elements for the plate and RENAVAM
                elemento_renavam = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtRenavam"]')
                elemento_placa = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtPlaca"]')

                # Clear the input elements and enter the plate and RENAVAM
                elemento_renavam.clear()
                elemento_placa.clear()
                elemento_renavam.send_keys(renavam)
                elemento_placa.send_keys(placa)

                # Wait 1 second before continuing
                time.sleep(1)

                # Get the CAPTCHA key from the website
                chave_captcha = chrome.find_element(By.ID,'conteudoPaginaPlaceHolder_g_recaptcha').get_attribute('data-sitekey')

                # Initialize the CAPTCHA solver
                solver = recaptchaV2Proxyless()
                solver.set_verbose(1)
                solver.set_key("03d6ce05e61a048fd4de08b3c7d68fdc")
                solver.set_website_url(url_do_forms)
                solver.set_website_key(chave_captcha)

                # Try to solve the CAPTCHA
                resposta = solver.solve_and_return_solution()

                # If the CAPTCHA was solved successfully, enter the solution in the website
                if resposta != 0:
                    print(resposta)
                    chrome.execute_script(f"document.getElementById('g-recaptcha-response').value = '{resposta}'")
                    
                else:
                    print(solver.err_string)

                # Wait 1 second before continuing
                time.sleep(1)
                # Click the "Consultar" button to access the vehicle information
                chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_btn_Consultar"]').click()

                # Wait 4 seconds for the information to load
                time.sleep(4)

                # Scroll down 1000 pixels to view the whole page
                chrome.execute_script("window.scrollBy(0,1000)")

                # Wait 1 second before continuing
                time.sleep(1)

                # Find the element with the vehicle's debts and assign it to the "debitos" variable
                elemento_debitos = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_lbl_Debitos"]').text

                # If the element with the debts is not empty, store it in the "debitos" column of the dataframe
                if elemento_debitos:
                    row["DEBITOS"] = elemento_debitos

                # If the element is empty, store "Não há débitos" in the "debitos" column of the dataframe
                else:
                    row["DEBITOS"] = "Não há débitos"

                # Print the vehicle's debts
                print(row["DEBITOS"])

                # Wait 1 second before continuing
                time.sleep(1)
                # Return to the previous page
                chrome.execute_script("window.history.go(-1)")

                # Wait 1 second before continuing
                time.sleep(1)

                # Close the Chrome window
                chrome.quit()

                # Save the changes to the dataframe
                dataframe.to_excel("TesteComPadraoResposta.xlsx",index=False)


#Inicia uma função de consulta para cada lista do Dataframe que foi separado.
for lista in lista_separada:
    Thread(target=pega_debitos,kwargs={"lista":lista}).start()
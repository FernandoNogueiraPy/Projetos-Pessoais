from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd 
from anticaptchaofficial.recaptchav2proxyless import *
import time
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread
from replaces import altera_placa
from logs import save_logs


options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')


#Função de divisão 
def separar_lista(lista: list, quantidade: int):
    new_list = []
    for index in range(0, len(lista), quantidade):
        new_list.append(lista[index:index+quantidade])
    return new_list

#Arquivo a ser lido.
df = pd.read_excel(r"TratamentoErros.xlsx")

 #Divide o dataframe em um número X.
numero_raw = len(df)  / 4# < Número que deve ser trocado para divisão < 

lista_separada = separar_lista(df,int(numero_raw))
url_do_forms = "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx"



def pega_debitos(lista):

    chrome = webdriver.Chrome(ChromeDriverManager().install())    
    chrome.get(url_do_forms)
    dataframe = pd.DataFrame(lista)

    for index,row in dataframe.iterrows():
        print("index: " + str(index) + " o nome é " + row ["CONTRATO"])
        
        time.sleep(2)

        
        renavam = row["RENAVAM"]
        placa = row["PLACA"]

        for i in range(0,2):
            try:

                #Identifica os elementos onde serão inseridos a placa e o renavam
                elemento_renavam = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtRenavam"]')
                elemento_placa = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtPlaca"]')
                elemento_renavam.clear()
                elemento_placa.clear()
                elemento_renavam.send_keys(renavam)
                elemento_placa.send_keys(placa)

                time.sleep(2)


                #Inicia o QuebraCpatcha.
                chave_captcha = chrome.find_element(By.ID,'conteudoPaginaPlaceHolder_g_recaptcha').get_attribute('data-sitekey')

                solver = recaptchaV2Proxyless()
                solver.set_verbose(1)
                solver.set_key("03d6ce05e61a048fd4de08b3c7d68fdc")
                solver.set_website_url(url_do_forms)
                solver.set_website_key(chave_captcha)

                resposta = solver.solve_and_return_solution()

                if resposta != 0:
                    print(resposta)
                    chrome.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
                    
                else:
                    print(solver.err_string)

                time.sleep(2)


                #Clicka na consulta.
                chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_btn_Consultar"]').click()

                time.sleep(2)


                #Scrol para baixo 1000 Pixel
                chrome.execute_script("window.scrollBy(0,1000)")

                #Captura o elemento e atribui ele a coluna de [DEBITOS]
                elemento_debito = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtExisteDividaAtiva"]' ).text #Pesquisa débitos inscritos em dívida ativa 
                print(elemento_debito)
                df['DEBITOS'][index] = elemento_debito 

                time.sleep(5)

                #Scrol para baixo 500 Pixel
                chrome.execute_script("window.scrollBy(0,500)")

                #Captura o elemento e atribui ele a coluna de [DEBITOS TOTAIS]
                elemento_total_debitos = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_Panel1"]/table[32]/tbody/tr/td[3]').text #Pesquisa de débitos totais. 
                print(elemento_total_debitos)
                df['DEBITOS TOTAIS'][index] = elemento_total_debitos


                #Cria o novo arquivo excel com os valores pesquisados. 
                df.to_excel('Tabela_Fipe_Valores_testando_abas.xlsx', index=False)

                time.sleep(2)

                chrome.back()
            except Exception as error:
                if i != 1:
                    placa = altera_placa(placa) # add trocar letra por numero
                else:
                    df['DEBITOS'][index] = "Não foi possivel localizar"
                    save_logs(f"log - {placa} {error}")
                continue
            else:
                break

    
#Inicia uma função de consulta para cada lista do Dataframe que foi separado.
for lista in lista_separada:
    Thread(target=pega_debitos,kwargs={"lista":lista}).start()



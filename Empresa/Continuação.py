from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd 
from selenium.webdriver.support.select import Select
from anticaptchaofficial.recaptchav2proxyless import *
import time


nome_do_arquivo = 'TabelaFipe.xlsx'
df = pd.read_excel(r"C:\Users\Moltt\Documents\python\Empresa\TabelaFipe.xlsx")
url_do_forms = "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx"
chrome = webdriver.Chrome(executable_path=r'C:\Users\Moltt\Documents\python\Empresa\chromedriver.exe') 
chrome.get(url_do_forms)





for index,row in df.iterrows():

   

    print("index: " + str(index) + " o nome é " + row ["CONTRATO"])
    
    time.sleep(3)

    elemento_renavam = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtRenavam"]')
    elemento_placa = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtPlaca"]')
    
    elemento_renavam.send_keys(row["RENAVAM"])
    elemento_placa.send_keys(row["PLACA"])

    time.sleep(2)

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

    elemento_consulta = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_btn_Consultar"]').click()


    time.sleep(100)
    

#chrome.quit()
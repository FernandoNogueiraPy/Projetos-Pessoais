import pandas as pd 
from selenium import webdriver
from threading import Thread
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from anticaptchaofficial.recaptchav2proxyless import *


df = pd.read_excel('TestePrincipal.xlsx')



class NotDivisibleList(Exception):
    pass


def separarlista(lista:list,n:int):
    listas = []
    if len(lista) % n == 0:
        parou = 0
        corte = int(len(lista) / n)
        for _ in range(n):
            atual_lista = lista[parou:corte]
            listas.append(atual_lista)
            parou = corte
            corte += corte
        return listas
    else:
        raise NotDivisibleList(f"{n} não pode dividir {len(lista)} que e o tamanho da lista")


listas = separarlista(df,2)  #pares 


contador = 0



        
url_do_forms = "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx"
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
chrome = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
chrome.get(url_do_forms)
    
       
    
        



def pega_debitos(index,row):

        print("index: " + str(index) + " o nome é " + row ["CONTRATO"])
        
        time.sleep(2)

        elemento_renavam = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtRenavam"]')
        elemento_placa = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtPlaca"]')
        
        elemento_renavam.clear()
        elemento_placa.clear()

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

        chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_btn_Consultar"]').click()

        time.sleep(2)

        chrome.execute_script("window.scrollBy(0,1000)")

        elemento_debito = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtExisteDividaAtiva"]' ).text #Pesquisa débitos inscritos em dívida ativa 
        print(elemento_debito)
        df['DEBITOS'][index] = elemento_debito 

        time.sleep(5)

        chrome.execute_script("window.scrollBy(0,500)")

        elemento_total_debitos = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_Panel1"]/table[32]/tbody/tr/td[3]').text #Pesquisa de débitos totais. 
        print(elemento_total_debitos)
        df['DEBITOS TOTAIS'][index] = elemento_total_debitos

        df.to_excel('Tabela_Fipe_Valores.xlsx', index=False)

        time.sleep(2)

        chrome.back()





for df in listas: #10 linhas 
    Thread(target=pega_debitos).start()
    contador = contador + 1 
    print(contador)
    print(df)

    if contador <= 50 :
        limitar()






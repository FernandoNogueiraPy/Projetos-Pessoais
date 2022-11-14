
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd 
from selenium.webdriver.support.select import Select
import time


#Para quebrar Captcha 
import winspeech as win
import ffmpy
import requests
import pydub

nome_do_arquivo = 'TabelaFipe.xlsx'
df = pd.read_excel(r"C:\Users\Moltt\Documents\python\Empresa\TabelaFipe.xlsx")
url_do_forms = "https://veiculos.fipe.org.br/#carro-comum"


#Lendo o Execel e entrando na pagina da FIPE.
for index,row in df.iterrows():

    print("index: " + str(index) + " o nome é " + row ["CONTRATO"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)

    time.sleep(2)

    #Rolando o site para cima 1 vez.
    last_height = chrome.execute_script("return document.body.scrollHeight")

    for contador in range(1):
        chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    time.sleep(2)

    #Clikando na Busca de carros
    elemento_busca_carro = chrome.find_element(By.XPATH,'//*[@id="front"]/div[1]/div[1]/ul/li[1]/a/div[2]').click()
    time.sleep(2)


    #Selecionando a Marca
    elemento_selecione_marca = chrome.find_element(By.XPATH,'//*[@id="selectMarcacarro_chosen"]').click()

    elemento_marca = chrome.find_element(By.XPATH,'//*[@id="selectMarcacarro_chosen"]/div/div/input')
    elemento_marca.send_keys(row["MARCA"])
    elemento_marca.send_keys(Keys.ENTER)
    

    #Selecionando o Ano
    elemento_selecione_ano = chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]').click()
    
    elemento_ano = chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]/div/div/input')
    elemento_ano.send_keys(row["ANO"])
    elemento_ano.send_keys(Keys.ENTER)


    #Selecionando Modelo 
    elemento_selecione_modelo = chrome.find_element(By.XPATH,'//*[@id="selectAnoModelocarro_chosen"]').click()
    
    elemento_modelo = chrome.find_element(By.XPATH,'//*[@id="selectAnoModelocarro_chosen"]/div/div/input')
    filtro_modelo = (row["MODELO"]).split()[0]
    elemento_modelo.send_keys(filtro_modelo)
    elemento_modelo.send_keys(Keys.ENTER)


    #Pesquisar Fipe
    elemento_selecione_pesquisa = chrome.find_element(By.XPATH,'//*[@id="buttonPesquisarcarro"]').click()

    #Coletar as informações da FIPE 
    elemento_valor_fipe = chrome.find_element(By.XPATH,'//*[@id="resultadoConsultacarroFiltros"]/table/tbody/tr[8]/td[2]/p').text

    #teste 
    df['FIPE'][index] = elemento_valor_fipe

    print(df)
    
    time.sleep(3)

    
    df.to_excel('TabelaFipe.xlsx')
    


    chrome.quit()

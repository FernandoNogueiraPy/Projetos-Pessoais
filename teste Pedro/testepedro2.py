import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

caminho = "Pasta1.xlsx"


def buscar_e_preencher(caminho, url):
    # Ler o arquivo do Excel em um DataFrame
    df = pd.read_excel(caminho)
    # Iterar pelas linhas do DataFrame
    for index, row in df.iterrows():
        # Obter a placa e o renavam das colunas 'placa' e 'renavam'
        
        placa = row['placa']
        renavam = row['renavam']

        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get(url)

        time.sleep(2)
        # Preencher os campos 'placa' e 'renavam' com os valores lidos da planilha
        driver.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtPlaca"]').send_keys(placa)
        driver.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtRenavam"]').send_keys(renavam)

        # Clicar no botão de pesquisa
        #driver.find_element(By.ID,"").click()

# Abrir 10 guias no navegador da web padrão com os dados do arquivo do Excel
for i in range(10):
    buscar_e_preencher(caminho, "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx")
  


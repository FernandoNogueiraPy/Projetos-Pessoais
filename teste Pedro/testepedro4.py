import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Caminho do arquivo do Excel
caminho = "Pasta1.xlsx"

url = "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx"

def buscar_e_preencher(caminho, url):
    # Ler o arquivo do Excel em um DataFrame
    df = pd.read_excel(caminho)
    # Obter o número total de linhas da planilha
    num_linhas = df.shape[0]

    # Inicializar o webdriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # Acessar a URL da primeira guia 
    driver.get(url)

    time.sleep(3)
   
    # Iterar pelas linhas do DataFrame de 10 em 10
    for i in range(0, num_linhas, 10):
        # Obter os dados das próximas 10 linhas da planilha
        dados = df[i:i+10]
        # Iterar pelas linhas desses dados
        for index, row in dados.iterrows():
            # Obter a placa e o renavam das colunas 'placa' e 'renavam'
            placa = row['placa']
            renavam = row['renavam']
            # Preencher os campos 'placa' e 'renavam' com os valores lidos da planilha
            driver.find_element(By.XPATH,'/[@id="conteudoPaginaPlaceHolder_txtPlaca"]').send_keys(placa)
            driver.find_element(By.XPATH,'/[@id="conteudoPaginaPlaceHolder_txtRenavam"]').send_keys(renavam)
            # Clicar no botão de pesquisa
            #driver.find_element_by_id("btnPesquisar").click()
            # Aguardar alguns segundos para a página carregar
            time.sleep(5)
        # Obter a lista de guias abertas no navegador
        guias = driver.window_handles
        # Mudar para a próxima guia


buscar_e_preencher(caminho, url)
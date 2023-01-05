import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Lê o arquivo Excel como um DataFrame do pandas
df = pd.read_excel("consultas.xlsx")

# Para cada linha no DataFrame
for index, row in df.iterrows():
    # Recupera o valor da célula na primeira coluna da linha
    consulta = row[0]
    
    # Monta a URL da consulta IPVA
    url = f"http://www.fazenda.sp.gov.br/ipva/consulta-ipva.aspx?consulta={consulta}"
    
    # Envia a consulta e armazena a resposta
    resposta = requests.get(url)
    
    # Verifica se a consulta foi bem-sucedida
    if resposta.status_code != 200:
        print(f"Erro ao enviar a consulta {consulta}")
        continue
    
    # Processa a resposta com o Beautiful Soup
    soup = BeautifulSoup(resposta.text, "html.parser")
    
    # Extrai as informações da resposta e armazena em um dicionário
    dados = {}
    dados["Placa"] = soup.find("span", id="lblPlaca").text
    dados["Renavam"] = soup.find("span", id="lblRenavam").text
    dados["CPF/CNPJ"] = soup.find("span", id="lblCPFCNPJ").text
    dados["Ano/Modelo"] = soup.find("span", id="lblAnoModelo").text
    dados["Marca"] = soup.find("span", id="lblMarca").text
    dados["Nome"] = soup.find("span", id="lblNome").text
    dados["IPVA"] = soup.find("span", id="lblIpva").text
    
    # Imprime os dados no console
    print(dados)
    
    # Dá uma pausa de 5 segundos para não sobrecarregar o servidor
    time.sleep(5)
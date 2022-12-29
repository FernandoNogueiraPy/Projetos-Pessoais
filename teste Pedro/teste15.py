import pandas as pd
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




df = pd.read_excel(r'Pasta1.xlsx')



urls = [
    "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx",
    "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx",
    "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx",
    "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx",
    "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx",
    "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx",
    "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx",
    "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx",
    "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx",
    "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx",
]



for url in urls:

    webbrowser.open(url)

    for index, row in df.iterrows():
        url = row['URL']
        # Open the URL in a new web browser
        webbrowser.open(url)

        webbrowser.open_new(url)

        numb = row["NUMB"]

        print(numb)
        break
   

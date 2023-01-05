import pandas as pd 
from selenium import webdriver
from threading import Thread
from webdriver_manager.chrome import ChromeDriverManager
from asyncio import sleep


df = pd.read_excel('TestePrincipal.xlsx')

        
def Web():
    url_do_forms = "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    chrome = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    chrome.get(url_do_forms)
    sleep(3)
    chrome.quit()
    

for index,row in df.iterrows(): #10 linhas 
    Thread(target=Web).start()


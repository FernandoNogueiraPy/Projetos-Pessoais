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
url_do_forms = "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx"



for index,row in df.iterrows():

    print("index: " + str(index) + " o nome é " + row ["CONTRATO"])
    chrome = webdriver.Chrome()#service_args=["--profile-directory=Profile 4"]) #executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe',service_args=["--profile-directory=Profile 4"]) 
    #chrome.get(url_do_forms)

    time.sleep(3)

    elemento_renavam = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtRenavam"]')
    elemento_placa = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtPlaca"]')
    
    elemento_renavam.send_keys(row["RENAVAM"])
    elemento_placa.send_keys(row["PLACA"])


    frames = chrome.find_elements(By.TAG_NAME,'iframe')
    chrome.switch_to.frame(frames[0])
    time.sleep(1)
    
    chrome.find_element(By.CLASS_NAME,'recaptcha-checkbox-border').click()

    time.sleep(3)

    chrome.switch_to.default_content()
    frames=chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_g_recaptcha"]/div/div/iframe')
    chrome.switch_to.frame(frames)

    time.sleep(1)

    frame_button = chrome.find_elements(By.TAG_NAME,'iframe')
    chrome.switch_to.frame(frame_button[0])
    chrome.find_element(By.ID,"recaptcha-audio-button").click()
    

    

#chrome.quit()
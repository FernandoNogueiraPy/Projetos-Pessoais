from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from threading import Thread
import pandas as pd
import time 


df = pd.read_excel('Pasta1.xlsx')
tamanho = df.index.stop

contador = 0

url = "https://google.com"
ChromeOptions = Options()
ChromeOptions.headless = False

driver = webdriver.Chrome(options=ChromeOptions)
driver.implicitly_wait(10)
driver.get(url)

print('Abriu o navegador')


def entrada():

    url = "https://google.com"
    ChromeOptions = Options()
    ChromeOptions.headless = False

    driver = webdriver.Chrome(options=ChromeOptions)
    driver.implicitly_wait(10)
    driver.get(url)
    
    print('Abriu o navegador')
    Webs(driver,url)


def Webs():

    driver.get(url)

    elemento_pesquisa = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        
    elemento_pesquisa.send_keys(row["TESTE"])

    elemento_pesquisa.send_keys(Keys.ENTER)

    time.sleep(3)

    elemento_avancar = driver.find_element(By.XPATH,'//*[@id="rso"]/div[2]/div/div/div/div[1]/div/a/h3').click()

    time.sleep(3)

    elemento_pegar = driver.find_element(By.XPATH,'//*[@id="speed-value"]').text

    time.sleep(3)

    print(elemento_pegar)

    df["RESULTADO"][index] = 'SALVO'

    df.to_excel('teste1.xlsx',index=False)

    print(contador)

              
for index,row in df.iterrows():       
    Webs()

    contador = contador + 1

    if contador == 5:
            
        contador = 0

        url = "https://google.com"
        ChromeOptions = Options()
        ChromeOptions.headless = False

        driver.quit()

        driver = webdriver.Chrome(options=ChromeOptions)
        driver.implicitly_wait(10)
        driver.get(url)



#Quantidade_Web = int(input('Quantas webs deseja abrir:  '))
#Esolher_quantidade(Quantidade_Web)
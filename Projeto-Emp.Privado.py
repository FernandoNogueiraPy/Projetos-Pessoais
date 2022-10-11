from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd 
import pyautogui
import time

#Localização do arquivo dentro do PC.
nome_do_arquivo = 'TestePrograma.xlsx'
df = pd.read_excel("TestePrograma.xlsx")
url_do_forms = "https://esaj.tjsp.jus.br/sco/abrirCadastro.do"


#Leitura dos dados = nome do arquivo = Falencias 
for index,row in df.iterrows():
    print("index: " + str(index) + " o nome é " + row ["Nome"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)
    time.sleep(3) 

    #Documento selecionado nessa função = Falencias
    pyautogui.press(['down']) 


#Se for Pessoa Júridica ele preenchera automatico os dados
    if row ["Pessoa"] == "Juridica":
     elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaJ"]').click()

     time.sleep(1)

     elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroJ"]') 
     elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuCnpjFormatado"]')

     elemento_texto_Nome.send_keys(row["Nome"])
     elemento_texto_Rg.send_keys(row["Rg"])

#Se For Pessoa Fisica ele preenchera os automatico os dados 
    else :
        elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaF"]').click()
    
      #Masculino 
        if row["Sexo"] == "M": 
            elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[1]/label/input').click()
        
            elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
            elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
            elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
        
            elemento_texto_Nome.send_keys(row["Nome"])
            elemento_texto_Rg.send_keys(row["Rg"])
            elemento_texto_Cpf.send_keys(row["Cpf"])
      #Feminino
        else :
         elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[2]/label/input').click()

         elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
         elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
         elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
        
         elemento_texto_Nome.send_keys(row["Nome"])
         elemento_texto_Rg.send_keys(row["Rg"])
         elemento_texto_Cpf.send_keys(row["Cpf"])

#Leitura dos dados = nome do arquivo = Civeis
for index,row in df.iterrows():
    print("index: " + str(index) + " o nome é " + row ["Nome"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)
    time.sleep(3) 

    #Documento selecionado nessa função = Falencias
    pyautogui.press(['down']) 
    pyautogui.press(['down']) 
    pyautogui.press(['down']) 
    pyautogui.press(['down']) 

#Se for Pessoa Júridica ele preenchera automatico os dados
    if row ["Pessoa"] == "Juridica":
     elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaJ"]').click()

     time.sleep(1)

     elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroJ"]') 
     elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuCnpjFormatado"]')

     elemento_texto_Nome.send_keys(row["Nome"])
     elemento_texto_Rg.send_keys(row["Rg"])

#Se For Pessoa Fisica ele preenchera os automatico os dados 
    else :
        elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaF"]').click()
    
      #Masculino 
        if row["Sexo"] == "M": 
            elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[1]/label/input').click()
        
            elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
            elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
            elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
        
            elemento_texto_Nome.send_keys(row["Nome"])
            elemento_texto_Rg.send_keys(row["Rg"])
            elemento_texto_Cpf.send_keys(row["Cpf"])
      #Feminino
        else :
         elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[2]/label/input').click()

         elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
         elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
         elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
        
         elemento_texto_Nome.send_keys(row["Nome"])
         elemento_texto_Rg.send_keys(row["Rg"])
         elemento_texto_Cpf.send_keys(row["Cpf"])

#Leitura dos dados = nome do arquivo = Saj5
for index,row in df.iterrows():

    print("index: " + str(index) + " o nome é " + row ["Nome"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)
    time.sleep(3) 

    #Documento selecionado nessa função = Falencias
    pyautogui.press(['down']) 
    pyautogui.press(['down']) 
    pyautogui.press(['down']) 
 

#Se for Pessoa Júridica ele preenchera automatico os dados
    if row ["Pessoa"] == "Juridica":
     elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaJ"]').click()

     time.sleep(1)

     elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroJ"]') 
     elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuCnpjFormatado"]')
     

     elemento_texto_Nome.send_keys(row["Nome"])
     elemento_texto_Rg.send_keys(row["Rg"])
     


#Se For Pessoa Fisica ele preenchera os automatico os dados 
    else :
        elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaF"]').click()
    
      #Masculino 
        if row["Sexo"] == "M": 
            elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[1]/label/input').click()
        
            elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
            elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
            elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
            elemento_texto_Nome_Mae = chrome.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
            elemento_texto_Datanasc = chrome.find_element(By.XPATH,'//*[@id="dataNascimento"]')


            elemento_texto_Nome.send_keys(row["Nome"])
            elemento_texto_Rg.send_keys(row["Rg"])
            elemento_texto_Cpf.send_keys(row["Cpf"])
            elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])
            elemento_texto_Datanasc.send_keys(row["Datanasc"])

      #Feminino
        else :
         elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[2]/label/input').click()

         elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
         elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
         elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
         elemento_texto_Nome_Mae = chrome.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
         elemento_texto_Datanasc = chrome.find_element(By.XPATH,'//*[@id="dataNascimento"]')


         elemento_texto_Nome.send_keys(row["Nome"])
         elemento_texto_Rg.send_keys(row["Rg"])
         elemento_texto_Cpf.send_keys(row["Cpf"])
         elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])
         elemento_texto_Datanasc.send_keys(row["Datanasc"])

#Leitura dos dados = nome do arquivo = Ações Criminais 
for index,row in df.iterrows():

    print("index: " + str(index) + " o nome é " + row ["Nome"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)
    time.sleep(3) 

    #Documento selecionado nessa função = Falencias
    pyautogui.press(['down']) 
    pyautogui.press(['down']) 
    pyautogui.press(['down']) 
    pyautogui.press(['down']) 
    pyautogui.press(['down'])
    pyautogui.press(['down'])

#Se for Pessoa Júridica ele preenchera automatico os dados
    if row ["Pessoa"] == "Juridica":
     elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaJ"]').click()

     time.sleep(1)

     elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroJ"]') 
     elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuCnpjFormatado"]')

     elemento_texto_Nome.send_keys(row["Nome"])
     elemento_texto_Rg.send_keys(row["Rg"])

#Se For Pessoa Fisica ele preenchera os automatico os dados 
    else :
        elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaF"]').click()
    
      #Masculino 
        if row["Sexo"] == "M": 
            elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[1]/label/input').click()
        
            elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
            elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
            elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
            elemento_texto_Nome_Mae = chrome.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
            elemento_texto_Datanasc = chrome.find_element(By.XPATH,'//*[@id="dataNascimento"]')


            elemento_texto_Nome.send_keys(row["Nome"])
            elemento_texto_Rg.send_keys(row["Rg"])
            elemento_texto_Cpf.send_keys(row["Cpf"])
            elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])
            elemento_texto_Datanasc.send_keys(row["Datanasc"])


      #Feminino
        else :
         elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[2]/label/input').click()

         elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
         elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
         elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
         elemento_texto_Nome_Mae = chrome.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
         elemento_texto_Datanasc = chrome.find_element(By.XPATH,'//*[@id="dataNascimento"]')



         elemento_texto_Nome.send_keys(row["Nome"])
         elemento_texto_Rg.send_keys(row["Rg"])
         elemento_texto_Cpf.send_keys(row["Cpf"])
         elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])
         elemento_texto_Datanasc.send_keys(row["Datanasc"])

#Leitura dos dados =  nome do arquivo = Sivec
for index,row in df.iterrows():
    print("index: " + str(index) + " o nome é " + row ["Nome"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)
    time.sleep(3) 

    #Documento selecionado nessa função = Falencias
    pyautogui.press(['down']) 
    pyautogui.press(['down']) 
    pyautogui.press(['down']) 
    pyautogui.press(['down']) 
    pyautogui.press(['down'])
    pyautogui.press(['down'])
    pyautogui.press(['down'])

#Se for Pessoa Júridica ele preenchera automatico os dados
    if row ["Pessoa"] == "Juridica":
     elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaJ"]').click()

     time.sleep(1)

     elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroJ"]') 
     elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuCnpjFormatado"]')

     elemento_texto_Nome.send_keys(row["Nome"])
     elemento_texto_Rg.send_keys(row["Rg"])

#Se For Pessoa Fisica ele preenchera os automatico os dados 
    else :
        elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaF"]').click()
    
      #Masculino 
        if row["Sexo"] == "M": 
            elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[1]/label/input').click()
        
            elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
            elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
            elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
            elemento_texto_Nome_Mae = chrome.find_element(By.XPATH,'')
            

            elemento_texto_Nome.send_keys(row["Nome"])
            elemento_texto_Rg.send_keys(row["Rg"])
            elemento_texto_Cpf.send_keys(row["Cpf"])
            elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])
      #Feminino
        else :
         elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[2]/label/input').click()

         elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
         elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
         elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
         elemento_texto_Nome_Mae = chrome.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')



         elemento_texto_Nome.send_keys(row["Nome"])
         elemento_texto_Rg.send_keys(row["Rg"])
         elemento_texto_Cpf.send_keys(row["Cpf"])
         elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])

chrome.quit
    



#documento 2 

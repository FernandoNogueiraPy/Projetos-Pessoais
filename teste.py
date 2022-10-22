#Documento de Falencia - Certidão


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 


a = 0
nome_do_arquivo = 'TestePrograma.xlsx'
df = pd.read_excel("TestePrograma.xlsx")

url_do_forms = "https://esaj.tjsp.jus.br/sco/abrirCadastro.do"


for index,row in df.iterrows():
    print("index: " + str(index) + " o nome é " + row ["Nome"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)

    time.sleep(5) 

    #Documento selecionado nessa função = Falencias
    elemento_selecao = Select(chrome.find_element(By.XPATH,'//*[@id="cdModelo"]'))
    elemento_selecao.select_by_index(3)
    

#Se for Pessoa Júridica ele preenchera automatico os dados
    if row ["Pessoa"] == "Juridica":
     elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaJ"]').click()
     time.sleep(3)

     elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroJ"]') 
     elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuCnpjFormatado"]')
     
     elemento_texto_Nome.send_keys(row["Nome"])
     elemento_texto_Rg.send_keys(row["Rg"])

     time.sleep(2)
     
     #Preencher Email
     chrome.find_element(By.ID,"identity.solicitante.deEmail").send_keys('fernandomoltt101@gmail.com') 
     #Clikar em confirmação 
     chrome.find_element(By.ID,"confirmacaoInformacoes").click()
     #Clikar em Enviar
     chrome.find_element(By.ID,"pbEnviar").click()

     print('Documento de Falencias emitido com Sucesso.')

     time.sleep(15)


#Se For Pessoa Fisica ele preenchera os automatico os dados 
    else :
        elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaF"]').click()

        time.sleep(2)
    
      #Masculino 
        if row["Sexo"] == "M": 
            df ['Datanasc'] = df['Datanasc'].dt.strftime('%d-%m-%Y')
            elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[1]/label/input').click()
        
            elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
            elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
            elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
            elemento_texto_Nome_Mae = chrome.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
            elemento_texto_Datanasc = chrome.find_element(By.XPATH,'//*[@id="dataNascimento"]')


            time.sleep(4)

            elemento_texto_Nome.send_keys(row["Nome"])
            elemento_texto_Rg.send_keys(row["Rg"])
            elemento_texto_Cpf.send_keys(row["Cpf"])
            elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])
            elemento_texto_Datanasc.send_keys(row["Datanasc"])

            chrome.find_element(By.ID,"identity.solicitante.deEmail").send_keys('fernandomoltt101@gmail.com') 
            #Clikar em confirmação 
            chrome.find_element(By.ID,"confirmacaoInformacoes").click()
            #Clikar em Enviar
            chrome.find_element(By.ID,"pbEnviar")

            print('Documento de Falencias emitido com Sucesso.')
            #Copiar protocolo 
            elemento_texto_protocolo = chrome.find_elements(By.XPATH,'//*[@id="deEmail"]/td[1]/label')
            #print(elemento_texto_protocolo)

      #Feminino
        else :
            df ['Datanasc'] = df['Datanasc'].dt.strftime('%d-%m-%Y')
            elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[2]/label/input').click()

            elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
            elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
            elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
            elemento_texto_Nome_Mae = chrome.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
            elemento_texto_Datanasc = chrome.find_element(By.XPATH,'//*[@id="dataNascimento"]')

            time.sleep(4)

            elemento_texto_Nome.send_keys(row["Nome"])
            elemento_texto_Rg.send_keys(row["Rg"])
            elemento_texto_Cpf.send_keys(row["Cpf"])
            elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])
            elemento_texto_Datanasc.send_keys(row["Datanasc"])
            time.sleep(3)

            chrome.find_element(By.ID,"identity.solicitante.deEmail").send_keys('fernandomoltt101@gmail.com') 
            #Clikar em confirmação 
            chrome.find_element(By.ID,"confirmacaoInformacoes").click()
            #Clikar em Enviar
            chrome.find_element(By.ID,"pbEnviar").click()
            print('Documento de Falencias emitido com Sucesso.')


            time.sleep(15)
       
    chrome.quit()         

a = 0
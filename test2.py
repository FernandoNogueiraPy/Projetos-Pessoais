
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd 
from selenium.webdriver.support.select import Select
import time

  #Localização do arquivo dentro do PC.
  nome_do_arquivo = 'TestePrograma.xlsx'
  df = pd.read_excel("TestePrograma.xlsx")
  df ['Datanasc'] = df['Datanasc'].dt.strftime('%d-%m-%Y')
  url_do_forms = "https://esaj.tjsp.jus.br/sco/abrirCadastro.do"




  escolher_docs = input(""" 

  Escolhas os documento que deseja emitir.

  [0] - Emita todos os documentos de uma vez

  [1] - Certidão Falencias
  [2] - Certidão Civeis
  [3] - Certidão Saj5 
  [4] - Certidão Ações Criminais
  [5] - Certidão Sivec

  [6] - Feche o programa 

  """)

  print(escolher_docs)
 

#Leitura dos dados = nome do arquivo = Falencias 
if escolher_docs == '1':

    for index,row in df.iterrows():

    print("index: " + str(index) + " o nome é " + row ["Nome"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)
    time.sleep(8) 

        #Documento selecionado nessa função = Falencias
        
    elemento_selecao = Select(chrome.find_element(By.XPATH,'//*[@id="cdModelo"]'))
    elemento_selecao.select_by_index(1)

    time.sleep(2)


    #Se for Pessoa Júridica ele preenchera automatico os dados
    if row ["Pessoa"] == "Juridica":
        elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaJ"]').click()

        time.sleep(3)
                
        elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroJ"]')
        elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuCnpjFormatado"]')

        elemento_texto_Nome.send_keys(row["Nome"])
        elemento_texto_Rg.send_keys(row["Rg"])

        time.sleep(3)

        elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

        chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

        time.sleep(2)

        chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()

        print('Documento: Falencias emitido com sucesso.')



    #Se For Pessoa Fisica ele preenchera os automatico os dados 
    else :
        df ['Datanasc'] = df['Datanasc'].dt.strftime('%d-%m-%Y')
        elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaF"]').click()
        
            #Masculino 
        if row["Sexo"] == "M": 
            elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[1]/label/input').click()
            
            elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
            elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
            elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
            
            time.sleep(3)

            elemento_texto_Nome.send_keys(row["Nome"])
            elemento_texto_Rg.send_keys(row["Rg"])
            elemento_texto_Cpf.send_keys(row["Cpf"])

            elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
            elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

            chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

            time.sleep(3)

            chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()
            print('Documento: Falencias emitido com sucesso.')

            #Feminino
        else :
            elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[2]/label/input').click()

            elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
            elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
            elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')

            time.sleep(2)
                
            elemento_texto_Nome.send_keys(row["Nome"])
            elemento_texto_Rg.send_keys(row["Rg"])
            elemento_texto_Cpf.send_keys(row["Cpf"])

            elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
            elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

            chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

            time.sleep(3)

            chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()

            print('Documento: Falencias emitido com sucesso.')

        

  time.sleep(3)
  chrome.quit()
#Leitura dos dados = nome do arquivo = Civeis
for index,row in df.iterrows():
  print("index: " + str(index) + " o nome é " + row ["Nome"])
  chrome = webdriver.Chrome()
  chrome.get(url_do_forms)
  time.sleep(8) 

#Documento selecionado nessa função = Falencias
  elemento_selecao = Select(chrome.find_element(By.XPATH,'//*[@id="cdModelo"]'))
  elemento_selecao.select_by_index(4)

  time.sleep(2)

#Se for Pessoa Júridica ele preenchera automatico os dados
  if row ["Pessoa"] == "Juridica":
    elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaJ"]').click()

    time.sleep(3)

    elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroJ"]') 
    elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuCnpjFormatado"]')

    time.sleep(2)

    elemento_texto_Nome.send_keys(row["Nome"])
    elemento_texto_Rg.send_keys(row["Rg"])

    elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
    elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

    chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

    time.sleep(2)

    chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()

#Se For Pessoa Fisica ele preenchera os automatico os dados 
  else :
    elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaF"]').click()
      
#Masculino 
    if row["Sexo"] == "M": 
        elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[1]/label/input').click()
        
        elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
        elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
        elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')

        time.sleep(2)
          
        elemento_texto_Nome.send_keys(row["Nome"])
        elemento_texto_Rg.send_keys(row["Rg"])
        elemento_texto_Cpf.send_keys(row["Cpf"])

        time.sleep(2)

        elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

        chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

        time.sleep(2)

        chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()

        #Feminino
    else :
      elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[2]/label/input').click()

      elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
      elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
      elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')

      time.sleep(2)
            
      elemento_texto_Nome.send_keys(row["Nome"])
      elemento_texto_Rg.send_keys(row["Rg"])
      elemento_texto_Cpf.send_keys(row["Cpf"])

      time.sleep(2)

      elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
      elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

      chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

      time.sleep(2)

      chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()

  chrome.quit()   
#Leitura dos dados = nome do arquivo = Saj5
for index,row in df.iterrows():

  print("index: " + str(index) + " o nome é " + row ["Nome"])
  chrome = webdriver.Chrome()
  chrome.get(url_do_forms)
  time.sleep(8) 

  elemento_selecao = Select(chrome.find_element(By.XPATH,'//*[@id="cdModelo"]'))
  elemento_selecao.select_by_index(3)

  time.sleep(2)
  

#Se for Pessoa Júridica ele preenchera automatico os dados
  if row ["Pessoa"] == "Juridica":
    elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaJ"]').click()

    time.sleep(2)

    elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroJ"]') 
    elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuCnpjFormatado"]')
        
    elemento_texto_Nome.send_keys(row["Nome"])
    elemento_texto_Rg.send_keys(row["Rg"])

    time.sleep(3)

    elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
    elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

    chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

    time.sleep(3)

    chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()

     
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

        time.sleep(2)

        elemento_texto_Nome.send_keys(row["Nome"])
        elemento_texto_Rg.send_keys(row["Rg"])
        elemento_texto_Cpf.send_keys(row["Cpf"])
        elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])
        elemento_texto_Datanasc.send_keys(row["Datanasc"])

        time.sleep(2)

        elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

        chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

        time.sleep(2)

        chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()

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

        time.sleep(2)

        elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

        chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

        time.sleep(2)

        chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()
  
  
  chrome.quit()            
#Leitura dos dados = nome do arquivo = Ações Criminais 
for index,row in df.iterrows():

  print("index: " + str(index) + " o nome é " + row ["Nome"])
  chrome = webdriver.Chrome()
  chrome.get(url_do_forms)
  time.sleep(8) 

#Documento selecionado nessa função = Falencias
  elemento_selecao = Select(chrome.find_element(By.XPATH,'//*[@id="cdModelo"]'))
  elemento_selecao.select_by_index(6)

  time.sleep(2)

#Se for Pessoa Júridica ele preenchera automatico os dados
  if row ["Pessoa"] == "Juridica":
    elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaJ"]').click()

    time.sleep(3)

    elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroJ"]') 
    elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuCnpjFormatado"]')

    elemento_texto_Nome.send_keys(row["Nome"])
    elemento_texto_Rg.send_keys(row["Rg"])

    elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
    elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

    chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

    time.sleep(3)

    chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()

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

        time.sleep(3)

        elemento_texto_Nome.send_keys(row["Nome"])
        elemento_texto_Rg.send_keys(row["Rg"])
        elemento_texto_Cpf.send_keys(row["Cpf"])
        elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])
        elemento_texto_Datanasc.send_keys(row["Datanasc"])
        

        elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

        chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

        time.sleep(3)

        chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()


        #Feminino
      else :
        elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[2]/label/input').click()

        elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
        elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
        elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
        elemento_texto_Nome_Mae = chrome.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
        elemento_texto_Datanasc = chrome.find_element(By.XPATH,'//*[@id="dataNascimento"]')

        time.sleep(3)

        elemento_texto_Nome.send_keys(row["Nome"])
        elemento_texto_Rg.send_keys(row["Rg"])
        elemento_texto_Cpf.send_keys(row["Cpf"])
        elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])
        elemento_texto_Datanasc.send_keys(row["Datanasc"])

        elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

        chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

        time.sleep(3)

        chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()
  
  
  chrome.quit()
#Leitura dos dados =  nome do arquivo = Sivec
for index,row in df.iterrows():

  print("index: " + str(index) + " o nome é " + row ["Nome"])
  chrome = webdriver.Chrome()
  chrome.get(url_do_forms)
  time.sleep(8) 

#Documento selecionado nessa função = Falencias
  elemento_selecao = Select(chrome.find_element(By.XPATH,'//*[@id="cdModelo"]'))
  elemento_selecao.select_by_index(7)

  time.sleep(2)
#Se for Pessoa Júridica ele preenchera automatico os dados
  if row ["Pessoa"] == "Juridica":
    elemento_texto_Pessoa = chrome.find_element(By.XPATH,'//*[@id="tpPessoaJ"]').click()

    time.sleep(3)

    elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroJ"]') 
    elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuCnpjFormatado"]')

    elemento_texto_Nome.send_keys(row["Nome"])
    elemento_texto_Rg.send_keys(row["Rg"])

    elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
    elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

    chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

    time.sleep(3)

    chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()



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

        time.sleep(3)
              

        elemento_texto_Nome.send_keys(row["Nome"])
        elemento_texto_Rg.send_keys(row["Rg"])
        elemento_texto_Cpf.send_keys(row["Cpf"])
        elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])

        elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

        chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

        time.sleep(3)

        chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()

#Feminino
      else :
        elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[2]/label/input').click()

        elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
        elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
        elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
        elemento_texto_Nome_Mae = chrome.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')

        time.sleep(3)


        elemento_texto_Nome.send_keys(row["Nome"])
        elemento_texto_Rg.send_keys(row["Rg"])
        elemento_texto_Cpf.send_keys(row["Cpf"])
        elemento_texto_Nome_Mae.send_keys(row["Nome mãe"])

        elemento_texto_email = chrome.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        elemento_texto_email.send_keys('fernando.costa@gcrdocumentacaoimobiliaria.com.br')

        chrome.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]').click()

        time.sleep(3)

        chrome.find_element(By.XPATH,'//*[@id="pbEnviar"]').click()
  
  time.sleep(3)
chrome.quit()
    
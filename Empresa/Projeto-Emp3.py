
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd 
from selenium.webdriver.support.select import Select
import time




nome_do_arquivo = 'TabelaFipe.xlsx'
df = pd.read_excel(r"C:\Users\Moltt\Documents\python\Empresa\TabelaFipe.xlsx")
url_do_forms = "https://veiculos.fipe.org.br/#carro-comum"


#Lendo o Execel e entrando na pagina da FIPE.
for index,row in df.iterrows():

    print("index: " + str(index) + " o nome é " + row ["CONTRATO"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)

    time.sleep(2)

    #Rolando o site para cima 1 vez.
    #last_height = chrome.execute_script("return document.body.scrollHeight")

    #for contador in range(1):
    chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    time.sleep(2)

    #Clikando na Busca de carros
    elemento_busca_carro = chrome.find_element(By.XPATH,'//*[@id="front"]/div[1]/div[1]/ul/li[1]/a/div[2]').click()
    time.sleep(2)


    #Selecionando a Marca
    elemento_selecione_marca = chrome.find_element(By.XPATH,'//*[@id="selectMarcacarro_chosen"]').click()
    elemento_marca = chrome.find_element(By.XPATH,'//*[@id="selectMarcacarro_chosen"]/div/div/input')
    correto_marca = (row["MARCA"])


    #Correção de nome de marcas
    if correto_marca == 'CITROEN':
        trocar_marca = correto_marca.replace('CITROEN','Citroën')
        elemento_marca.send_keys(trocar_marca)


    else:
        elemento_marca.send_keys(correto_marca)


    elemento_marca.send_keys(Keys.ENTER)


    #Selecionando o Ano
    elemento_selecione_ano = chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]').click()
    
    elemento_ano = chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]/div/div/input')
    elemento_ano_correto = (row["ANO"]).split('/')[1]
    elemento_ano.send_keys(elemento_ano_correto)
    elemento_ano.send_keys(Keys.ENTER)




    #Selecionando Modelo 
    elemento_selecione_modelo = chrome.find_element(By.XPATH,'//*[@id="selectAnoModelocarro_chosen"]').click()
    
    elemento_modelo = chrome.find_element(By.XPATH,'//*[@id="selectAnoModelocarro_chosen"]/div/div/input')
    correto_nome = (row["MODELO"])
    
    

    listagem = ['- 0P -  - '],'- 5P - Básico - '#'- 2P - Básico - ','- 4P - Básico - ',
    #'- 3P - Básico -','- 0P - Básico - ','- 0p - - ']

    
   
    for item in listagem:
        if item not in correto_nome:
                elemento_modelo.send_keys(correto_nome)
                      
        else: 
            nome_novo = correto_nome.replace(item,'')
            elemento_modelo.send_keys(nome_novo)


    time.sleep(5)

    elemento_modelo.send_keys(Keys.ENTER)

    time.sleep(1)
    

    #Pesquisar Fipe
    elemento_selecione_pesquisa = chrome.find_element(By.XPATH,'//*[@id="buttonPesquisarcarro"]').click()


    #Coletar as informações da FIPE 
    elemento_valor_fipe = chrome.find_element(By.XPATH,'//*[@id="resultadoConsultacarroFiltros"]/table/tbody/tr[8]/td[2]/p').text

    time.sleep(3)

    if elemento_valor_fipe == False:
        print('Não foi possivel pesquisar, Motivo = Precisa preencher todos os campos corretos.')
        df['FIPE'][index] = 'Falta dados corretos.'

    else:
        #Colocar informação do valor da fipe na Coluna FIPE do execel.
        df['FIPE'][index] = elemento_valor_fipe

    
    #df['FIPE'][index] = 'Pequisa fora do padrao'

    #Cria o novo execel com os valores que estão sendo pesquisado
    df.to_excel('Tabela_Fipe_Erros.xlsx', index=False)




    df2 = pd.read_excel(r"C:\Users\Moltt\Documents\python\Tabela_Fipe_Atualizada.xlsx")


    chrome.quit()





criador = """\n / Developer/ Fernando Nogueira Costa / \n"""
print(criador)

dados_criador = """ / Qualquer Alteração do programa , ou atualização da pagina
Tabela Fipe, procurar / https://github.com/FernandoNogueiraPy  / \n"""

print(dados_criador)

print('#'*40)



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd 
from selenium.webdriver.support.select import Select
import time




nome_do_arquivo = 'TabelaFipe.xlsx'
df = pd.read_excel(r"C:\Users\Moltt\Documents\python\Empresa\TabelaFipe.xlsx") #Adicionar caminho do arquivo.
url_do_forms = "https://veiculos.fipe.org.br/#carro-comum"



def clicar(xpath):
    lock = True
    while lock == True:
        try:
            a = chrome.find_element(By.XPATH, f"{xpath}")
            a.click()
            print(f"Cliquei em | {xpath}")
            lock = False
            time.sleep(0.5)
        except:
            time.sleep(1)
            pass

def caminhoes():
#Pesquisa Caminhão. 
    
    print("index: " + str(index) + " o nome é " + row ["CONTRATO"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)

    time.sleep(2)

    chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)

    #Clikando na Busca de caminhões 
    clicar('//*[@id="front"]/div[1]/div[1]/ul/li[2]/a/div[2]')
    time.sleep(2)


    #Selecionando a Marca
    clicar('//*[@id="selectMarcacaminhao_chosen"]/a/div/b')
    elemento_marca = chrome.find_element(By.XPATH,'//*[@id="selectMarcacaminhao_chosen"]/div/div/input')
    correto_marca = (row["MARCA"])
    elemento_marca.send_keys(correto_marca)
    elemento_marca.send_keys(Keys.ENTER)


        #Selecionando o Ano
    clicar('//*[@id="selectAnocaminhao_chosen"]/a/div/b')
    elemento_ano = chrome.find_element(By.XPATH,'//*[@id="selectAnocaminhao_chosen"]/div/div/input')
    elemento_ano_correto = (row["ANO"]).split('/')[1]
    elemento_ano.send_keys(elemento_ano_correto)
    elemento_ano.send_keys(Keys.ENTER)

        #Selecionando Modelo 
    clicar('//*[@id="selectAnoModelocaminhao_chosen"]/a/div/b')
    
    elemento_modelo = chrome.find_element(By.XPATH,'//*[@id="selectAnoModelocaminhao_chosen"]/div/div/input')

    Lista_correcao_portas = ['- 0P -  - ','- 5P - Básico - ',
        '- 2P - Básico - ','- 4P - Básico - ',
        '- 3P - Básico -','- 0P - Básico - ','- 0p - - ']

    #Correção de combustivel e portas 
    corringindo_modelo = (row["MODELO"])

    
    for portas in Lista_correcao_portas:
        if portas in corringindo_modelo:
            modelo_corrigido_portas = corringindo_modelo.replace(portas,'')


    time.sleep(2)

    elemento_modelo.send_keys(modelo_corrigido_portas)
    elemento_modelo.send_keys(Keys.ENTER)

    time.sleep(1)
    

    #Pesquisar Fipe
    elemento_selecione_pesquisa = chrome.find_element(By.XPATH,'//*[@id="buttonPesquisarcaminhao"]').click()


    #Coletar as informações da FIPE 
    elemento_valor_fipe = chrome.find_element(By.XPATH,'//*[@id="resultadoConsultacaminhaoFiltros"]/table/tbody/tr[8]/td[2]/p').text

    time.sleep(3)

    if elemento_valor_fipe == False:
        print('Não foi possivel pesquisar, Motivo = Precisa preencher todos os campos corretos.')
        df['FIPE'][index] = 'Não foi possivel emitir.'

    else:
        #Colocar informação do valor da fipe na Coluna FIPE do execel.
        df['FIPE'][index] = elemento_valor_fipe


    #Cria o novo execel com os valores que estão sendo pesquisado
    df.to_excel('Tabela_Fipe_valores.xlsx', index=False)

    time.sleep(1)

    chrome.quit()

def carros():
#Lendo o Execel e entrando na pagina da FIPE.
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
    clicar('//*[@id="front"]/div[1]/div[1]/ul/li[1]/a/div[2]')

    time.sleep(2)

    chrome.execute_script("window.scrollBy(0,50)")

    #Selecionando a Marca
    clicar('//*[@id="selectMarcacarro_chosen"]')
    elemento_marca = chrome.find_element(By.XPATH,'//*[@id="selectMarcacarro_chosen"]/div/div/input')
    correto_marca = (row["MARCA"])


    #Correção de nome de marcas
    if correto_marca == 'CITROEN':
        trocar_marca = correto_marca.replace('CITROEN','Citroën')
        elemento_marca.send_keys(trocar_marca)


    else:
        elemento_marca.send_keys(correto_marca)


    elemento_marca.send_keys(Keys.ENTER)

    

    #Selecionando Modelo 
    clicar('//*[@id="selectAnoModelocarro_chosen"]')
    
    elemento_modelo = chrome.find_element(By.XPATH,'//*[@id="selectAnoModelocarro_chosen"]/div/div/input')
     
    Lista_correcao_diesel = ['(diesel)','(DIESEL)',
        ' Diesel',' DIESEL','(die)',' Dies']
        
        
    Lista_correcao_portas = ['- 0P -  -  ','- 5P - Básico - ',
        '- 2P - Básico - ','- 4P - Básico - ',
        '- 3P - Básico -','- 0P - Básico - ','- 0p - - ','- 0P -  - ']


    #Correção de combustivel e portas 
    corringindo_modelo = (row["MODELO"])

    
    for portas in Lista_correcao_portas:
        if portas in corringindo_modelo:
            modelo_corrigido_portas = corringindo_modelo.replace(portas,'')
            elemento_modelo.send_keys(modelo_corrigido_portas)
            elemento_modelo.send_keys(Keys.ENTER)
            break

        elif portas not in corringindo_modelo:
            corrigindo_modelo1 = corringindo_modelo
            break



    for diesel in Lista_correcao_diesel:
        if diesel in modelo_corrigido_portas:
            modelo_corrigido_completo = modelo_corrigido_portas.replace(diesel,'')
            elemento_modelo.send_keys(modelo_corrigido_completo)
            elemento_modelo.send_keys(Keys.ENTER)
            break

        elif diesel not in corrigindo_modelo1:
           elemento_modelo.send_keys(corrigindo_modelo1)
           elemento_modelo.send_keys(Keys.ENTER)
           break
   

        
    time.sleep(2)
    
    if diesel in corringindo_modelo:
        #Selecionando Ano e Diesel
        chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]').click() #Selecione Ano.
        elemento_ano = chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]/div/div/input')
        elemento_ano_correto = (row["ANO"]).split('/')[1]
        elemento_ano.send_keys(elemento_ano_correto +' Diesel')
        elemento_ano.send_keys(Keys.ENTER)


    else:
        #Selecionando Ano e Gasolina
        elemento_selecione_ano = chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]').click()     
        elemento_ano = chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]/div/div/input')
        elemento_ano_correto = (row["ANO"]).split('/')[1]
        elemento_ano.send_keys(elemento_ano_correto +' Gasolina')
        elemento_ano.send_keys(Keys.ENTER)




    #Pesquisar Fipe
    clicar('//*[@id="buttonPesquisarcarro"]')


    #Coletar as informações da FIPE 
    elemento_valor_fipe = chrome.find_element(By.XPATH,'//*[@id="resultadoConsultacarroFiltros"]/table/tbody/tr[8]/td[2]/p').text

    print(elemento_valor_fipe)
    time.sleep(3)

    if elemento_valor_fipe == False:
        print('Não foi possivel pesquisar, Motivo = Precisa preencher todos os campos corretos.')
        df['FIPE'][index] = 'Falta dados corretos.'

    #Colocar informação do valor da fipe na Coluna FIPE do execel.
    else:
        df['FIPE'][index] = elemento_valor_fipe
        
    #Cria o novo execel com os valores que estão sendo pesquisado
    df.to_excel('Tabela_Fipe_valores.xlsx', index=False)

    chrome.quit()

#Escolha entre Carro/Caminhão
for index,row in df.iterrows():

    Tipo = (row ["CONTRATO"]) #Exp : 44-519190/20
    time.sleep(3)

    print(Tipo)
    Tipo2 = Tipo.split('-')[0]
    Tipo3 = int(Tipo2)

    print(Tipo2)

    ListaC = [40,41,42,43,44,45,46,47,48,49]


    if Tipo3 in ListaC:
        print(Tipo3)
        print('Ativou pesquisa caminhão')
        caminhoes()
        

    else:
        print(Tipo3)
        print('Ativou pesquisa carros')
        carros()
        
        
        
    

    
        
    

    
        
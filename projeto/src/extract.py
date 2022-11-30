from tkinter import *
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd 
import time
from selenium.webdriver.firefox.options import Options
from anticaptchaofficial.recaptchav2proxyless import *
import src.interface as inter
from webdriver_manager.chrome import ChromeDriverManager




def Iniciar():
    url_do_forms = "https://veiculos.fipe.org.br/#carro-comum"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    global chrome
    chrome = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    chrome.get(url_do_forms)
    leitura(filepath)

    
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


def caminhoes(df,index,row):
 #Pesquisa Caminhão.  
    
    print("index: " + str(index) + " o nome é " + row ["CONTRATO"])

    clicar('//*[@id="front"]/div[1]/div[3]/a/figure/img')

    time.sleep(2)

   
    chrome.execute_script("window.scrollTo(8, document.body.scrollHeight);")

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

    time.sleep(2)
    

    #Pesquisar Fipe
    elemento_selecione_pesquisa = chrome.find_element(By.XPATH,'//*[@id="buttonPesquisarcaminhao"]').click()


    #Coletar as informações da FIPE 
    elemento_valor_fipe = chrome.find_element(By.XPATH,'//*[@id="resultadoConsultacaminhaoFiltros"]/table/tbody/tr[8]/td[2]/p').text

    print(elemento_valor_fipe)
    time.sleep(2)

    if elemento_valor_fipe == False:
        print('Não foi possivel pesquisar, Motivo = Precisa preencher todos os campos corretos.')
        df['FIPE'][index] = 'Não foi possivel emitir.'

    else:
        #Colocar informação do valor da fipe na Coluna FIPE do execel.
        df['FIPE'][index] = elemento_valor_fipe


    #Cria o novo execel com os valores que estão sendo pesquisado
    df.to_excel(f"{inter.nome_arquivo}.xlsx", index=False)

   
    time.sleep(4)


def carros(df,index,row):
#Lendo o Execel e entrando na pagina da FIPE.
    #chrome.refresh() 

    print("index: " + str(index) + " o nome é " + row ["CONTRATO"])

    clicar('//*[@id="front"]/div[1]/div[3]/a/figure/img')

    #Rolando o site para cima 1 vez.
    chrome.execute_script("window.scrollTo(6, document.body.scrollHeight);")

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

    Lista_correcao_diesel = ['(diesel)','(DIESEL)',
        ' Diesel',' DIESEL','(die)',' Dies']
        
    correto_nome = (row["MODELO"])

    for diesel in Lista_correcao_diesel:
            if diesel in correto_nome:
                #Selecionando Ano e Diesel
                chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]').click() #Selecione Ano.
                elemento_ano = chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]/div/div/input')
                elemento_ano_correto = (row["ANO"]).split('/')[1]
                elemento_ano.send_keys(elemento_ano_correto +' Diesel')
                elemento_ano.send_keys(Keys.ENTER)
                break


            else:
                #Selecionando Ano e Gasolina
                elemento_selecione_ano = chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]').click()     
                elemento_ano = chrome.find_element(By.XPATH,'//*[@id="selectAnocarro_chosen"]/div/div/input')
                elemento_ano_correto = (row["ANO"]).split('/')[1]
                elemento_ano.send_keys(elemento_ano_correto +' Gasolina')
                elemento_ano.send_keys(Keys.ENTER)
                break




    #Selecionando Modelo 
    clicar('//*[@id="selectAnoModelocarro_chosen"]')
    
    elemento_modelo = chrome.find_element(By.XPATH,'//*[@id="selectAnoModelocarro_chosen"]/div/div/input')
     

    #Correção de  portas 
    #Pratica errada de programação Quebra galho.
    listagem = ['- 0P -  -  ','- 0P -  - ','- 5P - Básico - ','- 2P - Básico - ','- 4P - Básico - ',
    '- 3P - Básico -','- 0P - Básico - ','- 0p - - ']



    for item in listagem:
        if item in correto_nome:
            correto_nome = correto_nome.replace(item,"")
            break
    print(correto_nome)
    elemento_modelo.send_keys(correto_nome)

    
    elemento_modelo.send_keys(Keys.ENTER)

        
    time.sleep(2)
    
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
        pd.options.mode.chained_assignment = None
        df['FIPE'][index] = elemento_valor_fipe
        
    #Cria o novo execel com os valores que estão sendo pesquisado
    df.to_excel(f"{inter.nome_arquivo}.xlsx", index=False)


def leitura(filepath):

    df = pd.read_excel(filepath)
    tamanho = df.index.stop
    for index,row in df.iterrows():

        Tipo = row ["CONTRATO"] #Exp : 44-519190/20
        time.sleep(3)
        try:
            print(Tipo)
            Tipo2 = Tipo.split('-')[0]
            Tipo3 = int(Tipo2)

            ListaC = [40,41,42,43,44,45,46,47,48,49]

            if Tipo3 in ListaC:
                print('#'*40)
                print(Tipo3)
                print('Ativou pesquisa caminhão')
                chrome.refresh()
                caminhoes(df,index,row)
                print('#'*40)
                

            else:
                print('#'*40)
                print(Tipo3)
                chrome.refresh()
                print('Ativou pesquisa carros')
                carros(df,index,row)
                print('#'*40)

            #start(df)
            
        except:
            print('Não foi possivel pequisar esse contrato.')
            df['FIPE'][index]= 'Não foi possivel pesquisar '
        
        finally:
            aumento = 100/tamanho
            inter.progresso(aumento)
            

def OpenFile():
    global filepath
    filepath = filedialog.askopenfilename()
    local_arquivo = Label(text=filepath ,font=("Arial",8))
    local_arquivo.place(x=30,y=77)
    
   

def stop():
    chrome.quit()
    quit()


# =================== ABA 2 ==================== FUNÇÕES ====================#


def pega_debitos(df,index,row):

        url_do_forms = "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx"

        print("index: " + str(index) + " o nome é " + row ["CONTRATO"])
        
        time.sleep(2)

        elemento_renavam = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtRenavam"]')
        elemento_placa = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtPlaca"]')
        
        elemento_renavam.clear()
        elemento_placa.clear()

        elemento_renavam.send_keys(row["RENAVAM"])
        elemento_placa.send_keys(row["PLACA"])

        time.sleep(2)

        chave_captcha = chrome.find_element(By.ID,'conteudoPaginaPlaceHolder_g_recaptcha').get_attribute('data-sitekey')

        solver = recaptchaV2Proxyless()
        solver.set_verbose(1)
        solver.set_key("03d6ce05e61a048fd4de08b3c7d68fdc")
        solver.set_website_url(url_do_forms)
        solver.set_website_key(chave_captcha)

        resposta = solver.solve_and_return_solution()

        if resposta != 0:
            print(resposta)
            chrome.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
            
        else:
            print(solver.err_string)

        time.sleep(10)

        chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_btn_Consultar"]').click()

        time.sleep(2)

        chrome.execute_script("window.scrollBy(0,1000)")

        elemento_debito = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtExisteDividaAtiva"]' ).text #Pesquisa débitos inscritos em dívida ativa 
        print(elemento_debito)
        df['DEBITOS'][index] = elemento_debito 

        time.sleep(5)

        chrome.execute_script("window.scrollBy(0,500)")

        elemento_total_debitos = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_Panel1"]/table[32]/tbody/tr/td[3]').text #Pesquisa de débitos totais. 
        print(elemento_total_debitos)
        df['DEBITOS TOTAIS'][index] = elemento_total_debitos

        df.to_excel(f"{inter.nome_arquivo2}.xlsx", index=False)

        time.sleep(2)

        chrome.back()

def iniciar2():
    
    url_do_forms = "https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    global chrome
    chrome = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options) 
    chrome.get(url_do_forms)
    leitura2(filepath)

def leitura2(filepath):

    df = pd.read_excel(filepath)

    for index,row in df.iterrows():
        pega_debitos(df,index,row)
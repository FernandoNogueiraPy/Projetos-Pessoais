#Documento de Falencia - Certidão

from tkinter.tix import Select
import pandas as pd
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import sqlalchemy

sqlalchemy.__version__
'1.4.41'

#Conexão ao Banco de dados
engine = sqlalchemy.create_engine('sqlite:///Doc.Projeto.db', echo =True)

from sqlalchemy.orm import declarative_base 
from sqlalchemy import Column , Integer , String
Base = declarative_base()

class User(Base): 
    __tablename__ = 'users'
    id = Column (Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    age = Column(Integer)

#Criar a tabela no banco de dados
Base.metadata.create_all(engine)
#Repassar valores de tabela para programa 
user = User (name='Fernando', fullname='Fernando Nogueira',age=20)

#Selecionar se é pessoa física ou jurídica
escolha = int(input("digite 1 para pessoa juridica e 0 para pessoa fisica"))
#Acessa o site do TJ.
a = 0
navegador = webdriver.Chrome()
navegador.get('https://esaj.tjsp.jus.br/sco/abrirCadastro.do')
time.sleep(3)
#Selecionar o tipo de emissão de certidão 
pyautogui.press(['down'])

a = 0
if escolha == 0:

    #Se a escolha for Pessoa Fisica 
    navegador.find_element(By.ID,"tpPessoaF").click() 
    #Preencher nome completo
    navegador.find_element(By.ID,"nmCadastroF").send_keys('Fernando Nogueira')
    #Preencher CPF 
    navegador.find_element(By.ID,"identity.nuCpfFormatado").send_keys('11111111111')
    #Preencher RG
    navegador.find_element(By.ID,"identity.nuRgFormatado").send_keys('58.952.589-7') 
    #Selecionar se é masculino ou feminino 
    navegador.find_element(By.ID,"flGeneroM").click() 
    #Preencher Email 
    navegador.find_element(By.ID,"identity.solicitante.deEmail").send_keys('fernandomoltt101@gmail.com') 
    #Clikar em confirmação 
    navegador.find_element(By.ID,"confirmacaoInformacoes").click()
    #Clikar em Enviar
    navegador.find_element(By.ID,"pbEnviar").click()

elif escolha == 1:
    #Se a escolha for pessoa Jurídica
    navegador.find_element(By.ID,"tpPessoaJ").click()
    #Preencher razão social da Empresa
    navegador.find_element(By.ID,"nmCadastroJ").send_keys('Moltt Tecnologia Ltda')
    #Preencher CNPJ
    navegador.find_element(By.ID,"identity.nuCnpjFormatado").send_keys('56.565.666/5555-5')
    #Preencher Email 
    navegador.find_element(By.ID,"identity.solicitante.deEmail").send_keys('fernandomoltt101@gmail.com') 
    #Clikar em confirmação 
    navegador.find_element(By.ID,"confirmacaoInformacoes").click()
    #Clikar em Enviar
    navegador.find_element(By.ID,"pbEnviar").click()





a = 0
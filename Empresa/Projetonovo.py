#https://veiculos.fipe.org.br/api/veiculos//ConsultarValorComTodosParametros

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(ChromeDriverManager().install())



def Iniciar():
    url_do_forms = "https://veiculos.fipe.org.br/#carro-comum"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    chrome.get(url_do_forms)

Iniciar()
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless

from replaces import altera_placa
from logs import save_logs


#Arquivo a ser lido.
df = pd.read_excel(r"TratamentoErros.xlsx")

def dividir_lista(lista: list, quantidade: int):
    """Dividir uma lista em várias sublistas de tamanho igual ou próximo.
    
    Args:
        lista (list): Lista a ser dividida.
        quantidade (int): Tamanho das sublistas.
    
    Returns:
        list: Lista de sublistas.
    """
    nova_lista = []
    for index in range(0, len(lista), quantidade):
        nova_lista.append(lista[index:index+quantidade])
    return nova_lista


def pega_debitos(lista):
    """Pegar os débitos de uma lista de veículos.
    
    Args:
        lista (list): Lista de dicionários com os dados dos veículos.
    """
    # Configurações do navegador
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')

    with webdriver.Chrome(ChromeDriverManager().install(), options=options) as chrome:
        # Abrir a página do formulário
        chrome.get("https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx")
        
        # Converter a lista em um dataframe do Pandas
        dataframe = pd.DataFrame(lista)

        # Iterar sobre cada linha do dataframe
        for index, row in dataframe.iterrows():
            print(f"Processando veículo {row['CONTRATO']} (índice {index})")
            
            renavam = row["RENAVAM"]
            placa = row["PLACA"]

            for i in range(2):  # Tentar duas vezes
                try:
                    # Identificar os elementos do formulário
                    elemento_renavam = chrome.find_element(By.XPATH, '//*[@id="conteudoPaginaPlaceHolder_txtRenavam"]')
                    elemento_placa = chrome.find_element(By.XPATH, '//*[@id="conteudoPaginaPlaceHolder_txtPlaca"]')

                    # Limpar os elementos e preencher com os valores da linha atual
                    elemento_renavam.clear()
                    elemento_placa.clear()
                    elemento_renavam.send_keys(renavam)
                    elemento_placa.send_keys(placa)

                    time.sleep(2)

                    # Iniciar o QuebraCpatcha
                    chave_captcha = chrome.find_element(By.ID, 'conteudoPaginaPlaceHolder_g_recaptcha').get_attribute('data-sitekey')

                    solver = recaptchaV2Proxyless()
                    solver.set_verbose(1)
                    solver.set_key("03d6ce05e61a048fd4de08b3c7d68fdc")
                    solver.set_website_url("https://www.ipva.fazenda.sp.gov.br/IPVANET_Consulta/Consulta.aspx")
                    solver.set_website_key(chave_captcha)

                    resposta = solver.solve_and_return_solution()

                    if resposta != 0:
                        print(resposta)
                        chrome.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
                    else:
                        print(solver.err_string)

                    time.sleep(2)

                    # Clickar no botão de consulta
                    chrome.find_element(By.XPATH, '//*[@id="conteudoPaginaPlaceHolder_btn_Consultar"]').click()

                    time.sleep(2)

                    # Scroll para baixo em 1000 pixels
                    chrome.execute_script("window.scrollBy(0,1000)")

                    # Capturar o elemento dos débitos
                    elemento_debitos = chrome.find_element(By.XPATH, '//*[@id="conteudoPaginaPlaceHolder_lbl_Debitos"]')
                    debitos = elemento_debitos.text
                    row["DEBITOS"] = debitos

                    time.sleep(2)
                    
                    # Salvar o log
                    save_logs(row)
                    break  # Parar o loop se a consulta foi bem sucedida
                except Exception as e:
                    print(f"Erro na consulta: {e}")
                    time.sleep(5)  # Esperar antes de tentar novamente

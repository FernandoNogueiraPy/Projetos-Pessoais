from selenium import webdriver
import threading


def separar_lista(lista: list, quantidade: int):
    new_list = []
    for index in range(0, len(lista), quantidade):
        new_list.append(lista[index:index+quantidade])
    return new_list


df = pd.read_excel(r"F:\Users\Moltt\Documents\python\Empresa\projeto_com_api\TratamentoErros.xlsx")

numero_raw = len(df)  #/4 < Número que deve ser trocado para divisão < 

lista_separada = separar_lista(df,int(numero_raw))

def pega_debitos(lista):

    
    dataframe = pd.DataFrame(lista)

    for index,row in dataframe.iterrows():
        print("index: " + str(index) + " o nome é " + row ["CONTRATO"])
        
        time.sleep(2)

        
        renavam = row["RENAVAM"]
        placa = row["PLACA"]

        for i in range(0,2):
            try:

                #Identifica os elementos onde serão inseridos a placa e o renavam
                elemento_renavam = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtRenavam"]')
                elemento_placa = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtPlaca"]')
                elemento_renavam.clear()
                elemento_placa.clear()
                elemento_renavam.send_keys(renavam)
                elemento_placa.send_keys(placa)

                time.sleep(2)


                #Inicia o QuebraCpatcha.
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

                time.sleep(2)


                #Clicka na consulta.
                chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_btn_Consultar"]').click()

                time.sleep(2)


                #Scrol para baixo 1000 Pixel
                chrome.execute_script("window.scrollBy(0,1000)")

                #Captura o elemento e atribui ele a coluna de [DEBITOS]
                elemento_debito = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_txtExisteDividaAtiva"]' ).text #Pesquisa débitos inscritos em dívida ativa 
                print(elemento_debito)
                df['DEBITOS'][index] = elemento_debito 

                time.sleep(5)

                #Scrol para baixo 500 Pixel
                chrome.execute_script("window.scrollBy(0,500)")

                #Captura o elemento e atribui ele a coluna de [DEBITOS TOTAIS]
                elemento_total_debitos = chrome.find_element(By.XPATH,'//*[@id="conteudoPaginaPlaceHolder_Panel1"]/table[32]/tbody/tr/td[3]').text #Pesquisa de débitos totais. 
                print(elemento_total_debitos)
                df['DEBITOS TOTAIS'][index] = elemento_total_debitos


                #Cria o novo arquivo excel com os valores pesquisados. 
                df.to_excel('Tabela_Fipe_Valores_testando_abas.xlsx', index=False)

                time.sleep(2)

                chrome.back()
            except Exception as error:
                if i != 1:
                    placa = altera_placa(placa) # add trocar letra por numero
                else:
                    df['DEBITOS'][index] = "Não foi possivel localizar"
                    save_logs(f"log - {placa} {error}")
                continue
            else:
                break

# Função que será executada em cada thread
def search_keyword(driver, keyword):
  # Altere para a aba atual
  driver.switch_to.window(driver.current_window_handle)
  
  
# Abra o Chrome e crie dez novas abas
driver = webdriver.Chrome()
for i in range(10):
  driver.execute_script("window.open('https://www.google.com', '_blank');")

# Obtenha a lista de todas as abas abertas
handles = driver.window_handles

# Crie uma thread para cada aba
threads = []
for i, handle in enumerate(handles):
  keyword = "thread {}".format(i+1)
  t = threading.Thread(target=search_keyword, args=(driver, keyword))
  threads.append(t)

# Inicie todas as threads
for t in threads:
  t.start()

# Espere todas as threads terminarem
for t in threads:
  t.join()

# Feche o navegador
driver.quit()

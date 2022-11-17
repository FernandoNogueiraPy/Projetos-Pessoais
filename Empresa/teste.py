correto_nome = input('Nome')
print(correto_nome)
    

listagem = ['- 0P -  - ','- 5P - Básico - ','- 2P - Básico - ','- 4P - Básico - ',
    '- 3P - Básico -','- 0P - Básico - ','- 0p - - ']
    
for item in listagem:
    if item in correto_nome:
            nome_novo = correto_nome.replace(item,'')
            
print(nome_novo)
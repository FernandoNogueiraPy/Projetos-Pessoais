
lista_nomes = []
lista_sexo = []
lista_idade = []

for i in range(2):
    pergunta_nome = input('Qual seu nome ? ').strip()
    pergunta_sexo =  input('Seu sexo é ? Masculino / Feminino').strip()
    pergunta_idade = int(input('Qual sua Idade ?'))



    lista_nomes.append(pergunta_nome)
    lista_sexo.append(pergunta_sexo) 
    lista_idade.append(pergunta_idade)

    print(lista_nomes,lista_sexo,lista_idade)

soma_nome = sum(lista_nomes)
soma = sum(lista_idade)
media_idade = soma / lista_nomes 

print('A média de Idade é ',media_idade)
    
    

        
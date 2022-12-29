import pandas as pd
import random
import os
from time import sleep



def limpeza():
    os.system('cls')
    
    

def pega_palavra(nivel):
    dados = pd.read_csv("Palavras.csv", sep=";")

    x = random.randint(1,20)
    lin_i = 0
    ll=1
    for i in dados["Nivel"]:
        if i == nivel and lin_i == 0:
            lin_i = ll
        ll += 1
    x = lin_i+x
    if nivel == 1:
        li =[]
        li.append(dados.iat[x,2])
        li.append(dados.iat[x,3])
        return li
    else:
        return dados.iat[x,2]
#bonequinhos do jogo fácil


def chances_jogofacil (chances):
    def chance1 ():
        print('______')
        print('|    |')
        print('|   ')
        print('|  ')
        print('|_')

    def chance2 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|   ')
        print('|  ')
        print('|_')

    def chance3 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|    |')
        print('|  ')
        print('|_')

    def chance4 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|    |')
        print('|   /')
        print('|_')

    def chance5 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|    |')
        print('|   /\\')
        print('|_')

    def chance6 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|   <|')
        print('|   /\\')
        print('|_')

    def chance7 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|   <|>')
        print('|   /\\')
        print('|_')

    def chance8 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|   <|>')
        print('|  _/\\')
        print('|_')

    def chance9 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|   <|>')
        print('|  _/\\_')
        print('|_')

    def chance10 ():
        print('______')
        print('|   _|_\n|  (._.)')
        print('|   <|>')
        print('|  _/\\_')
        print('|_')

    def chance11 ():
        print('______')
        print('|   _|_\n|  (x_x)')
        print('|   <|>')
        print('|  _/\\_')
        print('|_')

    if chances == 10:
        chance1()
    if chances == 9:
        chance2()
    if chances == 8:
        chance3()
    if chances == 7:
        chance4()
    if chances == 6:
        chance5()
    if chances == 5:
        chance6()
    if chances == 4:
        chance7()
    if chances == 3:
        chance8()
    if chances == 2:
        chance9()
    if chances == 1:
        chance10()
    if chances == 0:
        chance11()
#bonequinhos do jogo médio
def chances_jogomedio (chances):
    def chance1 ():
        print('______')
        print('|    |')
        print('|   ')
        print('|  ')
        print('|_')

    def chance2 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|    |')
        print('|  ')
        print('|_')

    def chance3 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|    |')
        print('|   /\\')
        print('|_')

    def chance4 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|   <|>')
        print('|   /\\')
        print('|_')

    def chance5 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|   <|>')
        print('|  _/\\_')
        print('|_')

    def chance6 ():
        print('______')
        print('|   _|_\n|  (x_x)')
        print('|   <|>')
        print('|  _/\\_')
        print('|_')

    if chances == 5:
        chance1()
    if chances == 4:
        chance2()
    if chances == 3:
        chance3()
    if chances == 2:
        chance4()
    if chances == 1:
        chance5()
    if chances == 0:
        chance6()
def chances_jogodificil (chances):
    def chance1 ():
        print('______')
        print('|    |')
        print('|   ')
        print('|  ')
        print('|_')

    def chance2 ():
        print('______')
        print('|   _|_\n|  (   )')
        print('|   <|>')
        print('|  _/\\_')
        print('|_')

    def chance3 ():
        print('______')
        print('|   _|_\n|  (x_x)')
        print('|   <|>')
        print('|  _/\\_')
        print('|_')

    if chances == 2:
        chance1()
    if chances == 1:
        chance2()
    if chances == 0:
        chance3()

#input para testes
#palavra = input('Insira uma palavra para o jogador advinhar: ')
def modo_facil_iniciado():
    print("iniciou o facil\n\n\n\n\n\n")
    palav = pega_palavra(1)
    caracteres = list(palav[0]) #nivel 1 é facil
    palavra_esc = palav[0]
    dica_tx = palav[1]

    cont = 0

    troca = 0
    lista_troca = []

    for elemento in caracteres:
        if elemento == ' ':
            troca = cont
            caracteres.pop(troca)
            lista_troca.append(troca)

        cont +=1

    cont_caracteres = len(caracteres)

    espacos_letras = '_' * cont_caracteres

    lista_espacos_letras = list(espacos_letras)

    elemento = -1
    cont = 1

    if len(lista_troca) != 0:
        if len(lista_troca) == 1:
            for i in lista_troca:
                lista_espacos_letras.insert(i, ' ')
        elif len(lista_troca) > 1:
            while cont <= len(lista_troca):
                i = lista_troca[elemento]

                lista_espacos_letras.insert(i, ' ')

                elemento -= 1
                cont += 1

    espacos_letras = ''.join(map(str, lista_espacos_letras))

    espacos_letras = espacos_letras.replace(' ', '  ')
    espacos_letras = espacos_letras.replace('_', '_ ')

    print(espacos_letras)

    #espaco do jogo com o usuário com apenas uma palavra (independentemente do tamanho)
    letra_usuario = input('Digite uma letra: ')

    if len(letra_usuario) > 1: #mensagem de erro para controle de caracteres
        while len(letra_usuario) > 1:
            print('Insira apenas uma letra de cada vez!')
            letra_usuario = input('Digite uma letra: ')

    #mensagem de erro para números
    if letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
        while letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
            print('Insira apenas letras!')
            letra_usuario = input('Digite uma letra: ')

    lista_letras_usuario = []

    letra_usuario_aparece = caracteres.count(letra_usuario)

    if letra_usuario_aparece > 0: #caso o usuário acerte a primeira letra digitada
        lista_letras_usuario.append(letra_usuario)

        espacos_letras = list(espacos_letras)

        dica = 2
        letras_iguais = []
        cont_letras = 0

        for elemento in caracteres:
            if elemento.lower == letra_usuario.lower:
                letras_iguais.append(cont_letras)

                cont_letras += 1

            else:
                cont_letras += 1

        for indice in letras_iguais:
            if indice == 0:
                espacos_letras.pop(indice)
                espacos_letras.insert(indice, letra_usuario)

            else:
                espacos_letras.pop(indice * 2)
                espacos_letras.insert(indice * 2, letra_usuario)

        espacos_letras = ''.join(map(str, espacos_letras))

        print('______')
        print('|    |')
        print('|   ')
        print('|  ')
        print('|_')
        print('\n', espacos_letras)
        print('\nHistórico de letras digitadas:', lista_letras_usuario)

        chances = 10

        print('Você tem {} chances restantes.'.format(chances))

        while chances >= 0:
            letra_usuario = input("Digite uma letra:(Digite '.' para pedir uma dica) ")

            if len(letra_usuario) > 1: #mensagem de erro para controle de caracteres
                while len(letra_usuario) > 1:
                    print('Insira apenas uma letra de cada vez!')
                    letra_usuario = input('Digite uma letra: ')

            #mensagem de erro para números
            if letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                while letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                    print('Insira apenas letras!')
                    letra_usuario = input('Digite uma letra: ')

            if letra_usuario == '.' and dica >= 1: #se o usuário quiser usar a dica

                print(f"\n{dica_tx}\n")

                espacos_letras = list(espacos_letras)

                contagem_dica = espacos_letras.count('_')
                posicao_dica = espacos_letras.index('_')

                if contagem_dica > 1:
                    if posicao_dica == 0:
                        espacos_letras.pop(0)
                        espacos_letras.insert(0, caracteres[0])

                        espacos_letras = ''.join(map(str, espacos_letras))

                        chances_jogofacil(chances)
                        print('\n', espacos_letras)
                        print('\nHistórico de letras digitadas:', lista_letras_usuario)
                        print('Você tem {} chances restantes.'.format(chances))

                    else:
                        espacos_letras.pop(posicao_dica)
                        espacos_letras.insert(posicao_dica, caracteres[posicao_dica // 2])

                        espacos_letras = ''.join(map(str, espacos_letras))

                        chances_jogofacil(chances)
                        print('\n', espacos_letras)
                        print('\nHistórico de letras digitadas:', lista_letras_usuario)
                        print('Você tem {} chances restantes.'.format(chances))

                else: #se restar apenas uma letra, o usuário não poderá usar dicas
                    print('Resta apenas uma letra para advinhar, não é possível usar dicas!')

                dica -= 1

                continue

            elif letra_usuario == '.' and dica == 0: #nível médio possui apenas uma dica, se ela já tiver sido gasta
                print('Suas dicas esgotaram!')

                continue

            lista_letras_usuario.append(letra_usuario)

            letra_usuario_aparece = caracteres.count(letra_usuario)

            if letra_usuario_aparece > 0:
                espacos_letras = list(espacos_letras)

                letras_iguais = []
                cont_letras = 0

                for elemento in caracteres:
                    if elemento.lower == letra_usuario.lower:
                        letras_iguais.append(cont_letras)

                        cont_letras += 1

                    else:
                        cont_letras += 1

                for indice in letras_iguais:
                    if indice == 0:
                        espacos_letras.pop(indice)
                        espacos_letras.insert(indice, letra_usuario)

                    else:
                        espacos_letras.pop(indice * 2)
                        espacos_letras.insert(indice * 2, letra_usuario)

                espacos_letras = ''.join(map(str, espacos_letras))

                chances_jogofacil(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))

                espacos_letras_faltando = espacos_letras.count('_')

                if espacos_letras_faltando == 0:
                    print('Parabéns, você advinhou a palavra!\n\nVocê foi para o proximo nível!')
                    break

            else:
                chances -= 1

                chances_jogofacil(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))
                print('\nVocê errou!')

                if chances == 0:
                    print('Suas chances acabaram. Jogo encerrado!')
                    break

    else: #caso o usuário erre a primeira letra digitada
        lista_letras_usuario.append(letra_usuario)

        print('______')
        print('|   _|_\n|  (   )')
        print('|    ')
        print('|  ')
        print('|_')
        print('\n', espacos_letras)
        print('\n Você errou!')
        print('\nHistórico de letras digitadas:', lista_letras_usuario)

        dica = 2
        chances = 9

        print('Você tem {} chances restantes.'.format(chances))

        while chances >= 0:
            letra_usuario = input("Digite uma letra:(Digite '.' para pedir uma dica) ")

            if len(letra_usuario) > 1: #mensagem de erro para controle de caracteres
                while len(letra_usuario) > 1:
                    print('Insira apenas uma letra de cada vez!')
                    letra_usuario = input('Digite uma letra: ')

            #mensagem de erro para números
            if letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                while letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                    print('Insira apenas letras!')
                    letra_usuario = input('Digite uma letra: ')

            if letra_usuario == '.' and dica >= 1: #se o usuário quiser usar a dica
                print(f"\n{dica_tx}\n")

                espacos_letras = list(espacos_letras)
                contagem_dica = espacos_letras.count('_')
                posicao_dica = espacos_letras.index('_')

                if contagem_dica > 1:
                    if posicao_dica == 0:
                        espacos_letras.pop(0)
                        espacos_letras.insert(0, caracteres[0])

                        espacos_letras = ''.join(map(str, espacos_letras))

                        chances_jogofacil(chances)
                        print('\n', espacos_letras)
                        print('\nHistórico de letras digitadas:', lista_letras_usuario)
                        print('Você tem {} chances restantes.'.format(chances))

                    else:
                        espacos_letras.pop(posicao_dica)
                        espacos_letras.insert(posicao_dica, caracteres[posicao_dica // 2])

                        espacos_letras = ''.join(map(str, espacos_letras))

                        chances_jogofacil(chances)
                        print('\n', espacos_letras)
                        print('\nHistórico de letras digitadas:', lista_letras_usuario)
                        print('Você tem {} chances restantes.'.format(chances))

                else: #se restar apenas uma letra, o usuário não poderá usar dicas
                    print('Resta apenas uma letra para advinhar, não é possível usar dicas!')


                dica -= 1

                continue

            elif letra_usuario == '.' and dica == 0: #nível médio possui apenas uma dica, se ela já tiver sido gasta
                print('Suas dicas esgotaram!')

                continue

            lista_letras_usuario.append(letra_usuario)

            letra_usuario_aparece = caracteres.count(letra_usuario)

            if letra_usuario_aparece > 0:
                espacos_letras = list(espacos_letras)

                letras_iguais = []
                cont_letras = 0

                for elemento in caracteres:
                    if elemento.lower == letra_usuario.lower:
                        letras_iguais.append(cont_letras)

                        cont_letras += 1

                    else:
                        cont_letras += 1

                for indice in letras_iguais:
                    if indice == 0:
                        espacos_letras.pop(indice)
                        espacos_letras.insert(indice, letra_usuario)

                    else:
                        espacos_letras.pop(indice * 2)
                        espacos_letras.insert(indice * 2, letra_usuario)

                espacos_letras = ''.join(map(str, espacos_letras))

                chances_jogofacil(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))

                espacos_letras_faltando = espacos_letras.count('_')

                if espacos_letras_faltando == 0:
                    print('Parabéns, você advinhou a palavra!')
                    break

            else:
                chances -= 1

                chances_jogofacil(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))
                print('\nVocê errou!')

                if chances == 0:
                    chances_jogofacil(chances)
                    print('\nSuas chances acabaram. Jogo encerrado!')
                    print(f"\nA palavra era {palavra_esc}!")
                    break






#input para testes
#palavra = input('Insira uma palavra para o jogador advinhar: ')
def modo_medio_iniciado():
    print("iniciou o médio\n\n\n\n\n\n")
    caracteres = list(pega_palavra(2)) #nivel 2 é Médio
    palavra_esc = caracteres
    cont = 0

    troca = 0
    lista_troca = []

    for elemento in caracteres:
        if elemento == ' ':
            troca = cont
            caracteres.pop(troca)
            lista_troca.append(troca)

        cont +=1

    cont_caracteres = len(caracteres)

    espacos_letras = '_' * cont_caracteres

    lista_espacos_letras = list(espacos_letras)

    elemento = -1
    cont = 1

    if len(lista_troca) != 0:
        if len(lista_troca) == 1:
            for i in lista_troca:
                lista_espacos_letras.insert(i, ' ')
        elif len(lista_troca) > 1:
            while cont <= len(lista_troca):
                i = lista_troca[elemento]

                lista_espacos_letras.insert(i, ' ')

                elemento -= 1
                cont += 1

    espacos_letras = ''.join(map(str, lista_espacos_letras))

    espacos_letras = espacos_letras.replace(' ', '  ')
    espacos_letras = espacos_letras.replace('_', '_ ')

    print(espacos_letras)

    #espaco do jogo com o usuário com apenas uma palavra (independentemente do tamanho)
    letra_usuario = input('Digite uma letra: ')

    if len(letra_usuario) > 1: #mensagem de erro para controle de caracteres
        while len(letra_usuario) > 1:
            print('Insira apenas uma letra de cada vez!')
            letra_usuario = input('Digite uma letra: ')

    #mensagem de erro para números
    if letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
        while letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
            print('Insira apenas letras!')
            letra_usuario = input('Digite uma letra: ')

    lista_letras_usuario = []

    letra_usuario_aparece = caracteres.count(letra_usuario)

    if letra_usuario_aparece > 0: #caso o usuário acerte a primeira letra digitada
        lista_letras_usuario.append(letra_usuario)

        espacos_letras = list(espacos_letras)

        dica = 1
        letras_iguais = []
        cont_letras = 0

        for elemento in caracteres:
            if elemento.lower == letra_usuario.lower:
                letras_iguais.append(cont_letras)

                cont_letras += 1

            else:
                cont_letras += 1

        for indice in letras_iguais:
            if indice == 0:
                espacos_letras.pop(indice)
                espacos_letras.insert(indice, letra_usuario)

            else:
                espacos_letras.pop(indice * 2)
                espacos_letras.insert(indice * 2, letra_usuario)

        espacos_letras = ''.join(map(str, espacos_letras))

        print('______')
        print('|    |')
        print('|   ')
        print('|  ')
        print('|_')
        print('\n', espacos_letras)
        print('\nHistórico de letras digitadas:', lista_letras_usuario)

        dica = 1
        chances = 5

        print('Você tem {} chances restantes.'.format(chances))

        while chances >= 0:
            letra_usuario = input("Digite uma letra:(Digite '.' para pedir uma dica) ")

            if len(letra_usuario) > 1: #mensagem de erro para controle de caracteres
                while len(letra_usuario) > 1:
                    print('Insira apenas uma letra de cada vez!')
                    letra_usuario = input('Digite uma letra: ')

            #mensagem de erro para números
            if letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                while letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                    print('Insira apenas letras!')
                    letra_usuario = input('Digite uma letra: ')

            if letra_usuario == '.' and dica == 1: #se o usuário quiser usar a dica
                espacos_letras = list(espacos_letras)

                contagem_dica = espacos_letras.count('_')
                posicao_dica = espacos_letras.index('_')

                if contagem_dica > 1:
                    if posicao_dica == 0:
                        espacos_letras.pop(0)
                        espacos_letras.insert(0, caracteres[0])

                        espacos_letras = ''.join(map(str, espacos_letras))

                        chances_jogomedio(chances)
                        print('\n', espacos_letras)
                        print('\nHistórico de letras digitadas:', lista_letras_usuario)
                        print('Você tem {} chances restantes.'.format(chances))

                    else:
                        espacos_letras.pop(posicao_dica)
                        espacos_letras.insert(posicao_dica, caracteres[posicao_dica // 2])

                        espacos_letras = ''.join(map(str, espacos_letras))

                        chances_jogomedio(chances)
                        print('\n', espacos_letras)
                        print('\nHistórico de letras digitadas:', lista_letras_usuario)
                        print('Você tem {} chances restantes.'.format(chances))

                else: #se restar apenas uma letra, o usuário não poderá usar dicas
                    print('Resta apenas uma letra para advinhar, não é possível usar dicas!')

                dica -= 1

                continue

            elif letra_usuario == '.' and dica == 0: #nível médio possui apenas uma dica, se ela já tiver sido gasta
                print('Suas dicas esgotaram!')

                continue

            lista_letras_usuario.append(letra_usuario)

            letra_usuario_aparece = caracteres.count(letra_usuario)

            if letra_usuario_aparece > 0:
                espacos_letras = list(espacos_letras)

                letras_iguais = []
                cont_letras = 0

                for elemento in caracteres:
                    if elemento.lower == letra_usuario.lower:
                        letras_iguais.append(cont_letras)

                        cont_letras += 1

                    else:
                        cont_letras += 1

                for indice in letras_iguais:
                    if indice == 0:
                        espacos_letras.pop(indice)
                        espacos_letras.insert(indice, letra_usuario)

                    else:
                        espacos_letras.pop(indice * 2)
                        espacos_letras.insert(indice * 2, letra_usuario)

                espacos_letras = ''.join(map(str, espacos_letras))

                chances_jogomedio(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))

                espacos_letras_faltando = espacos_letras.count('_')

                if espacos_letras_faltando == 0:
                    print('Parabéns, você advinhou a palavra!\n\nVocê foi para o proximo nível!')
                    break

            else:
                chances -= 1

                chances_jogomedio(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))
                print('\nVocê errou!')

                if chances == 0:
                    print('Suas chances acabaram. Jogo encerrado!')
                    print(f"\nA palavra era {palavra_esc}!")
                    break

    else: #caso o usuário erre a primeira letra digitada
        lista_letras_usuario.append(letra_usuario)

        print('______')
        print('|   _|_\n|  (   )')
        print('|    |')
        print('|  ')
        print('|_')
        print('\n', espacos_letras)
        print('\n Você errou!')
        print('\nHistórico de letras digitadas:', lista_letras_usuario)

        dica = 1
        chances = 4

        print('Você tem {} chances restantes.'.format(chances))

        while chances >= 0:
            letra_usuario = input("Digite uma letra:(Digite '.' para pedir uma dica) ")

            if len(letra_usuario) > 1: #mensagem de erro para controle de caracteres
                while len(letra_usuario) > 1:
                    print('Insira apenas uma letra de cada vez!')
                    letra_usuario = input('Digite uma letra: ')

            #mensagem de erro para números
            if letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                while letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                    print('Insira apenas letras!')
                    letra_usuario = input('Digite uma letra: ')

            if letra_usuario == '.' and dica == 1: #se o usuário quiser usar a dica
                espacos_letras = list(espacos_letras)

                contagem_dica = espacos_letras.count('_')
                posicao_dica = espacos_letras.index('_')

                if contagem_dica > 1:
                    if posicao_dica == 0:
                        espacos_letras.pop(0)
                        espacos_letras.insert(0, caracteres[0])

                        espacos_letras = ''.join(map(str, espacos_letras))

                        chances_jogomedio(chances)
                        print('\n', espacos_letras)
                        print('\nHistórico de letras digitadas:', lista_letras_usuario)
                        print('Você tem {} chances restantes.'.format(chances))

                    else:
                        espacos_letras.pop(posicao_dica)
                        espacos_letras.insert(posicao_dica, caracteres[posicao_dica // 2])

                        espacos_letras = ''.join(map(str, espacos_letras))

                        chances_jogomedio(chances)
                        print('\n', espacos_letras)
                        print('\nHistórico de letras digitadas:', lista_letras_usuario)
                        print('Você tem {} chances restantes.'.format(chances))

                else: #se restar apenas uma letra, o usuário não poderá usar dicas
                    print('Resta apenas uma letra para advinhar, não é possível usar dicas!')


                dica -= 1

                continue

            elif letra_usuario == '.' and dica == 0: #nível médio possui apenas uma dica, se ela já tiver sido gasta
                print('Suas dicas esgotaram!')

                continue

            lista_letras_usuario.append(letra_usuario)

            letra_usuario_aparece = caracteres.count(letra_usuario)

            if letra_usuario_aparece > 0:
                espacos_letras = list(espacos_letras)

                letras_iguais = []
                cont_letras = 0

                for elemento in caracteres:
                    if elemento.lower == letra_usuario.lower:
                        letras_iguais.append(cont_letras)

                        cont_letras += 1

                    else:
                        cont_letras += 1

                for indice in letras_iguais:
                    if indice == 0:
                        espacos_letras.pop(indice)
                        espacos_letras.insert(indice, letra_usuario)

                    else:
                        espacos_letras.pop(indice * 2)
                        espacos_letras.insert(indice * 2, letra_usuario)

                espacos_letras = ''.join(map(str, espacos_letras))

                chances_jogomedio(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))

                espacos_letras_faltando = espacos_letras.count('_')

                if espacos_letras_faltando == 0:
                    print('Parabéns, você advinhou a palavra!')
                    break

            else:
                chances -= 1

                chances_jogomedio(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))
                print('\nVocê errou!')

                if chances == 0:
                    chances_jogomedio(chances)
                    print('\nSuas chances acabaram. Jogo encerrado!')
                    break




#bonequinhos do jogo difícil
def modo_dificil_iniciado():
    #input para testes
    print("iniciou o Difil\n\n\n\n\n\n")
    #palavra = input('Insira uma palavra para o jogador advinhar: ')

    caracteres = list(pega_palavra(3)) #nivel 3 é deficil
    palavra_esc = caracteres
    cont = 0

    troca = 0
    lista_troca = []

    for elemento in caracteres:
        if elemento == ' ':
            troca = cont
            caracteres.pop(troca)
            lista_troca.append(troca)

        cont +=1

    cont_caracteres = len(caracteres)

    espacos_letras = '_' * cont_caracteres

    lista_espacos_letras = list(espacos_letras)

    elemento = -1
    cont = 1

    if len(lista_troca) != 0:
        if len(lista_troca) == 1:
            for i in lista_troca:
                lista_espacos_letras.insert(i, ' ')
        elif len(lista_troca) > 1:
            while cont <= len(lista_troca):
                i = lista_troca[elemento]

                lista_espacos_letras.insert(i, ' ')

                elemento -= 1
                cont += 1

    espacos_letras = ''.join(map(str, lista_espacos_letras))

    espacos_letras = espacos_letras.replace(' ', '  ')
    espacos_letras = espacos_letras.replace('_', '_ ')

    print(espacos_letras)

    #espaco do jogo com o usuário com apenas uma palavra (independentemente do tamanho)
    letra_usuario = input('Digite uma letra: ')

    if len(letra_usuario) > 1: #mensagem de erro para controle de caracteres
        while len(letra_usuario) > 1:
            print('Insira apenas uma letra de cada vez!')
            letra_usuario = input('Digite uma letra: ')

    #mensagem de erro para números
    if letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
        while letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
            print('Insira apenas letras!')
            letra_usuario = input('Digite uma letra: ')

    lista_letras_usuario = []

    letra_usuario_aparece = caracteres.count(letra_usuario)

    if letra_usuario_aparece > 0: #caso o usuário acerte a primeira letra digitada
        lista_letras_usuario.append(letra_usuario)

        espacos_letras = list(espacos_letras)

        letras_iguais = []
        cont_letras = 0

        for elemento in caracteres:
            if elemento.lower == letra_usuario.lower:
                letras_iguais.append(cont_letras)

                cont_letras += 1

            else:
                cont_letras += 1

        for indice in letras_iguais:
            if indice == 0:
                espacos_letras.pop(indice)
                espacos_letras.insert(indice, letra_usuario)

            else:
                espacos_letras.pop(indice * 2)
                espacos_letras.insert(indice * 2, letra_usuario)

        espacos_letras = ''.join(map(str, espacos_letras))

        print('______')
        print('|    |')
        print('|   ')
        print('|  ')
        print('|_')
        print('\n', espacos_letras)
        print('\nHistórico de letras digitadas:', lista_letras_usuario)

        chances = 2

        print('Você tem {} chances restantes.'.format(chances))

        while chances >= 0:
            letra_usuario = input('Digite uma letra: ')

            if len(letra_usuario) > 1: #mensagem de erro para controle de caracteres
                while len(letra_usuario) > 1:
                    print('Insira apenas uma letra de cada vez!')
                    letra_usuario = input('Digite uma letra: ')

            #mensagem de erro para números
            if letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                while letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                    print('Insira apenas letras!')
                    letra_usuario = input('Digite uma letra: ')

            lista_letras_usuario.append(letra_usuario)

            letra_usuario_aparece = caracteres.count(letra_usuario)

            if letra_usuario_aparece > 0:
                espacos_letras = list(espacos_letras)

                letras_iguais = []
                cont_letras = 0

                for elemento in caracteres:
                    if elemento.lower == letra_usuario.lower:
                        letras_iguais.append(cont_letras)

                        cont_letras += 1

                    else:
                        cont_letras += 1

                for indice in letras_iguais:
                    if indice == 0:
                        espacos_letras.pop(indice)
                        espacos_letras.insert(indice, letra_usuario)

                    else:
                        espacos_letras.pop(indice * 2)
                        espacos_letras.insert(indice * 2, letra_usuario)

                espacos_letras = ''.join(map(str, espacos_letras))

                chances_jogodificil(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))

                espacos_letras_faltando = espacos_letras.count('_')

                if espacos_letras_faltando == 0:
                    print('Parabéns, você advinhou a palavra!')
                    break

            else:
                chances -= 1

                chances_jogodificil(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))
                print('\nVocê errou!')

                if chances == 0:
                    print('Suas chances acabaram. Jogo encerrado!')
                    break

    else: #caso o usuário erre a primeira letra digitada
        lista_letras_usuario.append(letra_usuario)

        print('______')
        print('|   _|_\n|  (   )')
        print('|   <|>')
        print('|  _/\\_')
        print('|_')
        print('\n', espacos_letras)
        print('\n Você errou!')
        print('\nHistórico de letras digitadas:', lista_letras_usuario)

        chances = 1

        print('Você tem {} chances restantes.'.format(chances))

        while chances >= 0:
            letra_usuario = input('Digite uma letra: ')

            if len(letra_usuario) > 1: #mensagem de erro para controle de caracteres
                while len(letra_usuario) > 1:
                    print('Insira apenas uma letra de cada vez!')
                    letra_usuario = input('Digite uma letra: ')

            #mensagem de erro para números
            if letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                while letra_usuario == '0' and letra_usuario == '1' and letra_usuario == '2' and letra_usuario == '3' and letra_usuario == '4' and letra_usuario == '5' and letra_usuario == '6' and letra_usuario == '7' and letra_usuario == '8' and letra_usuario == '9':
                    print('Insira apenas letras!')
                    letra_usuario = input('Digite uma letra: ')

            lista_letras_usuario.append(letra_usuario)

            letra_usuario_aparece = caracteres.count(letra_usuario)

            if letra_usuario_aparece > 0:
                espacos_letras = list(espacos_letras)

                letras_iguais = []
                cont_letras = 0

                for elemento in caracteres:
                    if elemento.lower == letra_usuario.lower:
                        letras_iguais.append(cont_letras)

                        cont_letras += 1

                    else:
                        cont_letras += 1

                for indice in letras_iguais:
                    if indice == 0:
                        espacos_letras.pop(indice)
                        espacos_letras.insert(indice, letra_usuario)

                    else:
                        espacos_letras.pop(indice * 2)
                        espacos_letras.insert(indice * 2, letra_usuario)

                espacos_letras = ''.join(map(str, espacos_letras))

                chances_jogodificil(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))

                espacos_letras_faltando = espacos_letras.count('_')

                if espacos_letras_faltando == 0:
                    print('Parabéns, você advinhou a palavra!')
                    print(f"\nA palavra era {palavra_esc}!")
                    break

            else:
                chances -= 1

                chances_jogodificil(chances)
                print('\n', espacos_letras)
                print('\nHistórico de letras digitadas:', lista_letras_usuario)
                print('Você tem {} chances restantes.'.format(chances))
                print('\nVocê errou!')

                if chances == 0:
                    chances_jogodificil(chances)
                    print('\nSuas chances acabaram. Jogo encerrado!')
                    break
def menuiniciar1 (): #menu inicial do jogo
    limpeza()
    print('Digite: J- JOGAR | S- SAIR')

    print('\n\t\t╔═════════════╗')
    print(  '\t\t║╔═╦══╦══╦═╦═╗║')
    print(  '\t\t║║═╣╔╗║░░║╔╣║║║')
    print(  '\t\t║║╔╣╚╝║╔╗╣╚╣╩║║')
    print(  '\t\t║╚╝╚══╩╝╚╩═╩╩╝║')
    print(  '\t\t╚═════════════╝')

    print('\n\t\t   ╔╦═╦═╦═╦╦╗')
    print(  '\t\t  ╔╝║║║╔╣╩║╔╝ - Digite "J"')
    print(  '\t\t  ╚═╩═╩═╩╩╩╝')

    print('\t\t   ╔══╦═╦╦╦╗')
    print('\t\t   ╠╗╚╣╩║║╔╝ - Digite "S"')
    print('\t\t   ╚══╩╩╩╩╝')

def jogar1 ():
    limpeza()
    print('Digite: F- FÁCIL | M- MÉDIO | D- DIFÍCIL | X- MENU')

    print('\n\t\t╔══════════════╗')
    print(  '\t\t║╔═╦══╦══╦═╦══╗║')
    print(  '\t\t║╚╗║╔╗║╔═╣║║░░║║')
    print(  '\t\t║╔╣║╚╝║╚╝║╩║╔╗╣║')
    print(  '\t\t║╚═╩══╩══╩╩╩╝╚╝║')
    print(  '\t\t╚══════════════╝')

    print('\n\t\t   ╔═╦═╦═╦╦╗')
    print(  '\t\t   ║╔╣╩║╠╣║╚╗ - Digite "F"')
    print(  '\t\t   ╚╝╚╩╩═╩╩═╝')

    print('\t\t  ╔══╦═╦═╦╦═╗')
    print('\t\t  ║║║║╦╣╠║║║║ - Digite "M"')
    print('\t\t  ╚╩╩╩═╩═╩╩═╝')

    print('\t\t  ╔═╦╦═╦╦═╦╦╗')
    print('\t\t  ║╠║║╔╣║╠╣║╚╗ - Digite "D"')
    print('\t\t  ╚═╩╩╝╚╩═╩╩═╝')

    print('\t\t  ╔══╦═╦═╦╦╗╔╗')
    print('\t\t  ║║║║╦╣║║║╚╝║ - Digite "X"')
    print('\t\t  ╚╩╩╩═╩╩═╩══╝')

def painel_facil ():
    limpeza()
    print('Digite: I- INICIAR | V- VOLTAR')

    print('\n\t\t╔══════════╗')
    print(  '\t\t║╔═╦═╦═╦╦╗ ║')
    print(  '\t\t║║═╣║║╔╣║║ ║')
    print(  '\t\t║║╔╣╩║╚╣║╚╗║')
    print(  '\t\t║╚╝╚╩╩═╩╩═╝║')
    print(  '\t\t╚══════════╝')

    print('\n                ╔╦═╦╦╦═╦╦═╦╦╗')
    print(  '                ║║║║║║╠╣║╩║╔╝ - Digite "i"')
    print(  '                ╚╩╩═╩╩═╩╩╩╩╝')

    print('               ╔╦╦═╦╗╔══╦═╦╦╗')
    print('               ║║║║║╚╬╗╔╣╩║╔╝ - Digite "v"')
    print('               ╚═╩═╩═╝╚╝╚╩╩╝')

def painel_medio ():
    limpeza()
    print('Digite: I- INICIAR | V- VOLTAR')

    print('\n\t\t╔═════════════╗')
    print(  '\t\t║╔══╦═╦═╗╔╦══╗║')
    print(  '\t\t║║║║║═╣║╚╣║╔╗║║')
    print(  '\t\t║║║║║═╣║╔╣║╚╝║║')
    print(  '\t\t║╚╩╩╩═╩═╝╚╩══╝║')
    print(  '\t\t╚═════════════╝')

    print('\n\t\t ╔╦═╦╦╦═╦╦═╦╦╗')
    print(  '\t\t ║║║║║║╠╣║╩║╔╝ - Digite "i"')
    print(  '\t\t ╚╩╩═╩╩═╩╩╩╩╝')

    print('\t\t╔╦╦═╦╗╔══╦═╦╦╗')
    print('\t\t║║║║║╚╬╗╔╣╩║╔╝ - Digite "v"')
    print('\t\t╚═╩═╩═╝╚╝╚╩╩╝')

def painel_dificil ():
    limpeza()
    print('Digite: I- INICIAR | V- VOLTAR')
    print('\n\t\t╔═════════════╗')
    print(  '\t\t║╔═╦╦╦═╦╦═╦╦╗ ║')
    print(  '\t\t║║║╚╣║═╣║╔╣║║ ║')
    print(  '\t\t║║║╔╣║╔╣║╚╣║╚╗║')
    print(  '\t\t║╚═╝╚╩╝╚╩═╩╩═╝║')
    print(  '\t\t╚═════════════╝')

    print('\n\t\t ╔╦═╦╦╦═╦╦═╦╦╗')
    print(  '\t\t ║║║║║║╠╣║╩║╔╝ - Digite "i"')
    print(  '\t\t ╚╩╩═╩╩═╩╩╩╩╝')

    print('\t\t╔╦╦═╦╗╔══╦═╦╦╗')
    print('\t\t║║║║║╚╬╗╔╣╩║╔╝ - Digite "v"')
    print('\t\t╚═╩═╩═╝╚╝╚╩╩╝')

def painel_jogar ():
    limpeza()
    print('\n\t\t╔════════════════════════════════════════╗')
    print(      '║╔═╦═╦╦╗╔╦╦═╦╦╗╔╦═╦═╦═╦═╦═╦═╦╦╦═╦╗╔╦══╦═╗║')
    print(      '║║║║║╚╣╚╝║║║║║╚╝║═╣ ║║║ ║░║║║║║║║╚╝║░░║║║║')
    print(      '║║╩║║╔╩╗╔╣║║║║╔╗║═╣ ║╩║ ║╔╣╩║╚╣╩╠╗╔╣╔╗╣╩║║')
    print(      '║╚╩╩═╝ ╚╝╚╩╩═╩╝╚╩═╝ ╚╩╝ ╚╝╚╩╩═╩╩╝╚╝╚╝╚╩╩╝║')
    print(      '╚════════════════════════════════════════╝')



entrar_jogo = input("Deseja abrir o jogo? ('s' ou 'n')\n ") #iniciar do jogo

if entrar_jogo.lower() != 's' and entrar_jogo.lower() != 'n': #mensagem de erro para controle
    while entrar_jogo.lower() != 's' and entrar_jogo.lower() != 'n':
        print('Resposta inválida. Digite novamente!')
        entrar_jogo = input("Deseja abrir o jogo? ('s' ou 'n')\n ")


if entrar_jogo.lower() == 's': #caso o usuário escolha iniciar o jogo
    funcao = 'X'

if funcao == 'X':
    while funcao == 'X':
        menuiniciar1 ()

        funcao = input('O que deseja fazer?\n ')

        if funcao.upper() != 'J' and funcao.upper() != 'S': #mensagem de erro para controle
            while funcao.upper() != 'J' and funcao.upper() != 'S':
                print('Resposta inválida. Digite novamente!')
                funcao = input('O que deseja fazer?\n ')
                    

if funcao.upper() == 'J':
    funcao = 'V'

    while funcao.upper() == 'V':
        jogar1 ()
        funcao = input('O que deseja fazer?\n ')
    

    if funcao.upper() != 'F' and funcao.upper() != 'M' and funcao.upper() != 'D' and funcao.upper() != 'X': #mensagem de erro para controle
        while funcao.upper() != 'F' and funcao.upper() != 'M' and funcao.upper() != 'D' and funcao.upper() != 'X':
            print('Resposta inválida. Digite novamente!')
            funcao = input('O que deseja fazer?\n ')


          
if funcao.upper() == 'F':
    painel_facil()
    funcao = input('O que deseja fazer?\n ')

                            
    if funcao.upper() != 'I' and funcao.upper() != 'V': #mensagem de erro para controle
        while funcao.upper() != 'I' and funcao.upper() != 'V':
            print('Resposta inválida. Digite novamente!')
            funcao = input('O que deseja fazer?\n ')

    elif funcao.upper() == 'V':                   
            jogar1 ()
                                
    else:
        modo_facil_iniciado() #Inicia as chances FACIL



if funcao.upper() == 'M':
    painel_medio()
    funcao = input('O que deseja fazer?\n ')


    if funcao.upper() != 'I' and funcao.upper() != 'V': #mensagem de erro para controle
        while funcao.upper() != 'I' and funcao.upper() != 'V':
                                    print('Resposta inválida. Digite novamente!')
                                    funcao = input('O que deseja fazer?\n ')

    elif funcao.upper() =='I':
        modo_medio_iniciado() #Inicia as chances Médio

    elif funcao.upper() == 'V':
        jogar1 ()
                            


if funcao.upper() == 'D':
    painel_dificil()
    funcao = input('O que deseja fazer?\n ')


    if funcao.upper() != 'I' and funcao.upper() != 'V': #mensagem de erro para controle
        while funcao.upper() != 'I' and funcao.upper() != 'V':
            print('Resposta inválida. Digite novamente!')
            funcao = input('O que deseja fazer?\n ')


    elif funcao.upper() =='I':
        modo_dificil_iniciado() #Inicia as chances Dificil
        limpeza()

    elif funcao.upper() == 'V':
        jogar1 ()
           
                        
if funcao.upper() == 'V':
    jogar1 ()        
    limpeza()   

if funcao.upper() == 'S':
    limpeza()
    print('(ಥ﹏ಥ)')

else: #caso o usuário não queira iniciar o jogo =(
    limpeza()
    print('(ಥ﹏ಥ)')
    

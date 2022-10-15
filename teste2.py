def menu() -> None:
    print("""
    [ 1 ] criar cliente
    [ 2 ] cadastrar compras
    [ 3 ] listar compras por cliente
    [ 4 ] excluir uma compra
    [ 5 ] listar todas as compras
    [ 6 ] fechar o programa
    """)
    opcao = int(input("digite a opcao que voce dejesa: "))
    return opcao


Banco_de_dados = {
    "clientes":{
    }
}

id = 0
while True:
#Compra
    opcao = menu()

    if opcao == 1:
        cliente = input("cadastrar cliente: ")
        if cliente in Banco_de_dados["clientes"]:
            print("erro")
            continue
        Banco_de_dados["clientes"][cliente] = []


    elif opcao == 2:
        cliente = input("qual cliente vai fazer a compra: ")
        if Banco_de_dados["clientes"].get(cliente) == None:
            print("cliente nao existe")
            continue
        tipo_peixe = input(f'Qual a especie do peixe: ')
        peso_peixe = int(input(f'Qual o peso do peixe? '))
        Banco_de_dados["clientes"][cliente].append({"tipo_peixe":tipo_peixe,"peso_peixe":peso_peixe,"id":id})
        id += 1


    elif opcao == 3:
        cliente = input("digite o nome do cliente: ")
        if cliente not in Banco_de_dados["clientes"]:
            print("erro")
            continue
        for compra in Banco_de_dados["clientes"][cliente]:
            tipo_peixe,peso_peixe,ids = compra.values()
            print(f"tipo do peixe: {tipo_peixe} peso_peixe: {peso_peixe} id: {ids} ")

    elif opcao == 4:
        ver = False
        cliente = input("digite o nome: ")
        if cliente in Banco_de_dados["clientes"]:
            id_ = int(input("digite o id da compra que dejesa excluir: "))
            for indice,compra in enumerate(Banco_de_dados["clientes"][cliente]):
                if id_ == compra["id"]:
                    del Banco_de_dados["clientes"][cliente][indice]
                    ver = True
            print(f"{id_} foi apagado " if ver == True else f"id {id_} nao foi encontrado")


    elif opcao == 5:
        for nome,compras in Banco_de_dados["clientes"].items():
            print(nome)
            for compra in compras:
                tipo_peixe,peso_peixe,ids = compra.values()
                print(f"tipo do peixe: {tipo_peixe} peso_peixe: {peso_peixe} id: {ids} ")
            

    elif opcao == 6:
        print("fechar programa")
        break
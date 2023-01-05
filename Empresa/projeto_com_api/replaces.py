def altera_placa(placa:str):
    lista = ["A","B","C","D","E","F","G","H","I","J"]
    nova_placa = ""
    if placa[4].isnumeric():
        for index,char in enumerate(placa):
            if index != 4:
                nova_placa += char
            else:
                nova_placa += lista[int(placa[4])]
    else:
        for index,char in enumerate(placa):
            if index != 4:
                nova_placa += char
            else:
                nova_placa += f"{lista.index(placa[4])}"
    return nova_placa

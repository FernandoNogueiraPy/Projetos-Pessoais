from unidecode import unidecode
from api import get_marcas,get_modelo,get_preco,get_ref




def verify_marca(ref,marca_formulario,tipo_veiculo):
    marcas = get_marcas(ref,tipo_veiculo)
    for marca in marcas:
        name,value = marca.values()
        if unidecode(name).lower().strip() == unidecode(marca_formulario).lower().strip():
            return value
    raise ValueError("a marca esta errada no formulario")

    
def verify_modelo(ref,tipo_veiculo,marca,nome):
    modelos = get_modelo(ref,tipo_veiculo,marca)
    listagem = ['- 0P -  -  ','- 0P -  - ','- 5P - Básico - ','- 2P - Básico - ','- 4P - Básico - ',     '- 3P - Básico -','- 0P - Básico - ','- 0p - - ']
    for item in listagem:         
        if item in nome:             
            nome = nome.replace(item,"")             
            break
    for modelo in modelos:
        name,value = modelo.values()
        if unidecode(name).lower().strip() == unidecode(nome).lower().strip():
            return value


def verify(ref,tipo_veiculo,marca,tipo_combustivel,ano_modelo,nome):
    marca_certa = verify_marca(ref,marca,tipo_veiculo)
    modelo_certo = verify_modelo(ref,tipo_veiculo,marca_certa,nome)
    preco = get_preco(ref,tipo_veiculo,marca_certa,tipo_combustivel,ano_modelo,modelo_certo)

    
    return preco
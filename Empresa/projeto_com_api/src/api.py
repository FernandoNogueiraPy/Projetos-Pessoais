from requests import post
from json import loads


def get_ref():
	url_referencia = "http://veiculos.fipe.org.br/api/veiculos/ConsultarTabelaDeReferencia"
	req_referencia_mes = post(url_referencia).json()
	lastest_code = req_referencia_mes[0]['Codigo']
	return lastest_code


def get_marcas(ref,tipo_veiculo):
	"""
		tipo do veiculo
		[1 - carro]
		[2 - moto ]
		[3 - caminhao]
	"""
	url_marcas = "http://veiculos.fipe.org.br/api/veiculos/ConsultarMarcas"
	body = {
		"codigoTabelaReferencia": ref,
		"codigoTipoVeiculo": tipo_veiculo #1 carro #2 moto # caminhao
	}
	marcas  = post(url_marcas,data=body).json()
	return marcas



def get_modelo(ref,tipo_veiculo,marca):
	"""
		tipo do veiculo
		[1 - carro]
		[2 - moto ]
		[3 - caminhao]
	"""
	url_modelos = "http://veiculos.fipe.org.br/api/veiculos/ConsultarModelos"
	body = {
		"codigoTabelaReferencia": ref,
		"codigoTipoVeiculo": tipo_veiculo,# 1 carro #2 moto # caminhao
		"codigoMarca": marca 
	}
	response = post(url_modelos,data=body).json()
	return response["Modelos"]


def get_preco(ref,tipo_veiculo,marca,tipo_combustivel,anoModelo,codigoModelo):
	"""
		tipo do veiculo
		[1 - carro]
		[2 - moto ]
		[3 - caminhao]
	"""
	url_preco = 'http://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros'
	body = {
		"codigoTabelaReferencia": ref,
		"codigoTipoVeiculo": tipo_veiculo,# 1 carro #2 moto # caminhao
		"codigoMarca": marca,
		"codigoTipoCombustivel": tipo_combustivel,
		"anoModelo": anoModelo,
		"codigoModelo": codigoModelo,
		"tipoConsulta": "tradicional" 
	}
	response = post(url_preco,data=body).json()
	return response["Valor"]

salario = 1250

pergunta = int(input('Qual o valor do seu Sálario'))


if pergunta >= salario:
    novo_valor = (pergunta*10/100+pergunta)
    print(novo_valor)

else :
    novo_valor2 = (pergunta*15/100+pergunta)
    print(novo_valor2)
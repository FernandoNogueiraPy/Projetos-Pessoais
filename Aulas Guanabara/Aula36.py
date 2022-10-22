
p1 = int(input('Qual o valor da casa que deseja comprar ??? '))
p2 = int(input('Atualmente qual e o valor da sua renda ??? '))
p3 = int(input('Em quantos anos pretende financiar esta casa ???'))

v1 = p3*12
print('Tempo de emprestimo em meses =', v1)

v2 = p1/v1
print('O valor da parcela fica em $',v2,' Reais')

v3 = p2*30/100 
print('30% da sua renda representa $',v3,' Reias' )  #Cauculo de porcentagem.

v4 = p2 - v3 
print('Analisando ...')

if v4  >= v2 :
    print('Seu Emprestimo foi aprovado parabéns. ')

else :
    print('Seu emprestimo foi negado. ')
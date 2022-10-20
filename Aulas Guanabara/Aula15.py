p1 = float(input('Quantos dias o carro ficou alugado ?'))
p2 = float(input('Quantos KM foi percorrido com o carro ?'))

r1 = 60*p1
r2 = 0.15*p2

print(f'O Valor do aluguel foi de',r1,'pela quantidade de',p1,'dias de aluguel')
print(f'O Valor dos Kms rodados foram de',r2,'pela quantidade de',p2,'kms rodados com o veiculo')
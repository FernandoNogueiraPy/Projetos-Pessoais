r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))
s1 = r1 + r2
s2 = r1 + r3
s3 = r3 + r2
if s1 > r3 and s2 > r2 and s3 > r1 :
    print('Com as medidas das retas: 1: {} 2: {} 3: {}, é possivel montar um triângulo.'.format(s1, s2, s3))
else:
    print('Não é possível montar um triângulo com essas medidas.')
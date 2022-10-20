p1 = str(input('Escreva uma frase')).strip().upper()

r1 = p1.count('A')
print('A letra A aparece',r1,' vezes  na frase')

r2 = p1.find('A')
print('A letra A começa na casa',r2,'da frase')

r3 = p1.rfind('A')
print('A ultima letra A está na casa',r3,'da frase')
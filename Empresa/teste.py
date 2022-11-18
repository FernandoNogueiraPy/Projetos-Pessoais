
Tipo = (input('teste')) #Exp : 44-519190/20 - 14-1081377/22
Tipo2 = Tipo.split('-')[0]

print(Tipo2)
ListaC = ['40','41','42','43','44','45','46','47','48','49']

if Tipo2 in ListaC:
    print ('está em listac')
else: 
    print('não esta em listac')
#Entrar comum número e informarse ele é divisívelpor 10, por 5, por2 ouse não é
#divisível por nenhum destes.
from os import system
system('cls')

numero_01 = int(input('Digite o numero:  '))

if(numero_01 % 10 == 0):
    print('E divisivel por 10: ')
if(numero_01 %2 == 0):
    print('E disivel por 2: ')
if(numero_01 %5 == 0):
    print('É divisivel por 5: ')    
else:
    print('Não e divisível nem 10 por 2 e nem 5 ')    

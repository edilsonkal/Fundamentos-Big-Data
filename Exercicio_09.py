#Entrar com um número e informar se ele é ou não divisível por 5.
from os import system
system('cls')

valor_01 = int(input('Digite um numero:  '))

if(valor_01 % 5 == 0):
    print(f'E divisivel por 5: ')
else:
    print(f'Não e Divisível por 5: ' )    
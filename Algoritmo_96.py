#Entrar com um número e informar se ele é divisível por 3 e por 7.
from os import system
system('cls')

numero_01 = int(input('Digite o numero : '))

if( numero_01 %3==0 and numero_01 %7 ==0):
    print('É divisivel por 3 e por 7: ')
else:
    print('Não e divísivel por 3 por 7')    


#Construir um algoritmo que leia dois números e efetue a adição. Caso o valor so-
#mado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8;

#caso o valor somado seja menor ou igual a 20, este deverá ser apresentado sub-
#traindo-se 5.
from os import system
system('cls')


numero_01 = int(input('Digite um numero: '))
numero_02 = int(input('Digite o segundo numero:'))
total = numero_01 + numero_02

if(total > 20):
    total = total + 8
    print('total + 8')

elif (total <= 20):
    total = total - 5
    print(f'total menos  - {total} 5')
        
    


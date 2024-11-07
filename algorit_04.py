from os import system
system('cls')
import math

numero = int(input("Digite um numero: "))

raiz =  numero**(1/2)
quadrado = math.pow(numero,2)

if(numero>0):
    print(f'Riaz quadrada:  {raiz}')
    
else:
    print(f'Exponenciação:  {quadrado}')    
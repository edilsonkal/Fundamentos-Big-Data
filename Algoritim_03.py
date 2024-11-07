from os import system
system('cls')


Valor_01 = int(input("Digite um numero:  "))
Valor_02 = int(input("Digite um numero:  "))

total = Valor_01 + Valor_02

if(total>20):
    total = total + 8
    print(f'Total mais 8')
    
elif (total <= 20):    
    total = total - 5
    print(f'Total menos 5: {total}')    
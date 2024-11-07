from os import system
system('cls')

quarenta = 0.4
trinta = 0.3

salario = float(input("Digite o valor do salário:  "))

if(salario <= 1000):
    salarioReajustado = salario+(salario*quarenta)
    print(f'O salario reajustado:  {salarioReajustado}')
else:
    salarioReajustado = salario(salario*trinta) 
    print(f'O salario reajustado : R${salarioReajustado}')    

from os import system
system('cls')

idade = 15
altura = 1.75
etnia = "indigena"

print("Dados da candidata!!")

idade = int(int(input("Dgite a idade da candidata:   ")))
altura+ float(input("Digite a altura da candidata:  "))
etnia = input("Digite a etnia da candidata :   ")

if(idade == 15 and altura == 1.75 and etnia == "indigena"):
    print("Aprovado")
else:
    print("Reprovada!!")    
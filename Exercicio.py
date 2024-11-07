from os import system
system('cls')


idade  = int(input("digite a idade do candidato(a): "))

if(idade >=11):
    print("Você é infantil")
elif (idade >=12 and idade  <7):
    print("Você é juvenil")  
else:
    print("Adulto")     
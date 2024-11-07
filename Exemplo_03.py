from os import system
system('cls')

nome_vendedor = input("Digite o nome do vendedor:  ")
janeiro = float(input("Digite o valor de vendas de janeiro:  "))
Fevereiro = float(input("Dgite o valor de vendas de fevereiro: "))
Marco = float(input("Digite o valor de vendas de Março: "))

totalVendas  = janeiro + Fevereiro + Marco

if(totalVendas > 5000):
    comissao = totalVendas*0.04
    print(f'Vendedor : {nome_vendedor} \nTotal de vendas: R$ {totalVendas}  \nComissão : R$ {comissao}')
else: 
    comissao  = totalVendas*0.01
    print("--------------Resultado-------------")
    print(f'Vendendor {nome_vendedor} \nTotal de vendas: R$ {totalVendas}  \nComissão : R$ {comissao}')   
    
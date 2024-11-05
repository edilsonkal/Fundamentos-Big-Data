#Fórmula de juros composto A = P*(1=)
from os import system
system('cls')



import math
p = 160000
r = 0.05
n = 12
t = 30 

a = p*(1+r/n)**(n*t)
print(f' O valor final com juros compostos : {a}')

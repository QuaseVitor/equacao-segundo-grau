import math
import os


os.system("cls")

print("O modelo da equação de segundo grau padrão é: ")
print("              AX²+BX+C=0")
print(" ") 
A = int(input("Insira o valor de A: "))
print("              ",A ,"X²+BX+C=0")
B = int(input("Insira o valor de B: "))
print("              ",A ,"X²+", B ,"X+C=0")
C = int(input("Insira o valor de C: "))
print("              ",A ,"X² +", B ,"X +", C ,"=0")
print(" ") 
delta = B**2 - 4*A*C

if delta<0:
    print("Delta é menor que zero, logo essa equação não possui raizes reais")
    print(" ")  
else:
    raiz = math.sqrt(delta)

    X1 = (-B + raiz)/2*A
    X2 = (-B - raiz)/2*A
    print(" ")

    if X1 != X2:  
        print("Essa equação possui raizes reais")
        print("X1 = ", X1)
        print("X2 =", X2)
    else:
        print("Delta é igual a 0 então essa equação possui duas raizes reais iguais")
        print("X1 e X2 = ", X1)

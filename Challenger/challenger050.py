print ("="*19)
print("==>Challenger050<==")
print ("="*19)
print("Faça um programa que leia seis numeros inteiros e mostre a soma apenas dos números que forem pares. Se for impar, descarte")

num1=0
numPar=0
for capturaNum in range(0,6):
    num = int(input("Por favor digite um número: "))
    if num % 2 ==0:
        num1 = num+num1
        numPar = numPar+1

print("você digitou {} numeros pares, a soma desse número é {}".format(numPar,num1))

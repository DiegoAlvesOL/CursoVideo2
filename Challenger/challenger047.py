print ("="*19)
print("==>Challenger046<==")
print ("="*19)
print("Crie um programa que mostre os número pares ente 1 e 50")

for cont in range(0,51, 2):
    print(cont)
print("fim")

# Outra forma de resolver o problema
for cont in range(0,51):
    if cont % 2==0:
        print(cont, end=" ")
print("Fim")
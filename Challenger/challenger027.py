from tkinter.font import names

print ("="*19)
print("==>Challenger024<==")
print ("="*19)
print("Faça um programa que leia um nome e faça:")
print("=> Printe uma mensagem de saudação apenas com o primeiro nome")
print("=> Printe qual é o primeiro nome")
print("=> Printe qual é o ultimo nome")

name = str(input("Please, type your full name: ")).strip()

name_split = name.split()

# Mensagem de saudação e o primeiro nome da pessoa
print("Nice to meet you {}".format(name_split [0]))

# Último nome do individuo
print("Your last name is: {}".format(name_split[len(name_split)-1]))
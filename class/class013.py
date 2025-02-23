# aula de estrutura de repeticão for c in range():

# # Funciona colocar apenas o número.
# for c in range(3):
#     print("Diego")
#
# print("terminou")
#
# # realizar a contagem
# for c in range(0,7):
#     print(c)
# print("fim")
#
# # para realizar contagem regressiva
#
# for c in range (6,0, -1):
#     print(c)
# print("Fim")
#
# # para realizar uma conragem contando de 2 em 2
#
# for c in range(0, 7, 1):
#     print(c)
# print("Fiim")

#
# #  realizando o loop usando um número fornecido pelo usuário
# num1 = int(input("Digite um número: "))
# for c in range(num1, 0, -2):
#     print(c)
# print("Fim")

# aqui estou usando a estrutura de repetição para perguntar mais de uma vez.
# for c in range(0,3):
#     num3 = int(input("Digite um número: "))
# print(num3)
# print("fim")

# Posso pedir um número e somar.
num = 0
for c in range(0,3):
    num3 = int(input("Digite um número: "))
    num = num+num3
print("A soma dos números é: {}".format(num))
print("fim")
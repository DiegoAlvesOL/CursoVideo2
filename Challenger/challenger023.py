print ("="*19)
print("==>Challenger023<==")
print ("="*19)
print("Faça um programa que leia um  número de 0 à 9999 e mostre cada um dos digitos separadamente \n"
      "Ex: 1789 unidade: 9 dezena: 8 centena: 7 e milhar: 1")


num = int(input("Digite um número de 0 à 9999: "))
# vou dividir o número que eu pegar do usuáro pegando sua fatia inteira usando // e no final pegando seu resto usando o %
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print("checando o número digitado {}".format(num))
print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}". format(milhar))
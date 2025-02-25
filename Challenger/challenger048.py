print ("="*19)
print("==>Challenger046<==")
print ("="*19)
print("Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encotram no intevalo de 1 e 500")

num=0
contMult3=0
for cont in range(1,501, 2):
    if cont % 3 == 0:
            num = cont+num
            contMult3 = contMult3+1
            print(cont)
print("a soma dos {} números que são multiplos de 3 é {}".format(contMult3, num))


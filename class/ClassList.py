# num = [10, 2, 7, 5]
# names = ["Diego", "Rodrigo", "Thiago"]
from operator import index

Citys = ["São Paulo", "Paris", "Berlin", "Dublin"]
# myAdres = ["Tonlegee Road", 219, "Donaghmede", "Dublin"]
#
#
# print("my integer List", num)
# print("Name of my brothers", names)
# print("My favority citys at moment is ", Citys)
# print("My current address is ",myAdres)
#
# print(" ")
# print("This is my vilage: ", myAdres[2])
# print(" ")
# print("My olders brother is: ", names[1])
#
# # Se eu colocar o intex na frente da variável,
# newBrother = names
# print("make a cópi of my variable: ",newBrother)
#
# # eu também posso pegar um item da minha lista e assinar em uma posição diferente
# newBrother[0] = names[2]
#
# print("Result of copy my index 2 and past in index 0", newBrother)
#
# names[2] = "Carlos"
#
# print(names)
#
# # Aqui posso colocar o usuário para interagir com minha lista.
# talkUser = int(input("Input your index for favority City: "))
# print("My favor city is: ", Citys[(talkUser)])
#
# # Se eu dejar saber quantos dados possui em minha lista preciso usar o len
# print("How many citys i knew: ", len(Citys))
#
# # Como remover um item da lista
# print("Original list is: ", num)
# print("The size of my list is: ",len(num))
# del num [3]
# print(num)
# # para pegar o ultimo elemento da lista é
# print(num[-1])
#

# Activity in class
Num1 = [1,2,3,4,5]

# First part
# num2 = int(input("type one numberm: "))
# Num1[2] = num2
# print(Num1)
#
# # Second part
# del Num1[4]
# print(Num1)
#
# print("The lengh of the list is : ", len(Num1))



# Inserir novo elemento na minha lista. ao usar o metodo append ele insere um elemento no finalda lista
# print(Citys)
# Citys.append("Porto")
# print(Citys)
#
# # Citys.append(input("Type the name of the new City you had visit: "))
# print(Citys)
#
#
# # NewCity = input("Type other City: ")
# # Citys.append(NewCity)
#
# print("Resulto from the last city", Citys)
#
# # para inserir um elemento na posição que eu quiser devo usar o metodo insert
# Citys.insert(0,"Dubrovinick")
# print(Citys)
#
# Citys.insert(0,input("Type your new City: "))
# print(Citys)
#
#
# mynewList = []
# for i in range(5):
#     mynewList.insert(0, i+1)
# print(mynewList)
#
#
#
# mynewList2 = []
# for i in range(5):
#     mynewList2.append(i+1)
# print(mynewList2)


# beatles = []
# beatles.append("John Lennon",)
# beatles.append("McCartney")
# beatles.append("George Harrison")
# print(beatles)
#
# for NewMember in range(2):
#     NewMember2 = input("Type the new name of Member: ")
#     beatles.append(NewMember2)
# print("Now the band had this members", beatles)
#
# del beatles[3]
# print(beatles)
# del beatles[3]
# print(beatles)
#
# NewMember2 = input("Type the name of the last member: ")
# if NewMember2 == "Ringo Star":
#     beatles.insert(0,NewMember2)
#     print("Welcome to the band {}".format(NewMember2))
#     print("Now we are completely, our band if format for: ", beatles)
# else:
#     print("Sorry you type a wrong name! ")
#     print(beatles)
#
# print("The the current formation of the band is: ",beatles)

MyList = [10,20,2,9,1,4,6,3,8]
print(MyList)

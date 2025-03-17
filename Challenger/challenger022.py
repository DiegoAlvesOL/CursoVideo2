print ("="*19)
print("==>Challenger049<==")
print ("="*19)
print("Faça um programa solicite o nome completo do usuário e faça algumas mudanças ou checagens")

name = str (input("please type your full name: ")).strip()
# o .strip() irá retirar os estpaços do início e do final caso o usuário digite por acidente.

# Coverter o nome do usuário para letras maiusculas.
print("Seu nome em letra maiuscula é {}".format(name.upper()))

# Coverter o nome do usuário para letras minúsculas.
print("Seu nome em letra minuscula é {}".format(name.lower()))

# Quantas letras ao todo (sem considerar os espaços)
print("Seu nome tem ao todo {} letras".format(len(name) - name.count(" ")))

# Quantas letras tem o primeiro nome
print("Seu primeiro nome tem {} letras".format(name.find(" ")))

# Outra forma de contar a quantidade de letras do primeiro nome é separar o nome.
splitName =name.split()
print("Seu primeiro noome é {} e ele tem {} letrar".format(splitName[0], len(splitName[0])))


print ("="*19)
print("==>Challenger024<==")
print ("="*19)
print("Faça um programa que verifique se sua a cidade digitada começa com a palavra 'Santo'")

# Realizar a captura de dados do usuário
cidade = str(input("Type the name of your city: ")).strip()
print(cidade[:5].upper() == "SANTO")
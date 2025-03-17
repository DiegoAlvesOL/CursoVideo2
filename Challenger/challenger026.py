print ("="*19)
print("==>Challenger024<==")
print ("="*19)
print("Faça um programa que leia uma pelo teclado e moostre:")
print("=> Quantas vezes aparece a letra 'A'")
print("=> Em que posição a letra 'A' aparece pela primeira vez")
print("=> Em que posição a letra 'A' aparece pela ultima vez")


letra = str(input("Please, type your phrase: ")).strip().upper()
# Aqui estou contado quantas vezes tem a letra A, para isso, na captura eu converto todas as letras para maiúsculo
# pq na minha busca eu procuro por letras maiúsculas
print("A letra 'A' apreceu {} vezes".format(letra.count("A")))

# Aqui estou mostrando onde a letra A aparece pela primeira vez.
print("A letra 'A' aparece pela primeira vez na posião {}.".format(letra.find("A")))

# Aqui vou mostrar onde a letra A aparece pela ultima vez.
# O r.find quer dizer que o pytho vai contar começar a procurar da direita para esquerda.
print("A letra 'A' aparece pela última vez na posição {}".format(letra.rfind("A")))

# tota de posições na sua frase é de:
# Note que a quantidade de letrar é diferente da quantidade de posições pq os espaços entre as palavras contam como posição
# Importante destacar que se o usuario digitar espaço no início ou no final da frase o .strip na captura vai elemina-los.
print("A frase que vc digitou tem {} letrar".format(len(letra) - letra.count(" ")))



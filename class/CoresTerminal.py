print("\033[1;31;40mOla, Diego!\033[m")

print(
    """
    código das cores
    +===========================+
    | STYLE | TEXT | BACKGROUND |
    |   0   |  30  |     40     |
    |   1   |  31  |     41     |
    |   4   |  32  |     42     |
    |   7   |  33  |     43     |
    |       |  34  |     44     |
    |       |  35  |     45     |
    |       |  36  |     46     |
    |       |  37  |     47     |
    +===========================+
    """
)

print(
    """
    como executar as cores deve digitar o código \ 033[m tudo junto conforme exemplo abaixo
    +=================+
    | STYLE |TEXT|BACK|
    |   0   | \033[30m30\033[m | \033[40m40\033[m |
    |   1   | \033[31m31\033[m | \033[41m41\033[m |
    |   4   | \033[32m32\033[m | \033[42m42\033[m |
    |   7   | \033[33m33\033[m | \033[43m43\033[m |
    |       | \033[34m34\033[m | \033[44m44\033[m |
    |       | \033[35m35\033[m | \033[45m45\033[m |
    |       | \033[36m36\033[m | \033[46m46\033[m |
    |       | \033[37m37\033[m | \033[47m47\033[m |
    +=================+
    """
)

print("é poossivel realizar combinação de cores e estilo")

print("Como por exemplo")
print("\033[1;33;40mé poossivel\033[m realizar \033[4;30;45mcombinação de cores\033[m e \033[7;33;40mestilo\033[m")
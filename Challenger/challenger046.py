print ("="*19)
print("==>Challenger046<==")
print ("="*19)
print("O objetivo desse desafio e realizar uma contagem regressiva de 10 até 0 com intervalo de 1 segundo entre eles")

import time
for c in range(10, -1, -1):
    print(c)
    time.sleep(0.5)
print("fim")
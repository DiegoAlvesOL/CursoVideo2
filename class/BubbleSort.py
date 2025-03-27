myList = [11,14,12,10, 3, 23, 1, 3, 2]
size = len(myList)

for i in range (size -1):
    for j in range (size -1 -i):
        if myList[j] > myList[j+1]:
            temp = myList[j]
            myList[j] = myList[j+1]
            myList[j+1] = temp
        else:
            print("não houve troca")
print("nova ordenação da lista {}".format(myList))

# transformando meu bubble sort em uma função

def bubble_sort(myList):
    size = len(myList)

    for i in range(size-1):
        for j in range (size -1 -i):
            if myList[j] > myList[j+1]:
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
            else:
                print("Nou houve troca")
    return (myList)




print ("="*19)
print("==>Challenger030<==")
print ("="*19)
print("create a programme that reads an integer number and checks whether it is even or odd")

num = int(input("Enter a integer number: "))
result = num % 2
if result == 0:
    print("The number you typed is even")
else:
    print("The number you typed is odd")

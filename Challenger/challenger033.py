print("="*19)
print("==>Challenger033<==")
print("="*19)
print("create a programme that reads 3 inputs and prints which one is bigger")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter with the second number: "))
num3 = int(input("Enter with the third number: "))

bigger = num1
bigger_var = "num1"

if num2 > bigger:
    bigger = num2
    bigger_var = "num2"
if num3 > bigger:
    bigger = num3
    bigger_var = "num3"
print("The most bigger number entered was {}, which was entered as {}".format(bigger, bigger_var))

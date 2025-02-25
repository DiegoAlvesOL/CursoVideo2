print ("="*19)
print("==>Challenger049<==")
print ("="*19)
print("Faça uma tabuada")

num=0
num1 = int(input("Enter with integer number: "))
for c in range(0, 11):
    num = c * num1
    print("|{}x{:2}={:2}|".format(num1,c,num))
print(" ")

print("="*41)
print("==Outra forma de resolver esse problema==")
print("="*41)
print(" ")
for c in range(0,11):
    print("|{}x{:2}={:2}|".format(num1, c, num1*c))

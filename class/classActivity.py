from math import floor

# first example
# largest_number = -999999999
# number = int(input("Enter a number or type -1 to stop: "))
# while number != -1:
#     if number > largest_number:
#         largest_number = number
# number = int(input("Enter a number or type -1 to stop: "))
# print("The largest number is: ", largest_number)
#
# cocktail = 20.
# beer = 7.5
# moneyInMyWallet = 20.
# while moneyInMyWallet >= 7.5:
#     typeDrink = input("Enter name of your drink: ")
#     drinPrice = float(input("How much is your drink? "))
#
#     if drinPrice <= moneyInMyWallet:
#         moneyInMyWallet = moneyInMyWallet - drinPrice
#         print("Here is your", typeDrink,"Enjoy!")
#         print("Do you have in your wallet: ", moneyInMyWallet)
#     else :
#         # newDrink = floor(input("choose a drink more cheaper. How much is your new drink: "))
#         # newDrink <= moneyInMyWallet
#         print("Sorry i don't have money enought to buy your drink")
#         break
#
#     # moneyInMyWallet = moneyInMyWallet -7.5
#
# print("I left the pub, the money left is: ", moneyInMyWallet)
#


balance = 20.
beer = 7.50
negroni = 25.

print("Here there are just two drinks, Beer and Negroni! ")

typeOfDrink = int(input("Type 1 for beer, 2 for negroni or 3 for exit the program: "))
opntion = 1
opntion2 = 2
opntion3 = 3

opntion = beer
opntion2 = negroni

if typeOfDrink == 1:
    balance = balance - opntion
    print("Enjoy your Beer. do you have in your wallet {}".format (beer))
    print ("Thank you for visit us!")
    break







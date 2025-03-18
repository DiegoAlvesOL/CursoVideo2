print ("="*19)
print("==>Challenger028<==")
print ("="*19)
print("make a programme that asks the user to guess an integer, \n"
      " if he guessed the correct number print a congratulations message \n"
      " if not tell him that the number he entered is incorrect.")

secret_number = 4
print(" ")
guessed_number = int(input("type one integer number between 0 to 5: "))

if guessed_number != secret_number:
    print("Im sorry you choose the incorrect number: ")
    print("BOOOOOM!!!")
else:
    print("Congratulations! You managed to defuse the bomb")
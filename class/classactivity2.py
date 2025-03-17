secret_number = 777

user_number = int(input("Enter your number: "))

while user_number != secret_number:
    print("Ha ha ha you choose the incorrect number, try again oor yoou neve will left this loop: ")
    user_number = int(input("Enter your number: "))
#     if user_number != secret_number:
#         print("Ha ha ha you choose the incorrect number, try again oor yoou neve will left this loop: ")
#     user_number = int(input("Enter your number: "))
# else:
print(
        """
        +==============================+
        |Wel done my friend you got it |
        |you choose the corect number  |
        +==============================+
        """
    )
exit()
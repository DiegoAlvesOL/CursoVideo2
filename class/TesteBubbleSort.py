from BubbleSort import bubble_sort

stopAsk = "yes"
user_list = []
continue_input = "yes"

while continue_input == "yes":
    for i in range(4):
        num = int(input("Enter a number for your indice: "))
        user_list.insert(0,num)
        size = len(user_list)
        if size >=4:
            continue_input = str(input("Would you like to enter more 4 numbers? 'yes/no'")).strip().lower()

result_sorted = bubble_sort(user_list)

print("Your sorted list is: ",result_sorted)


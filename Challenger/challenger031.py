print("="*19)
print("==>Challenger031<==")
print("="*19)
print("create a programme that asks the user the distance of a journey and calculates it:")
print("up to 200km the value of the kilometre travelled is $0.50")
print("above 200km the value is $0.45, per km travelled")

distance = int(input("Enter with the distance of your journey: "))
if distance <= 200:
    ticket = distance * 0.50
    print("The value of your ticket is: ${:.2f}".format(ticket))
else:
    ticket = distance * 0.45
    print("The value of your ticket is: ${:.2f}".format(ticket))

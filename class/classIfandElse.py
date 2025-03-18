name = str(input("Please type your name: ")).strip().lower()

if name == "diego":
    print("Your name is wondeful")
else:
   print("Your name is boring!")
print("Good morning {} ".format(name))

# validação de nota

n1 = float(input("type your first score: "))
n2 = float(input("type your second scrore: "))
median = (n1 + n2)/2

if median < 5:
    print("Your final score is {},  sorry you don't pass in this subject: ".format(median))
else:
    print("Your final score is {}, congratulations you got it: ".format(median))
print("bye bye")

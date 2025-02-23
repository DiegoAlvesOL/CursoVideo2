print("="*21)
print("==CHALLENGER013==")
print("="*21)
print("The purpose of this activity is to receive an amount and calculate how much the new salary will be based on the percentage increase.")
print("="*21)

currentSalary = float(input("Please provide the employee's current salary: "))
percentage = int(input("Indicate how many per cent will be added to the employee's salary. "))
addedValue = (currentSalary/100)*percentage
newSalary = currentSalary+addedValue

print("The new salary of the employee is R${:.2f}: ".format(newSalary))


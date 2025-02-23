import tkinter

def buttonAction():
    currentSalary = float (oldSalary.get())
    percentage = float(percentageIncrease.get())
    addedValue = (currentSalary/100)*percentage
    result = currentSalary+addedValue
    resultMessage["text"]=result
    # print(result)
    return None

windown = tkinter.Tk()
windown.geometry("500x300")
windown.title("New Salary")

textSalary = tkinter.Label(windown, text="Esse programa irá calcular o novo salario do colaborador")
textSalary.pack(padx=10, pady=10)

oldSalary = tkinter.Entry(windown, width=30)
oldSalary.pack(padx=10, pady=10)

percentageIncrease = tkinter.Entry(windown, width=30)
percentageIncrease.pack(padx=10, pady=10)

buttonCalc = tkinter.Button(windown, text="Calcular", command=buttonAction)
buttonCalc.pack(padx=10, pady=10)

resultMessage = tkinter.Label(windown, text="")
resultMessage.pack(padx=10, pady=10)

windown.mainloop()
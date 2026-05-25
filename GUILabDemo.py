import tkinter as tk

root = tk.Tk()
root.title('BMI Calculator')
root.geometry('400x250')
root.config(bg='#E2B3FF')

# Widget variables
weight = tk.StringVar(value='0.0')
height = tk.StringVar(value='0.0')
bmiResult = tk.StringVar(value='No computation yet')

# Button Functions
def calculate():
    weightValue = float(weight.get())
    heightValue = float(height.get())

    bmi = weightValue/heightValue ** 2

    if bmi < 18.5:
        bmiResult.set(value=f'BMI: {bmi:.2f} (Underweight)')
    elif 18.5 < bmi < 24.9:
        bmiResult.set(value=f'BMI: {bmi:.2f} (Normal weight)')
    else:
        bmiResult.set(value=f'BMI: {bmi:.2f} (Overweight)')

def reset():
    weight.set(value='0.0')
    height.set(value='0.0')
    bmiResult.set(value='No computation yet')

entriesFrame = tk.Frame(root, bg=root['bg'])
entriesFrame.pack()

weightLabel = tk.Label(entriesFrame, text='Weight(kg)', font=('Avenir', 14), bg=root['bg'])
weightLabel.grid(row=0, column=0, padx=5, pady=10)
weightEntry = tk.Entry(entriesFrame, font=('Avenir', 14), textvariable=weight)
weightEntry.grid(row=0, column=1, padx=5, pady=10)

heightLabel = tk.Label(entriesFrame, text='Height(m)', font=('Avenir', 14), bg=root['bg'])
heightLabel.grid(row=1, column=0, padx=5, pady=10)
heightEntry = tk.Entry(entriesFrame, font=('Avenir', 14), textvariable=height)
heightEntry.grid(row=1, column=1, padx=5, pady=10)

buttonsFrame = tk.Frame(root, bg=root['bg'])
buttonsFrame.pack()

calculateBtn = tk.Button(buttonsFrame, text='Calculate', font=('Avenir', 14, 'bold'),width=12, command=calculate)
calculateBtn.pack(side='left', padx=5, pady=10)
resetBtn = tk.Button(buttonsFrame, text='Reset', font=('Avenir', 14, 'bold'), width=12, command=reset)
resetBtn.pack(side='left',padx=5, pady=10)

resultlabel = tk.Label(root, font=('Avenir', 16), bg=root['bg'], textvariable=bmiResult)
resultlabel.pack(padx=5, pady=10)

root.mainloop()
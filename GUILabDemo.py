import tkinter as tk

root = tk.Tk()
root.title('BMI Calculator')
root.geometry('400x250')
root.config(bg='#E2B3FF')

# Widget variables


# Button Functions


entriesFrame = tk.Frame(root, bg=root['bg'])
entriesFrame.pack()

weightLabel = tk.Label(entriesFrame, text='Weight(kg)', font=('Avenir', 14), bg=root['bg'])
weightLabel.grid(row=0, column=0, padx=5, pady=10)
weightEntry = tk.Entry(entriesFrame, font=('Avenir', 14))
weightEntry.grid(row=0, column=1, padx=5, pady=10)

heightLabel = tk.Label(entriesFrame, text='Height(m)', font=('Avenir', 14), bg=root['bg'])
heightLabel.grid(row=1, column=0, padx=5, pady=10)
heightEntry = tk.Entry(entriesFrame, font=('Avenir', 14))
heightEntry.grid(row=1, column=1, padx=5, pady=10)

buttonsFrame = tk.Frame(root, bg=root['bg'])
buttonsFrame.pack()

calculateBtn = tk.Button(buttonsFrame, text='Calculate', font=('Avenir', 14, 'bold'),width=12)
calculateBtn.pack(side='left', padx=5, pady=10)
resetBtn = tk.Button(buttonsFrame, text='Reset', font=('Avenir', 14, 'bold'), width=12)
resetBtn.pack(side='left',padx=5, pady=10)

resultlabel = tk.Label(root, font=('Avenir', 16), bg=root['bg'])
resultlabel.pack(padx=5, pady=10)

root.mainloop()
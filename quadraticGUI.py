# Quadratic Equation Solver GUI Project
import tkinter as tk
import math

class App(tk.Tk):
    def __init__(self):
        # App window properties 
        super().__init__()
        self.title('Quadratic Equation Solver')
        self.config(bg='#eef2ff')
        self.minsize(450, 320)
        self.resizable(False, False)
    
        # Widget Variables
        self.a = tk.StringVar(value='0.0')
        self.b = tk.StringVar(value='0.0')
        self.c = tk.StringVar(value='0.0')
        self.result = tk.StringVar()

        titleLabel = tk.Label(self, text='Quadratic Equation Solver', font=('Avenir', 18, 'bold'), fg='#4f46e5', bg=self['bg'])
        titleLabel.pack()
        equationLabel = tk.Label(self, text='ax^2 + bx + c = 0', font=('Avenir', 15, ), fg='#6b7280', bg=self['bg'])
        equationLabel.pack()
        entriesFrame = tk.Frame(self, bg='white', padx=20, pady=10)
        entriesFrame.pack(padx=10, pady=5)
        buttonsFrame = tk.Frame(self, bg=self['bg'])
        buttonsFrame.pack(padx=5, pady=5)
        resultLabel = tk.Label(self, text="No computation yet", font=('Avenir', 16), justify='left', textvariable=self.result)
        resultLabel.pack(padx=5, pady=(0, 5))

        aLabel = tk.Label(entriesFrame, text='Coefficient a:', font=('Avenir', 14), bg=entriesFrame['bg'])
        aLabel.grid(row=0, column=0, padx=5, pady=5)
        aEntry = tk.Entry(entriesFrame, font=('Avenir', 14), textvariable=self.a)
        aEntry.grid(row=0, column=1, padx=5, pady=5)
        bLabel = tk.Label(entriesFrame, text='Coefficient b:', font=('Avenir', 14), bg=entriesFrame['bg'])
        bLabel.grid(row=1, column=0, padx=5, pady=5)
        bEntry = tk.Entry(entriesFrame, font=('Avenir', 14), textvariable=self.b)
        bEntry.grid(row=1, column=1, padx=5, pady=5)
        cLabel = tk.Label(entriesFrame, text='Coefficient c:', font=('Avenir', 14), bg=entriesFrame['bg'])
        cLabel.grid(row=2, column=0, padx=5, pady=5)
        cEntry = tk.Entry(entriesFrame, font=('Avenir', 14), textvariable=self.c)
        cEntry.grid(row=2, column=1, padx=5, pady=5)

        solveBtn = tk.Button(buttonsFrame, text='Solve Equation', font=('Avenir', 14, 'bold'), bg='#6366f1', fg='white', width=15, command=self.solveEquation)
        solveBtn.pack(side='left', padx=5, pady=8)
        resetBtn = tk.Button(buttonsFrame, text='Reset', font=('Avenir', 14, 'bold'), bg='#6366f1', fg='white', width=15, command=self.reset)
        resetBtn.pack(side='left', padx=5, pady=8)

    # Functions for the Button commands
    def solveEquation(self):
        try:
            a = float(self.a.get())
            b = float(self.b.get())
            c = float(self.c.get())

            if a == 0:
                raise ValueError
            b = float(b)
            c = float(c)
            discriminant = b ** 2 - 4 * a * c
        except ValueError:
            self.result.set('**Invalid numeric entry value\n** Ensure that a is value greater than 0')
        else:
            partialRoot = -b/(2 * a)
            if discriminant > 0:
                root1 = partialRoot + math.sqrt(discriminant)/(2*a)
                root2 = partialRoot - math.sqrt(discriminant)/(2*a)
                self.result.set(f'The roots are real and distinct\nx1 = {root1:.2f}\nx2 = {root2:.2f}')
            elif discriminant < 0:
                root1 = str(f'{partialRoot:.2f} + {math.sqrt(-discriminant)/(2*a):.2f}j')
                root2 = str(f'{partialRoot:.2f} - {math.sqrt(-discriminant)/(2*a):.2f}j')
                self.result.set(f'The roots are real and complex\nx1 = {root1}\nx2 = {root2}')
            else:
                self.result.set(f'The roots are real and repeated\nx = {partialRoot:.2f} twice')

    def reset(self):
        self.a.set('0.0')
        self.b.set('0.0')
        self.c.set('0.0')
        self.result.set('')

app = App()
app.mainloop()
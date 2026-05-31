# BMI Calculator GUI Project
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        # App window properties 
        super().__init__()
        self.title('BMI Calculator')
        self.config(bg='#E2B3FF')
        # self.geometry('320x190')
        self.minsize(320, 190)
        self.resizable(False, False)
       
        # Widget attributes
        self.font = ('Montserrat', 12)
        self.weight = tk.StringVar(value='0.0')
        self.height = tk.StringVar(value='0.0')
        self.result = tk.StringVar()

       # Widgets for the BMI application
        titleLabel = tk.Label(text='BMI Health Checker', font=('Montserrat', 18, 'bold'), bg=self['bg'])
        titleLabel.pack()
        entriesFrame = tk.Frame(self, bg=self['bg'])
        entriesFrame.pack()
        buttonsFrame = tk.Frame(self, bg=self['bg'])
        buttonsFrame.pack()
        resultLabel = tk.Label(self, bg=self['bg'], font=self.font, textvariable=self.result)
        resultLabel.pack()

        weightLabel =tk.Label(entriesFrame, text='Weight (kg) : ', bg=self['bg'], font=self.font)
        weightLabel.grid(row=0, column=0, padx=5, pady=10)
        weightEntry =tk.Entry(entriesFrame, font=self.font, textvariable=self.weight)
        weightEntry.grid(row=0, column=1, padx=5, pady=10)
        weightEntry.focus_set()  # Cursor lands here automatically!
        heightLabel =tk.Label(entriesFrame, text='Height (m) : ', bg=self['bg'], font=self.font)
        heightLabel.grid(row=1, column=0, padx=5, pady=10)
        heightEntry =tk.Entry(entriesFrame, font=self.font, textvariable=self.height)
        heightEntry.grid(row=1, column=1, padx=5, pady=10)
        
        solveBtn = tk.Button(buttonsFrame, text='Calculate', font=self.font, width=10, command=self.calculateBMI)
        solveBtn.pack(ipadx=5, ipady=5, padx=5,pady=10,side='left')
        resetBtn = tk.Button(buttonsFrame, text='Reset', font=self.font, width=10, command=self.resetBMI)
        resetBtn.pack(ipadx=5, ipady=5, padx=5,pady=10,side='left')

    # Functions for the Button commands
    def calculateBMI(self):
        height = self.height.get()
        weight = self.weight.get()
        try:
            height = float(height)
            weight = float(weight)
            BMI = weight / height ** 2
        except ValueError:
            self.result.set('Invalid numeric entry value')
        except ZeroDivisionError:
            self.result.set('Invalid entry value for the height.')
        else:
            if BMI < 18.5:
                self.result.set(f'BMI: {BMI:.2f} (Underweight)')
            elif BMI > 18.5 and BMI < 24.9:
                self.result.set(f'BMI: {BMI:.2f} (Normal weight)')
            else:
                self.result.set(f'BMI: {BMI:.2f} (Overweight)')

    def resetBMI(self):
        self.weight.set('0.0')
        self.height.set('0.0')
        self.result.set('')
    
app = App()
app.mainloop()



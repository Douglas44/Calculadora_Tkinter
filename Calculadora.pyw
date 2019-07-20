from tkinter import *
from tkinter import messagebox

class Calculadora:
    def __init__(self, master):
        # Frame for values
        self.frame1 = Frame(master)
        self.frame1.pack()
        # Frame for buttons
        self.frame2 = Frame(master)
        self.frame2.pack()

        self.Barra_Valor = Entry(self.frame1, width=38, bd=5, bg='#c0c0c0', border='2px')
        self.Barra_Valor.pack()

        # Buttons of operations
        self.Clear = Button(self.frame2, bd=4, width=8, text='Clear', bg='#808080', foreground='white')
        self.Clear['command'] = self.Clearall
        self.Clear.grid(row=1, column=4)

        self.Sub = Button(self.frame2, bd=4, width=8, text='-', bg='#808080', foreground='white')
        self.Sub['command'] = lambda: self.Numbers_Operations("-")
        self.Sub.grid(row=4, column=1)

        self.Sum = Button(self.frame2, bd=4, width=8, text='+', bg='#808080', foreground='white')
        self.Sum['command'] = lambda: self.Numbers_Operations("+")
        self.Sum.grid(row=4, column=3)

        self.Mult = Button(self.frame2, bd=4, width=8, text='*', bg='#808080', foreground='white')
        self.Mult['command'] = lambda: self.Numbers_Operations("*")
        self.Mult.grid(row=2, column=4)

        self.Div = Button(self.frame2, bd=4, width=8, text='/', bg='#808080', foreground='white')
        self.Div['command'] = lambda: self.Numbers_Operations("/")
        self.Div.grid(row=3, column=4)

        self.Result = Button(self.frame2, bd=4, width=8, text='=', bg='#808080', foreground='white')
        self.Result['command'] = self.Equalbut
        self.Result.grid(row=4, column=4)

        # Buttons of numbers
        self.Num7 = Button(self.frame2, bd=4, width=8, text='7', bg='#808080', foreground='white')
        self.Num7['command'] = lambda: self.Numbers_Operations(7)
        self.Num7.grid(row=1, column=1)

        self.Num8 = Button(self.frame2, bd=4, width=8, text='8', bg='#808080', foreground='white')
        self.Num8['command'] = lambda: self.Numbers_Operations(8)
        self.Num8.grid(row=1, column=2)

        self.Num9 = Button(self.frame2, bd=4, width=8, text='9', bg='#808080', foreground='white')
        self.Num9['command'] = lambda: self.Numbers_Operations(9)
        self.Num9.grid(row=1, column=3)

        self.Num4 = Button(self.frame2, bd=4, width=8, text='4', bg='#808080', foreground='white')
        self.Num4['command'] = lambda: self.Numbers_Operations(4)
        self.Num4.grid(row=2, column=1)

        self.Num5 = Button(self.frame2, bd=4, width=8, text='5', bg='#808080', foreground='white')
        self.Num5['command'] = lambda: self.Numbers_Operations(5)
        self.Num5.grid(row=2, column=2)

        self.Num6 = Button(self.frame2, bd=4, width=8, text='6', bg='#808080', foreground='white')
        self.Num6['command'] = lambda: self.Numbers_Operations(6)
        self.Num6.grid(row=2, column=3)

        self.Num1 = Button(self.frame2, bd=4, width=8, text='1', bg='#808080', foreground='white')
        self.Num1['command'] = lambda: self.Numbers_Operations(1)
        self.Num1.grid(row=3, column=1)

        self.Num2 = Button(self.frame2, bd=4, width=8, text='2', bg='#808080', foreground='white')
        self.Num2['command'] = lambda: self.Numbers_Operations(2)
        self.Num2.grid(row=3, column=2)

        self.Num3 = Button(self.frame2, bd=4, width=8, text='3', bg='#808080', foreground='white')
        self.Num3['command'] = lambda: self.Numbers_Operations(3)
        self.Num3.grid(row=3, column=3)

        self.Num0 = Button(self.frame2, bd=4, width=8, text='0', bg='#808080', foreground='white')
        self.Num0['command'] = lambda: self.Numbers_Operations(0)
        self.Num0.grid(row=4, column=2)

    def Numbers_Operations(self, num):
        """Insert the numbers in Entry"""
        self.Barra_Valor.insert(END, num)

    def Clearall(self):
        """When the button clear is press"""
        self.Barra_Valor.delete(0, END)

    def Equalbut(self):
        """When the button Result is press"""
        try:
            resultado = eval(self.Barra_Valor.get())
            self.Barra_Valor.delete(0, END)
            self.Barra_Valor.insert(END, str(resultado))
        except:
            messagebox.showerror(title='Calcu Error', message='Error. Tente novamente')


if __name__ == '__main__':
    root = Tk()
    root.geometry('320x170')
    root.title('Calcu')
    #root.iconbitmap(default='Martz90-Circle-Calculator.ico')
    Calculadora(root)
    root.mainloop()

# Create a graphical application that accepts user inputs, performs some operation on them, 
# and then writes the output on the screen. For example, write a small calculator. Use the 
# tkinter library.
 

# It works..But Not completed Yet .... Because I have to use some Object oriented Concepts to make it work... which are not
# included in the curriculum of CBSE
# Because of not having an exact meaning of simple Calculator its getting difficult
# to not use some complex OOps concepts for creating a GUI calculator...
# Will make a simple calculator with simple arithmetic functions only

# Creating a Calculator app

from tkinter import *
import tkinter.ttk  as ttk

class CalculatorApp:
    def __init__(self,master):
        self.label = ttk.Label(master,text="Simple Calculator",font=("bold"))
        self.labelx = ttk.Label(master,text="x")
        self.labely = ttk.Label(master,text="y")
        self.inputx = ttk.Entry(master)
        self.inputy = ttk.Entry(master)
        self.labelOperant = ttk.Label(master,text="Choose Operation",padding=15)
        self.labelResult = ttk.Label(master,text="Result",padding=15,font=("bold"))
        

        self.badd = ttk.Button(master,text=" + ",command=self.add)
        self.bsub = ttk.Button(master,text=" - ",command=self.sub)
        self.bmul = ttk.Button(master,text=" * ",command=self.multi)
        self.bdiv = ttk.Button(master,text=" / ",command=self.div)

        self.label.grid(column=0,row=0,columnspan=4)
        self.labelx.grid(column=0,row=1)
        self.labely.grid(column=2,row=1)
        self.labelResult.grid(column=0,row=4,columnspan=4)

        self.inputx.grid(column=1,row=1)
        self.inputy.grid(column=3,row=1)
        self.labelOperant.grid(column=0,row=2,columnspan=4)

        self.badd.grid(column=0,row=3)
        self.bsub.grid(column=1,row=3)
        self.bmul.grid(column=2,row=3)
        self.bdiv.grid(column=3,row=3)
        

        self.labelx.configure(padding=10)
        self.labely.configure(padding=10)
        
    
    def add(self):
        self.labelOperant['text'] = "Addition"
        self.labelResult['text'] = self.x() + self.y()
    def sub(self):
        self.labelOperant['text'] = "Subtraction"
        self.labelResult['text'] = self.x() - self.y()
    def multi(self):
        self.labelOperant['text'] = "Multiplication"
        self.labelResult['text'] = self.x() * self.y()
    def div(self):
        self.labelOperant['text'] = "Division"
        if(self.y() == 0.0):
            self.labelResult['text'] = "Not defined"
        else:
            self.labelResult['text'] = self.x() / self.y()

    def x(self):
        if(self.inputx.get().isnumeric()):
            if(len(self.inputx.get()) == 0):
                return float(0.0)
            else:
                return float(self.inputx.get())
        else:
            return None
    def y(self):
        if(self.inputy.get().isnumeric()):
            if(len(self.inputy.get()) == 0):
                return float(0.0)
            else:
                return float(self.inputy.get())
        else:
            return None

def main():
    root = Tk()
    root.minsize(450,300)

    calc = CalculatorApp(root)

    root.mainloop()

if __name__ == "__main__" : main()
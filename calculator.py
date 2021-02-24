# calculator.py
# Exploration of tkinter
# Adpated from:
#   https://www.youtube.com/watch?v=YU67Dc8pbPU and https://www.youtube.com/watch?v=a84KYOwGc7U
# Updates:
# 1) Limited import to only what is used in app
# 2) Updated objects to tkinter.tkk which resolves an issue on OS X where text is not visible on buttons
# 3) Applied 'classic' theme style

from tkinter import Tk, END, messagebox
from tkinter.ttk import Button, Frame, Entry, Style # this overrides older controls in tkinter with newer tkk versions

calculator = Tk()
calculator.title("Calculator")
calculator.resizable(0,0)

style = Style()
style.theme_use('classic')

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master=None, *args, **kwargs)
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()
    
    def clearText(self):
        self.replaceText("0")

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)
    
    def calculateExpression(self):
        self.expression = self.display.get()
        self.expression = self.expression.replace("%","/ 100")
        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showerror("Error", "Invalid Input")

    def createWidgets(self):
        self.display = Entry(self)
        self.display.insert(0, "0")
        self.display.grid(row=0,column=0, columnspan=5, sticky="NWNESESE")

        self.sevenButton = Button(self, text="7", command=lambda: self.appendToDisplay("7"))
        self.sevenButton.grid(row=1, column=0, sticky="NWNESESE")

        self.eightButton = Button(self, text="8", command=lambda: self.appendToDisplay("8"))
        self.eightButton.grid(row=1, column=1, sticky="NWNESESE")

        self.nineButton = Button(self, text="9", command=lambda: self.appendToDisplay("9"))
        self.nineButton.grid(row=1, column=2, sticky="NWNESESE")

        self.timesButton = Button(self, text="*", command=lambda: self.appendToDisplay("*"))
        self.timesButton.grid(row=1, column=3, sticky="NWNESESE")

        self.clearButton = Button(self, text="C", command=lambda: self.clearText())
        self.clearButton.grid(row=1, column=4, sticky="NWNESESE")

        self.fourButton = Button(self, text="4", command=lambda: self.appendToDisplay("4"))
        self.fourButton.grid(row=2, column=0, sticky="NWNESESE")
        
        self.fiveButton = Button(self, text="5", command=lambda: self.appendToDisplay("5"))
        self.fiveButton.grid(row=2, column=1, sticky="NWNESESE")

        self.sixButton = Button(self, text="6", command=lambda: self.appendToDisplay("6"))
        self.sixButton.grid(row=2, column=2, sticky="NWNESESE")

        self.divideButton = Button(self, text="/", command=lambda: self.appendToDisplay("/"))
        self.divideButton.grid(row=2, column=3, sticky="NWNESESE")

        self.percentButton = Button(self, text="%", command=lambda: self.appendToDisplay("%"))
        self.percentButton.grid(row=2, column=4, sticky="NWNESESE")

        self.oneButton = Button(self, text="1", command=lambda: self.appendToDisplay("1"))
        self.oneButton.grid(row=3, column=0, sticky="NWNESESE")

        self.twoButton = Button(self, text="2", command=lambda: self.appendToDisplay("2"))
        self.twoButton.grid(row=3, column=1, sticky="NWNESESE")

        self.threeButton = Button(self, text="3", command=lambda: self.appendToDisplay("3"))
        self.threeButton.grid(row=3, column=2, sticky="NWNESESE")

        self.minusButton = Button(self, text="-", command=lambda: self.appendToDisplay("-"))
        self.minusButton.grid(row=3, column=3, sticky="NWNESESE")

        self.equalsButton = Button(self, text="=", command=lambda: self.calculateExpression())
        self.equalsButton.grid(row=3, column=4, sticky="NWNESESE", rowspan=2)

        self.zeroButton = Button(self, text="0", command=lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=4, column=0, sticky="NWNESESE", columnspan=2)

        self.pointButton = Button(self, text=".", command=lambda: self.appendToDisplay("."))
        self.pointButton.grid(row=4, column=2, sticky="NWNESESE")

        self.plusButton = Button(self, text="+", command=lambda: self.appendToDisplay("+"))
        self.plusButton.grid(row=4, column=3, sticky="NWNESESE")

app = Application(calculator).grid()
calculator.mainloop()
# Project by Pinghang Fan
# Making a calculator with Python Tkinter
# Following guide from Geeksforgeeks "Python | Simple GUI calculator using Tkinter"
# Upadated by me to display result after calculation on 4/6/2021

from tkinter import *
from tkinter.ttk import *

expression = ""
results = ""


def press(num):
    global expression
    global results
    global in_calculation

    if in_calculation == False:
        expression = expression + str(num)
        equation.set(expression) 

    if in_calculation == True:
        expression = results + str(num)
        results = expression
        equation.set(expression) 

def equalpress():
    try:
        global expression
        global results
        global in_calculation

        in_calculation = True
        results = str(eval(expression))
        equation.set(results)
    except:
        equation.set("Expression not valid")
        expression = ""

def clear():
    global expression
    global results
    global in_calculation

    in_calculation = False
    expression = ""
    results = ""
    equation.set("")


gui = Tk()

gui.configure(background="white")
gui.title("Pinghang's Calcualtor")
gui.geometry("400x180")

# StringVar() is a variable class
# This creates an instance of this class
equation = StringVar()
in_calculation = False

if in_calculation == False:
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

if in_calculation == True:
    expression_field = Entry(gui, textvariable=results)
    expression_field.grid(columnspan=4, ipadx=70)

#button style
style = Style()
style.configure('TButton', fg="black", bg="white", height=1, width=7)


#creating buttons
button1 = Button(gui, text="7", style='TButton', command=lambda: press(7))
button1.grid(row=2, column=0)

button2 = Button(gui, text="8", style='TButton', command=lambda: press(8))
button2.grid(row=2, column=1)

button3 = Button(gui, text="9", style='TButton', command=lambda: press(9))
button3.grid(row=2, column=2)

button4 = Button(gui, text="4", style='TButton', command=lambda: press(4))
button4.grid(row=3, column=0)

button5 = Button(gui, text="5", style='TButton', command=lambda: press(5))
button5.grid(row=3, column=1)

button6 = Button(gui, text="6", style='TButton', command=lambda: press(6))
button6.grid(row=3, column=2)

button7 = Button(gui, text="1", style='TButton', command=lambda: press(1))
button7.grid(row=4, column=0)

button8 = Button(gui, text="2", style='TButton', command=lambda: press(2))
button8.grid(row=4, column=1)

button9 = Button(gui, text="3", style='TButton', command=lambda: press(3))
button9.grid(row=4, column=2)

button0 = Button(gui, text="0", style='TButton', command=lambda: press(0))
button0.grid(row=5, column=1)

addition = Button(gui, text="+", style='TButton', command=lambda: press("+"))
addition.grid(row=5, column=3)

subtraction = Button(gui, text="-", style='TButton', command=lambda: press("-"))
subtraction.grid(row=4, column=3)

multiplication = Button(gui, text="×", style='TButton', command=lambda: press("*"))
multiplication.grid(row=3, column=3)

division = Button(gui, text="÷", style='TButton', command=lambda: press("/"))
division.grid(row=2, column=3)

equals = Button(gui, text="=", style='TButton', command=equalpress)
equals.grid(row=5, column=2)

decimal = Button(gui, text=".", style='TButton', command=lambda: press("."))
decimal.grid(row=5, column=0)

clearB = Button(gui, text="clear", style='TButton', command=clear)
clearB.grid(row=6, column=1)

gui.mainloop() 

#Import required libraries and modules
import tkinter as tk
from tkinter import StringVar
import math
#Define the main window
main_window=tk.Tk()
#Determine the size of the window
main_window.geometry('410x324')
#Name the window
main_window.title('My_Calculator')

#Define global variables
expression=''
input_text=StringVar()

#Define 3 functions
#Create a function for number and operator button clicks
def btn_click(item):
    global expression
    expression=expression +str(item)
    input_text.set(expression)

#Create a function to clear the input
def btn_clear():
    global expression
    expression =''
    input_text.set('')

#function to evaluate the expression
def btn_equal():
    global expression
    try:
        result=str(eval(expression))
        input_text.set(result)
        expression = ''
    except:
        input_text.set('Error')
        expression =''

def btn_sqrt():
    global expression
    try:
        result = str(math.sqrt(eval(expression)))
        input_text.set(result)
        expression = ''
    except:
        input_text.set('Error')
        expression = ''

#Creating frames to organize the widgets
#Top Frame
input_frame =tk.Frame(main_window, width=312, height=50, bd=0, highlightbackground='black',
                        highlightcolor='black',highlightthickness=1)
#Pack the frame using pack()
input_frame.pack(side='top')

#Creating and placing an Entry Widget (input field) in the frame
input_field = tk.Entry(input_frame,font=('arial', 18,'bold'),
                       textvariable=input_text, width= 50, bg='#eee', bd=0, justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

#Buttons Frame
btns_frame = tk.Frame(main_window,width=312,height=272.5,bg='grey')
btns_frame.pack()

#The next row contains the buttons for clearing and division, and square roots:
#Create a widget called btn_clearing

# Clear Button
btn_clearing = tk.Button(btns_frame, text='Clear', fg='black', width=32, height=3, bd=0, bg='#eee',
                         cursor="hand2", command=btn_clear)
btn_clearing.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

# Parentheses Buttons
tk.Button(btns_frame, text='(', fg='black', width=10, height=3, bd=0, bg='#eee',
          cursor='hand2', command=lambda: btn_click('(')).grid(row=2, column=4, padx=1, pady=1)
tk.Button(btns_frame, text=')', fg='black', width=10, height=3, bd=0, bg='#eee',
          cursor='hand2', command=lambda: btn_click(')')).grid(row=3, column=4, padx=1, pady=1)

# Percentage Button
tk.Button(btns_frame, text='%', fg='black', width=10, height=3, bd=0, bg='#eee',
          cursor='hand2', command=lambda: btn_click('/100')).grid(row=1, column=4, padx=1, pady=1)

btn_sqrt = tk.Button(btns_frame, text='√', fg='black', width=10, height=3, bd=0, bg='#eee',
                     cursor='hand2', command=btn_sqrt)
btn_sqrt.grid(row=0, column=4, padx=1, pady=1)

btn_div= tk.Button(btns_frame, text='/', fg='black', width= 10, height= 3, bd= 0, bg='#eee',
                   cursor='hand2', command=lambda: btn_click('/'))
#Position the division button in the main grid

btn_div.grid(row=0, column= 3, padx=1, pady=1)


#Create the third row of buttons for "7" "8" "9" and "*"
tk.Button(btns_frame, text='7',fg='black',width=10, height=3, bd=0, bg='#fff',
          cursor='hand2', command=lambda: btn_click(7)).grid(row= 1, column=0, padx=1,pady=1)
tk.Button(btns_frame, text='8',fg='black',width=10, height=3, bd=0, bg='#fff',
          cursor='hand2', command=lambda: btn_click(8)).grid(row= 1, column=1, padx=1,pady=1)
tk.Button(btns_frame, text='9',fg='black',width=10, height=3, bd=0, bg='#fff',
          cursor='hand2', command=lambda: btn_click(9)).grid(row= 1, column=2, padx=1,pady=1)
tk.Button(btns_frame, text='*',fg='black',width=10, height=3, bd=0, bg='#eee',
          cursor='hand2', command=lambda: btn_click('*')).grid(row= 1, column=3, padx=1,pady=1)

#Create the fourth row of buttons for "4" "5" "6" and "-"
tk.Button(btns_frame, text='4',fg='black',width=10, height=3, bd=0, bg='#fff',
          cursor='hand2', command=lambda: btn_click(4)).grid(row= 2, column=0, padx=1,pady=1)
tk.Button(btns_frame, text='5',fg='black',width=10, height=3, bd=0, bg='#fff',
          cursor='hand2', command=lambda: btn_click(5)).grid(row= 2, column=1, padx=1,pady=1)
tk.Button(btns_frame, text='6',fg='black',width=10, height=3, bd=0, bg='#fff',
          cursor='hand2', command=lambda: btn_click(6)).grid(row= 2, column=2, padx=1,pady=1)
tk.Button(btns_frame, text='-',fg='black',width=10, height=3, bd=0, bg='#eee',
          cursor='hand2', command=lambda: btn_click('-')).grid(row= 2, column=3, padx=1,pady=1)

#Create the fifth row of buttons for "1" "2" "3" and "+"
tk.Button(btns_frame, text='1',fg='black',width=10, height=3, bd=0, bg='#fff',
          cursor='hand2', command=lambda: btn_click(1)).grid(row= 3, column=0, padx=1,pady=1)
tk.Button(btns_frame, text='2',fg='black',width=10, height=3, bd=0, bg='#fff',
          cursor='hand2', command=lambda: btn_click(2)).grid(row= 3, column=1, padx=1,pady=1)
tk.Button(btns_frame, text='3',fg='black',width=10, height=3, bd=0, bg='#fff',
          cursor='hand2', command=lambda: btn_click(3)).grid(row= 3, column=2, padx=1,pady=1)
tk.Button(btns_frame, text='+',fg='black',width=10, height=3, bd=0, bg='#eee',
          cursor='hand2', command=lambda: btn_click('+')).grid(row= 3, column=3, padx=1,pady=1)

#Create the sixth row of buttons for "0" "." and "=":
tk.Button(btns_frame, text='0',fg='black',width=21, height=3, bd=0, bg='#fff',
          cursor='hand2', command=lambda: btn_click(0)).grid(row= 4, column=0, columnspan=2, padx=1,pady=1)
tk.Button(btns_frame, text='.',fg='black',width=10, height=3, bd=0, bg='#eee',
          cursor='hand2', command=lambda: btn_click('.')).grid(row= 4, column=2, padx=1,pady=1)
tk.Button(btns_frame, text='=',fg='black',width=21, height=3, bd=0, bg='#eee',
          cursor='hand2', command=btn_equal).grid(row= 4, column=3, columnspan=3, padx=1,pady=1)
main_window.mainloop()
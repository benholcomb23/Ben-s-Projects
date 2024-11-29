import tkinter as tk

root = tk.Tk()

root.title('Calculator')


#ValuesofExpressions
display_value = ''
total = ''

#Debug
def test_click():
    print('test works')

#Button Commands
def number_press(x):
    global display_value
    display_value = str(display_value) + str(x)
    display.config(text=display_value)

def clear():
    global display_value 
    display_value = ''
    display.config(text=display_value)

def calculate():
    try:
        global display_value
        global total
        total = str(eval(display_value))
        print(display_value)
        display_value = total
        display.config(text=total)
    except:
        clear()
        display.config(text='ERR')


#Number Display
display = tk.Label(root, text=display_value, width=20, fg= 'grey', bg= 'white')
display.grid(columnspan=5, row=0, column=0)

#Button Inputs
number_0 = tk.Button(root, text='0', width=2, command=lambda: number_press('0'))
number_0.grid(columnspan=3, row=5, column=0)

number_1 = tk.Button(root, text='1', width=2, command=lambda: number_press('1'))
number_1.grid(row=4, column=0)

number_2 = tk.Button(root, text='2', width=2, command=lambda: number_press('2'))
number_2.grid(row=4, column=1)

number_3 = tk.Button(root, text='3', width=2, command=lambda: number_press('3'))
number_3.grid(row=4, column=2)

number_4 = tk.Button(root, text='4', width=2, command=lambda: number_press('4'))
number_4.grid(row=3, column=0)

number_5 = tk.Button(root, text='5', width=2, command=lambda: number_press('5'))
number_5.grid(row=3, column=1)

number_6 = tk.Button(root, text='6', width=2, command=lambda: number_press('6'))
number_6.grid(row=3, column=2)

number_7 = tk.Button(root, text='7', width=2, command=lambda: number_press('7'))
number_7.grid(row=2, column=0)

number_8 = tk.Button(root, text='8', width=2, command=lambda: number_press('8'))
number_8.grid(row=2, column=1)

number_9 = tk.Button(root, text='9', width=2, command=lambda: number_press('9'))
number_9.grid(row=2, column=2)

number_dot = tk.Button(root, text='.', width=2)
number_dot.grid(row=5, column=2)

#Misc Buttons
clear_button = tk.Button(root, text='C', width=2, command=lambda: clear())
clear_button.grid(row=1, column=1)

negative_positive_button = tk.Button(root, text='+/-', width=2,)
negative_positive_button.grid(row=1, column=2)

all_clear_button = tk.Button(root, text='AC', width=2)
all_clear_button.grid(row=1, column=0)

#Function Buttons
divide_button = tk.Button(root, text='/', width=2, command=lambda: number_press('/'))
divide_button.grid(row=1, column= 3)

multiply_button = tk.Button(root, text='X', width=2, command=lambda: number_press('*'))
multiply_button.grid(row=2, column= 3)

subtract_button = tk.Button(root, text='-', width=2, command=lambda: number_press('-'))
subtract_button.grid(row=3, column= 3)

add_button = tk.Button(root, text='+', width=2, command=lambda: number_press('+'))
add_button.grid(row=4, column= 3)

equals_button = tk.Button(root, text='=', width = 2, command=lambda: calculate())
equals_button.grid(row=5, column=2)



root.mainloop()


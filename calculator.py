from tkinter import *
from tkinter import ttk

# colors

dark_blue = '#145369'
darker_blue = '#041014'
light_blue = '#2596be'
white = '#fefefe'

# window

window = Tk()
window.title('Calculator')
window.geometry('320x480')
window.config(bg=darker_blue)
window.resizable(False, False)

# frames

frame_display = Frame(window, width=320, height=85, bg=darker_blue)
frame_display.grid(row=0, column=0)

frame_keyboard = Frame(window, width=320, height=400, bg=darker_blue)
frame_keyboard.grid(row=1, column=0)

# label
value = StringVar()

label = Label(frame_display, textvariable=value, width=15,
              height=2, padx=4, relief=FLAT, anchor='e', justify=RIGHT, font='Ivy 24', bg=darker_blue, fg=white)
label.place(x=0, y=0)

# buttons

expression = ''


# function

def type_key(key):
    global expression
    if key == 'C':
        expression = ''
    if len(str(expression) + str(key)) < 15:
        if key == '=':
            try:
                result = eval(expression)
                if str(result)[::-1].find('.') > 9:
                    expression = '%.9f' % result
                else:
                    expression = result
            except:
                ...
        elif key != 'C' and key != '=':
            expression = str(expression) + str(key)
        value.set(expression)


b_1 = Button(frame_keyboard, text='C', bg=white,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('C'))
b_1.place(x=0, y=0, width=160, height=79)
b_2 = Button(frame_keyboard, text='%', bg=white,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('%'))
b_2.place(x=160, y=0, width=80, height=79)
b_3 = Button(frame_keyboard, text='/', bg=light_blue, fg=white,
             activebackground=dark_blue, activeforeground=white, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('/'))
b_3.place(x=240, y=0, width=80, height=79)

b_4 = Button(frame_keyboard, text='7', bg=white,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('7'))
b_4.place(x=0, y=79, width=80, height=79)
b_5 = Button(frame_keyboard, text='8', bg=white,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('8'))
b_5.place(x=80, y=79, width=80, height=79)
b_6 = Button(frame_keyboard, text='9', bg=white,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('9'))
b_6.place(x=160, y=79, width=80, height=79)
b_6 = Button(frame_keyboard, text='*', bg=light_blue, fg=white,
             activebackground=dark_blue, activeforeground=white, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('*'))
b_6.place(x=240, y=79, width=80, height=79)

b_7 = Button(frame_keyboard, text='4', bg=white,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('4'))
b_7.place(x=0, y=158, width=80, height=79)
b_8 = Button(frame_keyboard, text='5', bg=white,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('5'))
b_8.place(x=80, y=158, width=80, height=79)
b_9 = Button(frame_keyboard, text='6', bg=white,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('6'))
b_9.place(x=160, y=158, width=80, height=79)
b_10 = Button(frame_keyboard, text='-', bg=light_blue, fg=white,
              activebackground=dark_blue, activeforeground=white, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('-'))
b_10.place(x=240, y=158, width=80, height=79)

b_11 = Button(frame_keyboard, text='1', bg=white,
              font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('1'))
b_11.place(x=0, y=237, width=80, height=79)
b_12 = Button(frame_keyboard, text='2', bg=white,
              font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('2'))
b_12.place(x=80, y=237, width=80, height=79)
b_13 = Button(frame_keyboard, text='3', bg=white,
              font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('3'))
b_13.place(x=160, y=237, width=80, height=79)
b_14 = Button(frame_keyboard, text='+', bg=light_blue, fg=white,
              activebackground=dark_blue, activeforeground=white, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('+'))
b_14.place(x=240, y=237, width=80, height=79)

b_15 = Button(frame_keyboard, text='0', bg=white,
              font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('0'))
b_15.place(x=0, y=316, width=160, height=79)
b_16 = Button(frame_keyboard, text='.', bg=white,
              font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('.'))
b_16.place(x=160, y=316, width=80, height=79)
b_17 = Button(frame_keyboard, text='=', bg=light_blue, fg=white,
              activebackground=dark_blue, activeforeground=white, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: type_key('='))
b_17.place(x=240, y=316, width=80, height=79)

window.mainloop()

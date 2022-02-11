from tkinter import *


root = Tk()     # настройки окна
root.title('Sign Up')
root.geometry('600x800')
root.resizable(False, False)

frame1 = Frame(root, bg='orange')
frame1.place(relx=0.005, rely=0.005, relwidth=0.99, relheigh=0.99)
frame2 = Frame(root, bg='black')
frame2.place(relx=0.005, rely=0.01, relwidth=0.99, relheigh=0.8)

# настройка кнопок
button_can = Button(root, text='cancel', width=5, height=1, bg='red', fg='white', font='arial 10')
button_can.place(x=530, y=760)
button_sub = Button(root, text='submit', width=5, height=1, bg='green', fg='white', font='arial 10')
button_sub.place(x=470, y=760)

root.mainloop()

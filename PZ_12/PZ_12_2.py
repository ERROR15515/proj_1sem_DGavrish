from tkinter import *


def check(event):
    n1 = int(num1.get())
    n2 = int(num2.get())

    if n1 % 2 != 0 and n2 % 2 != 0:
        positive['text'] = " Условие выполнено "

    if n1 % 2 == 0 or n2 % 2 == 0:
        positive['text'] = " Условие не выполнено "


root = Tk()
root.title('Проверка на нечетность')
root.geometry('500x150')

label1 = Label(root, text="Введите 1-ое число: ", font='Arial 12')
label1.place(x=25, y=20)
num1 = Entry()
num1.place(x=200, y=25)

label2 = Label(root, text="Введите 2-ое число: ", font='Arial 12')
label2.place(x=25, y=45)
num2 = Entry()
num2.place(x=200, y=50)

button1 = Button(text="Обработать")
button1.place(x=200, y=85)

positive = Label()
positive.place(x=175, y=110)

button1.bind('<Button-1>', check)

root.mainloop()

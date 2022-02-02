from tkinter import *


def window_deleted():
    print('Окно закрыто')
    root.quit()


root = Tk()
root.title('Пример приложения')
root.geometry('600x800')
root.protocol('WM_DELETE_WINDOW', window_deleted)
root.resizable(True, False)
root.mainloop()

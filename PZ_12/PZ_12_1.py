from tkinter import *
from tkinter import ttk


# настройки окна
root = Tk()
root.title('Sign Up')
root.geometry('600x800')
root.resizable(False, False)

frame1 = Frame(root, bg='orange')
frame1.place(relx=0.005, rely=0.005, relwidth=0.99, relheigh=0.99)
frame2 = Frame(root, bg='#0d1c33')
frame2.place(relx=0.005, rely=0.05, relwidth=0.99, relheigh=0.89)

# настройка кнопок
button_can = Button(root, text='cancel', width=5, height=1, bg='red',
                    fg='white', font='arial 10')
button_can.place(x=530, y=760)
button_sub = Button(root, text='submit', width=5, height=1, bg='green',
                    fg='white', font='arial 10')
button_sub.place(x=470, y=760)

# настройки текстов
lab_sig = Label(root, text='Sign up', bg='orange', fg='yellow',
                font='arial 15')
lab_sig.place(x=10, y=7)
lab_fn = Label(root, text='First Name', bg='#0d1c33', fg='white',
               font='arial 12')
lab_fn.place(x=120, y=80)
lab_ln = Label(root, text='Last Name', bg='#0d1c33', fg='white',
               font='arial 12')
lab_ln.place(x=122, y=130)
lab_sn = Label(root, text='Screen Name', bg='#0d1c33', fg='white',
               font='arial 12')
lab_sn.place(x=102, y=180)
lab_db = Label(root, text='Date of Birth', bg='#0d1c33', fg='white',
               font='arial 12')
lab_db.place(x=110, y=230)
lab_g = Label(root, text='Gender', bg='#0d1c33', fg='white',
              font='arial 12')
lab_g.place(x=145, y=280)
lab_c = Label(root, text='Country', bg='#0d1c33', fg='white',
              font='arial 12')
lab_c.place(x=145, y=330)
lab_em = Label(root, text='E-Mail', bg='#0d1c33', fg='white',
               font='arial 12')
lab_em.place(x=150, y=380)
lab_p = Label(root, text='Phone', bg='#0d1c33', fg='white',
              font='arial 12')
lab_p.place(x=152, y=430)
lab_pw = Label(root, text='Password', bg='#0d1c33',
               fg='white', font='arial 12')
lab_pw.place(x=130, y=480)
lab_cpw = Label(root, text='Confirm Password', bg='#0d1c33',
                fg='white', font='arial 12')
lab_cpw.place(x=72, y=530)

# Настройки пис. панелей
ent_fn = Entry(root, width=45)
ent_fn.place(x=220, y=80)
ent_ln = Entry(root, width=45)
ent_ln.place(x=220, y=130)
ent_sn = Entry(root, width=45)
ent_sn.place(x=220, y=180)
ent_em = Entry(root, width=45)
ent_em.place(x=220, y=380)
ent_ph = Entry(root, width=45)
ent_ph.place(x=220, y=430)
ent_pw = Entry(root, width=45)
ent_pw.place(x=220, y=480)
ent_cpw = Entry(root, width=45)
ent_cpw.place(x=220, y=530)

# поля выбора
listbox_db = ttk.Combobox(root, values=[u'January', u'February',
                                        u'March', u'April', u'May',
                                        u'June', u'July', u'August',
                                        u'September', u'October',
                                        u'November', u'December'],
                          width=10)
listbox_db.grid(column=1, row=1)
listbox_db.current(1)
listbox_db.place(x=220, y=230)
listbox_db = ttk.Combobox(root, values=[u'1', u'2', u'3', u'4', u'5',
                                        u'6', u'7', u'8', u'9', u'10',
                                        u'11', u'12', u'13', u'14',
                                        u'15', u'16', u'17', u'18',
                                        u'19', u'20', u'21', u'22',
                                        u'23', u'24', u'25', u'26',
                                        u'27', u'28', u'29', u'30',
                                        u'31'], width=5)
listbox_db.grid(column=1, row=1)
listbox_db.current(1)
listbox_db.place(x=330, y=230)
listbox_db = ttk.Combobox(root, values=[u'1960', u'1961', u'1962',
                                        u'1963', u'1964', u'1965',
                                        u'1966', u'1967', u'1968',
                                        u'1969', u'1970',
                                        u'1971', u'1972', u'1973',
                                        u'1974',
                                        u'1975', u'1976', u'1977',
                                        u'1978',
                                        u'1979', u'1980', u'1981',
                                        u'1982',
                                        u'1983', u'1984', u'1985',
                                        u'1986',
                                        u'1987', u'1988', u'1989',
                                        u'1990',
                                        u'1991', u'1992', u'1993',
                                        u'1994', u'1995', u'1996',
                                        u'1997', u'1998', u'1999',
                                        u'2000', u'2001', u'2002',
                                        u'2003', u'2004', u'2005',
                                        u'2006', u'2007', u'2008',
                                        u'2009', u'2010'], width=10)
listbox_db.grid(column=1, row=1)
listbox_db.current(1)
listbox_db.place(x=410, y=230)
listbox_db = ttk.Combobox(root, values=[u'USA', u'Russia',
                                        u'Germany', u'England', u'China',
                                        u'S.Korea', u'Japan', u'Australia',
                                        u'France', u'Mexico',
                                        u'Brazil', u'Canada'],
                          width=41)
listbox_db.grid(column=1, row=1)
listbox_db.current(1)
listbox_db.place(x=220, y=330)

# чек маркеры
var = IntVar()
rbutton_g1 = Radiobutton(root, text='Male', variable=var, value=1,
                         bg='#0d1c33', fg='grey')
rbutton_g1.place(x=220, y=280)
rbutton_g2 = Radiobutton(root, text='Female', variable=var, value=2,
                         bg='#0d1c33', fg='grey')
rbutton_g2.place(x=290, y=280)
var2 = IntVar()
check = Checkbutton(root, text='I agree to the Terms of Use',
                    variable=var2, onvalue=1, offvalue=0, bg='#0d1c33',
                    fg='grey')
check.place(x=200, y=580)


root.mainloop()

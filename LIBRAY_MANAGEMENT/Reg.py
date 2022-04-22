from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
py=sys.executable

#creating window
class reg(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500, 417)
        self.minsize(500, 417)
        self.title('Add User')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
#creating variables Please chech carefully
        u = StringVar()
        n = StringVar()
        p = StringVar()


        def insert():
            try:
                print('check1')
                self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='Mysql@1009')
                print('check2')
                self.myCursor = self.conn.cursor()
                print('check3')
                self.myCursor.execute("INSERT INTO admin(user,name,password) VALUES(%s,%s,%s)",(u.get(), n.get(), p.get()))
                print('check4')
                self.conn.commit()
                print('check5')
                messagebox.showinfo("Done", "User Inserted Successfully")
                ask = messagebox.askyesno("Confirm", "Do you want to add another user?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'Reg.py'))
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except Error:
                messagebox.showinfo("Error", "Something Goes Wrong")
#label and input
        Label(self, text='User Details', bg='gray', fg='black', font=('Courier new', 25, 'bold')).place(x=130, y=22)
        Label(self, text='Username:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=82)
        Entry(self, textvariable=u, width=30).place(x=200, y=84)
        Label(self, text='Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=130)
        Entry(self, textvariable=n, width=30).place(x=200, y=132)
        Label(self, text='Password:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=p, width=30).place(x=200, y=182)
        Button(self, text="Submit", width=15, command=insert).place(x=230, y=220)
reg().mainloop()
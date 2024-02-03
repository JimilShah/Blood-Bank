import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
import sys
print('Python %s on %s' % (sys.version, sys.platform))

import mysql.connector
db = mysql.connector.connect(
     host='localhost',
     user='root',
     password='',
     database='bloodbank'
)
# conn = db.cursor()
#conn.execute('Create database bloodbank')
#create table (name (varchar(255)),lastname (varchar(255)),age (varchar(255)),bloodgroup (varchar(255)))

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    Id = listBox.selection()[0]
    select = listBox.set(Id)
    e1.insert(0,select['Id'])
    e2.insert(0,select['Name'])
    e3.insert(0,select['Lastname'])
    e4.insert(0,select['Age'])
    e5.insert(0,select['Blood_Group'])
    e6.insert(0,select['Mobile_No'])
    
 
 
def Add():
    Id = e1.get()
    Name = e2.get()
    Lastname = e3.get()
    Age = e4.get()
    Blood_group = e5.get()
    Mobile_no = e6.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="bloodbank")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO  form (Id,Name,Lastname,Age,Blood_group,Mobile_no) VALUES (%s, %s, %s, %s,%s,%s)"
       val = (Id,Name,Lastname,Age,Blood_group,Mobile_no)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
 
def update():
  
    Id = e1.get()
    Name = e2.get()
    Lastname = e3.get()
    Age = e4.get()
    Blood_group = e5.get()
    Mobile_no = e6.get()
  
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="bloodbank")
    mycursor=mysqldb.cursor()

    try:
        sql = "UPDATE form SET Name= %s,Lastname=%s,Age= %s,Blood_Group=%s,Mobile_no= %s where id= %s"
        val = (Name,Lastname,Age,Blood_group,Mobile_no,Id)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updateddddd successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e1.focus_set()
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def delete():
    Id = e1.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="bloodbank")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "delete from form where Id = %s"
       val = (Id,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="bloodbank")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT Id,Name,Lastname,Age,Blood_group,Mobile_no FROM form")
        records = mycursor.fetchall()
        print(records)
 
        for i, (Id,Name,Lastname,Age,Blood_group,Mobile_no) in enumerate(records, start=1):
            listBox.insert("", "end", values=(Id,Name,Lastname,Age,Blood_group,Mobile_no))
            mysqldb.close()
 
root = Tk()
root.geometry("1200x500")
global e1
global e2
global e3
global e4
global e5
global e6

tk.Label(root, text="Blood Bank Registation", fg="red", font=(None, 50)).place(x=300, y=5)
 
tk.Label(root, text="USER ID").place(x=10, y=10)
Label(root, text="NAME").place(x=10, y=30)
Label(root, text="LAST NAME").place(x=10, y=50)
Label(root, text="AGE").place(x=10, y=70)
Label(root, text="BLOOD GROUP").place(x=10, y=90)
Label(root, text="MOBILE NO").place(x=10, y=110) 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=30)
 
e3 = Entry(root)
e3.place(x=140, y=50)
 
e4 = Entry(root)
e4.place(x=140, y=70)

e5= Entry(root)
e5.place(x=140, y=90)

e6 = Entry(root)
e6.place(x=140, y=110)
 
Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=130)
Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=130)
Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=130)
 
cols = ('Id', 'Name', 'Lastname','Age','Blood_Group','Mobile_No')
listBox = ttk.Treeview(root, columns=cols, show='headings' )
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)
 
show()
listBox.bind('<Double-Button-1>',GetValue)
 
root.mainloop()

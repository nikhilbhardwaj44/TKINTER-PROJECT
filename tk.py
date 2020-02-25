from tkinter import *
import sqlite3

root = Tk()
#geometry method is used to set the dimensions of the Tkinter window 
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   prog=var1.get()
   conn = sqlite3.connect('F.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender) VALUES(?,?,?)',(name1,email,gender,))
   conn.commit()
   
   
 # A Label is a Tkinter Widget class, which is used to display text or an image            
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

root.mainloop()
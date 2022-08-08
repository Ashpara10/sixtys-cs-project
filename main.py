import tkinter as tk
from  AddBook import addBook
import pymysql

root = tk.Tk()
root.title("Quandale Dingle")
root.minsize(width=400,height=400)
root.geometry("600x500")
same=True
n=0.70

# Connnecting to mysql 

# --------------------------

mypass = "ashpara21092005" #use your own password
mydatabase="db" #The database name
con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor()
# --------------------------

print(cur.execute("SELECT title FROM books"))


headingFrame1 = tk.Frame(root,bg="#212121",bd=5)
headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)
headingLabel = tk.Label(headingFrame1, text="Welcome to \n Sixty's Library", bg='#212121', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = tk.Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = tk.Button(root,text="Delete Book",bg='black', fg='white')
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = tk.Button(root,text="View Book List",bg='black', fg='white', )
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = tk.Button(root,text="Issue Book to Student",bg='black', fg='white', )
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = tk.Button(root,text="Return Book",bg='black', fg='white', )
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()

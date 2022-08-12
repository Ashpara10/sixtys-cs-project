import tkinter as tk
import tkinter.ttk as ttk
from  AddBook import addBook
from  DeleteBook import delete as deleteBook
import pymysql

root = tk.Tk()
root.title("Dataflair")
root.minsize(width=400,height=400)
root.geometry("600x500")
same=True
n=0.70

# Connnecting to mysql 

# --------------------------

mypass = "ashpara21092005" #use your own password
mydatabase="db" #The database name
con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor()
# --------------------------



headingFrame1 = ttk.Frame(root,padding=10)
headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)
headingLabel = ttk.Label(headingFrame1, text="Welcome to \n Sixty's Library", font=('Courier',15),border=50)
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


btn1 = ttk.Button(root,text="Add Book Details",command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = ttk.Button(root,text="Delete Book",command=deleteBook)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = ttk.Button(root,text="View Book List" )
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = ttk.Button(root,text="Issue Book to Student" )
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = ttk.Button(root,text="Return Book")
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()

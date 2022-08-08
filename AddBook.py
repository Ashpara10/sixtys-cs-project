import tkinter as tk
def log():
    print("id :"+bookInfo1.get()+"\n"+"title :"+bookInfo2.get()+"\n"+"author :"+bookInfo3.get()+"\n"+"status :"+bookInfo4.get())

def addBook():
 global bookInfo1,bookInfo2,bookInfo3,bookInfo4 
 root = tk.Tk()
 root.title("Library")
 root.minsize(width=400,height=400)
 root.geometry("600x500")


 Canvas1 = tk.Canvas(root)   
 Canvas1.config(bg="#ff6e40")
 Canvas1.pack(expand=True,fill=tk.BOTH)
     
 headingFrame1 = tk.Frame(root,bg="#FFBB00",bd=5)
 headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13) 
 headingLabel = tk.Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
 headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1) 
 labelFrame = tk.Frame(root,bg='black')
 labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
     
 # Book ID
 lb1 = tk.Label(labelFrame,text="Book ID : ", bg='black', fg='white')
 lb1.place(relx=0.05,rely=0.2, relheight=0.08)
     
 bookInfo1 = tk.Entry(labelFrame)
 bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
#  bookInfo1.pack(padx=10,pady=10)
     
 # Title
 lb2 = tk.Label(labelFrame,text="Title : ", bg='black', fg='white')
 lb2.place(relx=0.05,rely=0.35, relheight=0.08)

 bookInfo2 = tk.Entry(labelFrame)
 bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
     
 # Book Author
 lb3 = tk.Label(labelFrame,text="Author : ", bg='black', fg='white')
 lb3.place(relx=0.05,rely=0.50, relheight=0.08)
     
 bookInfo3 = tk.Entry(labelFrame)
 bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
     
 # Book Status
 lb4 = tk.Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
 lb4.place(relx=0.05,rely=0.65, relheight=0.08)
     
 bookInfo4 = tk.Entry(labelFrame)
 bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
     
 #Submit Button
 SubmitBtn = tk.Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=log)
 SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
 
 quitBtn = tk.Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
 quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08) 
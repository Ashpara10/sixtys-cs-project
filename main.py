import tkinter as tk


root = tk.Tk()
root.title("Quandale Dingle")
root.minsize(width=400,height=400)
root.geometry("600x500")
same=True
n=0.70

headingFrame1 = tk.Frame(root,bg="#212121",bd=5)
headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)
headingLabel = tk.Label(headingFrame1, text="Welcome to \n Sixty's Library", bg='#212121', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
root.mainloop()

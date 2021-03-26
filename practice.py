import tkinter
from tkinter import*
from tkinter import messagebox
import string
import random

root = tkinter.Tk()
root.geometry("400x200")
root.resizable(0,0)
root.title("password generator")

def btn_delet_clicked():
   entry2.delete(0, END)
   
   entry1.delete(0,END)
   return None

def btn_generate_clicked():
    Text=entry2.get()
    print("")
    return None
    
   

entry1 = Entry(
    root, 
    width = 20,
    font = ("verdana",16)
    )
entry1.pack()

entry2 = Entry(
    root,
    
    width = 20,
    font = ("verdana",16),
    
    )
entry2.pack(pady=20)



btn1= Button(
    root,
    text="generate",
    font = ("Arial bold",20),
    command=btn_generate_clicked
)
btn1.pack()

btn1= Button(
    root,
    text="delete",
    font = ("Arial bold",20),
    command=btn_delet_clicked
)

btn1.pack()





root.mainloop()


    



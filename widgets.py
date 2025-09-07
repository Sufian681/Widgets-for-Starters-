from tkinter import *
from datetime import date 
root = Tk()
root.title('Demo Window')
root.geometry('400x300')
lbl = Label(text='Hello World', fg="white", bg="blue", height=1, width=300)

name_lbl = Label(text="Full Name", bg="lightgrey")
name_entry = Entry()

def display():
    name = name_entry.get()
    message = "Welcome to the Application! \nToday is: " 
    greet = "Hello "+name+"\n"
    
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
    
text_box = Text(height=3)

btn = Button(text="Begin", command=display, height=1, bg="lightblue",
fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()

from tkinter import *

root = Tk()
root.title("Party Planner")
root.geometry("350x250")

def addGuest():
    listbox.insert(END,name.get())
    name.delete(0,END)

def removeGuest():
    index=listbox.curselection()
    if index:
        listbox.delete(index)


name = Entry(root)
name.grid(row=0,column=0,pady=10)

addButton = Button(root, text = "Add Guest", command = addGuest)
addButton.grid(row=0,column = 1)

listbox = Listbox(root,width=15,height=5,activestyle = "underline",bg='grey')
listbox.grid(row=2,column=0)

removeButton = Button(root, text="Remove Selected", command=removeGuest)
removeButton.grid(row=2,column=1)


mainloop()
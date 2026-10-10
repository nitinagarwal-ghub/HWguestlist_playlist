from tkinter import *

root = Tk()
root.title("Music Player")
root.geometry("300x300")
def change_name():
    index = listbox.get(listbox.curselection())
    if index:
        label.config(text=f"Now Playing {index}")

listbox = Listbox(root, height = 5,
                  width =25,
                  activestyle="underline")
listbox.insert(1,"Shape of you by Ed Sheeran")
listbox.insert(2,"Blinding lights by The Weeknd")
listbox.insert(3,"As it was by Harry Styles")
listbox.insert(4,"Treat you better by Shawn Mendes")
listbox.insert(5,"Flowers by Miley Cyrus")
listbox.pack()

button = Button(root, text="Play", command = change_name)
button.pack()
label = Label(root, text= "Now Playing... ")
label.pack()

mainloop()
from tkinter import *

root = Tk()
#root.geometry("500x200")

a = Entry(root)
a.pack()

def onSend():
    inputFile = open("input.txt","a")
    inputFile.write(str(a.get))
    inputFile.close()
    print("a")

window = Button(root, text="Send Message", command=onSend)
window.pack()

root.mainloop()
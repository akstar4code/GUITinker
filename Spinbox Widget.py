from tkinter import*
root = Tk()
root.title('Spinbox Widget')
root.geometry('300x400+800+80')
spin = Spinbox(root,to=10,from_=1).pack()
root.mainloop()
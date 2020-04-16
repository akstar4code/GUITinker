from tkinter import*
root = Tk()
root.title('Message Widget')
root.geometry('300x400+800+80')
var = StringVar()
msg = Message(root,text='Hello Welcome to Tkinter').pack()
root.mainloop()
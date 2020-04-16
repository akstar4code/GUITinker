from tkinter import*
root = Tk()
root.title('Frame Widget')
root.geometry('300x400')
label1 =Label(root,text = 'Hello Friends',anchor='center').place(x=100,y=200)
key0 = Button(root,text='0',width=6,height=1).place(x=90,y=175)
root.mainloop()
from tkinter import*

def add():
    _sum = str(int(e1.get())+int(e2.get()))
    left.insert(1,_sum)

panel1 = PanedWindow()
panel1.pack(fill=BOTH,expand=1)

left = Entry(panel1,bd=5)
panel1.add(left)

panel2 = PanedWindow(panel1,orient=VERTICAL)
panel1.add(panel2)

e1 = Entry(panel2)
e2 = Entry(panel2)
panel2.add(e1)
panel2.add(e2)

btn = Button(panel2,text='Sum',command=add)
panel2.add(btn)

mainloop()
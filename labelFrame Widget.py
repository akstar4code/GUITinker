from tkinter import*
window = Tk()
window.title('LabelFrame Widget')
window.geometry('500x400+800+80')
lf = LabelFrame(window,text='Hello Python GUI')
lf.pack(fill=BOTH,expand=1)
label = Label(lf,text='I am enjoying doing in python this time.....').pack()

lf2 = LabelFrame(window,text='Tkinter GUI Library')
lf2.pack(fill=BOTH,expand=1)
label2 = Label(lf2,text='Next activity to make a move and create some projects').pack()

window.mainloop()
from tkinter import*
window = Tk()
window.title('Scale Widget')
window.geometry('300x400+800+80')
def sel():
    point = 'Value of Scale'+str(var.get())
    label.config(text=point)
var = IntVar()
var2 = DoubleVar()
sc = Scale(window,orient=VERTICAL,length=300,variable = var,sliderlength=40,label='Range',repeatdelay=100,from_=0,to=50).pack()
sc2 = Scale(window,orient=HORIZONTAL,length=300,variable = var2,sliderlength=40,label='Range',repeatdelay=100,from_=0,to=80).pack()
btn = Button(window,text='Value',command = sel).pack()
label = Label(window)
label.pack()
window.mainloop()
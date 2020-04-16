from tkinter import*
window = Tk()
window.title('MenuButton Widget')
window.geometry('300x400')
mbt = Menubutton(window,text='Language',activebackground = 'Red',direction = RIGHT)
mbt.menu = Menu(mbt,tearoff = 0)
mbt['menu'] = mbt.menu
mbt.menu.add_checkbutton(label='Python3',variable = IntVar())
mbt.menu.add_checkbutton(label='Java',variable = IntVar())
mbt.pack()
window.mainloop()
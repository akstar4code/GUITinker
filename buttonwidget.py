from tkinter import*
window = Tk()
window.geometry('300x300+600+200')
window.title('Button Widget')
def key_press(x):
    print(x.char,end='')
photo = PhotoImage(file='unnamed.png').subsample(30,30)
but1 = Button(window,text='Stop',activebackground = 'pink',activeforeground = 'violet',bd=3,command = window.destroy
              ,bg='yellow',fg='green',font='Elephant',height=50,width=80,highlightcolor = 'blue',image=photo,compound = LEFT
              ,anchor = 'center',padx=10,pady = 10,relief = 'flat',state = ACTIVE)
window.bind('<Key>',lambda a:key_press(a))
but1.pack() #justify when more then one line
window.mainloop()
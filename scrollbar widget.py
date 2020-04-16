from tkinter import*
root = Tk()
root.title('Scrollbar Widget')
root.geometry('150x200+800+80')
xt = IntVar()
def sel():
    pass
sb =Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)
mylist =Listbox(root,yscrollcommand = sb.set)
for i in range(1,21):
    mylist.insert(i,'NewItem '+str(i))
mylist.pack(side=LEFT)
sb.config(command=mylist.yview)
mainloop()
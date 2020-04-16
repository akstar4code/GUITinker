from tkinter import*
root = Tk()
root.title('Text Widget')
root.geometry('400x400+800+80')
text = Text(root,wrap=WORD,spacing3=5,font=('elephant',15,'bold'),spacing2=10,spacing1=10,bd=5,relief=GROOVE
            ,selectbackground='pink',insertwidth=5,insertontime=300,insertbackground='red'
            ,exportselection=0)
text.insert(INSERT,'Name....')
text.insert(END,'Salary....')
text.tag_add('Write Here','1.0','1.4')
text.tag_add('Click Here','1.8',"1.13")

text.tag_config('Write Here',background='yellow',foreground='black')
text.tag_config('Click Here',background='black',foreground='white')

text.pack()
root.mainloop()
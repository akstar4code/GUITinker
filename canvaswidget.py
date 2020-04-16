from tkinter import*
window = Tk()
window.title('Canvas Widget')
window.geometry('300x200+300+200')
cn = Canvas(window,bg = 'red',height=200,width=200,cursor = 'exchange')
cn.create_line(0,0,110,110)
cn.create_arc((5,10,150,200),start=0,extent = 100,fill='white')
cn.create_rectangle((15,14,82,96))
cn.pack()
window.mainloop()

'''
"arrow"
"circle"
"clock"
"cross"
"dotbox"
"exchange"
"fleur"
"heart"
"heart"
"man"
"mouse"
"pirate"
"plus"
"shuttle"
"sizing"
"spider"
"spraycan"
"star"
"target"
"tcross"
"trek"
"watch"
'''
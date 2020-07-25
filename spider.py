from tkinter import *
root=Tk()
c=Canvas(height=1000,width=1000,bg='white')
c.create_oval(500,150,580,230,fill='red',tag='k')
c.create_oval(515,230,565,280,fill='red',tag='k')
c.create_oval(525,280,555,310,fill='red',tag='k')
c.create_polygon([530,230],[440,230],[440,150],[430,240],[650,240],[640,160],[640,160],[640,230],fill='black',tag='k')
c.create_polygon([530,230],[460,150],[460,80],[450,100],[450,160],[530,240],fill='black',tag='k')
c.create_polygon([560,240],[630,150],[630,100],[620,80],[620,150],[550,230],fill='black',tag='k')
c.create_polygon([525,235],[460,280],[460,360],[470,350],[470,280],[525,245],fill='black',tag='k')
c.create_polygon([555,235],[620,280],[620,360],[610,350],[610,280],[555,245],fill='black',tag='k')
c.create_polygon([520,270],[490,360],[500,370],[525,275],fill='black',tag='k')
c.create_polygon([555,275],[590,370],[600,360],[560,270],fill='black',tag='k')
c.focus_set()
c.pack()
def up(event):
    c.itemconfig(c.move('k',0,-2))
c.bind('<Up>', up)
def down(event):
    c.itemconfig(c.move('k',0,2))
c.bind('<Down>', down)
def left(event):
    c.itemconfig(c.move('k',-2,0))
c.bind('<Left>', left)
def right(event):
    c.itemconfig(c.move('k',2,0))
c.bind('<Right>', right)

oval=c.create_oval(500,800,550,850,fill='black')


root.mainloop()

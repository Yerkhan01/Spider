from tkinter import *

root = Tk()
c = Canvas(height=1000, width=1000, bg='white')

for x in [[500, 150, 580, 230], [515, 230, 565, 280], [525, 280, 555, 310]]:
    c.create_oval(x[0], x[1], x[2], x[3], fill='red', tag='k')

coords = [
    [[530, 230], [440, 230], [440, 150], [430, 240], [650, 240], [640, 160], [640, 160], [640, 230]],
    [[530, 230], [460, 150], [460, 80], [450, 100], [450, 160], [530, 240]],
    [[560, 240], [630, 150], [630, 100], [620, 80], [620, 150], [550, 230]],
    [[525, 235], [460, 280], [460, 360], [470, 350], [470, 280], [525, 245]],
    [[555, 235], [620, 280], [620, 360], [610, 350], [610, 280], [555, 245]],
    [[520, 270], [490, 360], [500, 370], [525, 275]],
    [[555, 275], [590, 370], [600, 360], [560, 270]]
]

for x in coords:
    c.create_polygon(x, fill='black', tag='k')

c.focus_set()
c.pack()


def up(event):
    c.move('k', 0, -2)


def down(event):
    c.move('k', 0, 2)


def left(event):
    c.move('k', -2, 0)


def right(event):
    c.move('k', 2, 0)


c.bind('<Up>', up)
c.bind('<Down>', down)
c.bind('<Left>', left)
c.bind('<Right>', right)
c.bind('<Escape>', lambda _: root.destroy())

oval = c.create_oval(500, 800, 550, 850, fill='black')

root.mainloop()

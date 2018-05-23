
from Tkinter import *


canvas_width = 800
canvas_height =800

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

circle = canvas.create_oval((80,91),(116,115))

#line =canvas.create_line((98,102),(128,132))
#for x in range (0, 600):
#    canvas.move(line,1, 1)
#    master.update()

def callback(event):
    print(event.x, event.y)

def radio_wave():
    x = 100
    y = 100
    t = 90
    r = 130

    canvas.create_line((x, y), (r, t), (x + 20, y + 20), smooth=True, width = 3, fill='green')
    for k in range(0,100):
        x = x + 20
        y = y + 20
        r = r - 20
        t = t + 60
        canvas.create_line((x, y), (r, t), (x + 20, y + 20), smooth=True, width = 3, fill='green')
        x = x + 20
        y = y + 20
        r = r + 60
        t = t - 20
        canvas.create_line((x, y), (r, t), (x + 20, y + 20), smooth=True, width = 3, fill='green')


canvas.bind("<Button-1>", callback)

radio_wave()
mainloop()

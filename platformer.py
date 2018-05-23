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
    t = 120
    canvas.create_line((x, 100), (x+10, t), (x + 20, 100), smooth=True)
    for k in range(0,100):
        x = x + 20
        t = t - 40
        canvas.create_line((x, 100), (x+10, t), (x + 20, 100), smooth=True)
        x = x + 20
        t = t + 40
        canvas.create_line((x, 100), (x+10, t), (x + 20, 100), smooth=True)

canvas.bind("<Button-1>", callback)

radio_wave()
mainloop()

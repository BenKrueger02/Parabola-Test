from Tkinter import *

canvas_width = 500
canvas_height =500

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

canvas.create_line((210,200),(250,400),(280,200), smooth=True)

def callback(event):
    print(event.x, event.y)

canvas.bind("<Button-1>", callback)

mainloop()

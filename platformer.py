from Tkinter import *
import random


canvas_width = 800
canvas_height =800

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height,bg = '#16316E')
canvas.pack()

##Creates upper half of stars
for c in range(0, 80):
    x = random.randint(1, 801)
    y = random.randint(1, 580)
    canvas.create_oval((x,y),(x-6,y-6), fill = "white", outline = "White")

##creates lower left half of stars
for k in range(0, 10):
    x = random.randint(1, 190)
    y = random.randint(580, 801)
    canvas.create_oval((x,y),(x-6,y-6), fill = "white", outline = "White")

##creates lower right half of stars
for q in range(0, 10):
    x = random.randint(605, 801)
    y = random.randint(580, 801)
    canvas.create_oval((x,y),(x-6,y-6), fill = "white", outline = "White")


##Creates the Satelite
def create_satelite():
    ##Left Solar panel
    y= 88
    x=316
    ##Lines on Solar Panel
    canvas.create_rectangle((300,88),(380,152), fill="#4863A0", width = 3)
    for j in range(0,5):
        canvas.create_line((x,88),(x,152))
        x = x+16

    for i in range(0,4):
        canvas.create_line((300, y), (380, y))
        y = y + 16

    ##Body of Satelite
    canvas.create_rectangle((380, 96), (436, 144), fill="Gray", width=3)

    ##Right solar Panel
    y = 88
    x = 452
    canvas.create_rectangle((436, 88), (516, 152), fill="#4863A0", width=3)
    ##Lines on Solar Panel
    for b in range(0, 5):
        canvas.create_line((x, 88), (x, 152))
        x = x + 16

    for a in range(0, 4):
        canvas.create_line((436, y), (516, y))
        y = y + 16

    ##Lower Part (Satelite Dish)
    canvas.create_line((408,144),(408,188),width=3)

    canvas.create_line((397.6,229.6),(389.6,173.6), (453.6,173.6),width=3,smooth=True)
    canvas.create_line((410,190),(153.6,205.6), width=3)
    canvas.create_oval((149.6,201.6),(157.6,209.6), fill="Black")

##Makes the Satelite Dish
def create_satelite_dish(width):
    if width == "narrow":
        canvas.create_line((266,500),(960,960),(680,480), smooth=True, width=5,fill = 'gray')
        canvas.create_line((561.6,561.6),(770.4,770.4),width=5,fill='gray')
        canvas.create_oval((580, 580),(540, 540),width=5,fill='gray', outline="Gray")
    if width == "wide":
        canvas.create_line((199, 600), (400, 900), (601, 600), smooth=True, width=5, fill='gray')
        canvas.create_line((400, 750), (400, 682.66), width=5, fill='gray')
        canvas.create_oval((380, 662.66), (420, 702.66), width=5, fill='gray', outline="Gray")
    if width == "straight":
        canvas.create_line((336, 760),(760, 336), width=5, fill='gray')
        canvas.create_line((460, 460), (548, 548), width=5, fill='gray')
        canvas.create_oval((480, 480), (440, 440), width=5, fill='gray', outline="Gray")

def callback(event):
    print(event.x, event.y)

def radio_wave():
    x = 155
    y = 210
    t = 200
    r = 185

    canvas.create_line((x, y), (r, t), (x + 20, y + 20), smooth=True, width = 3, fill='green')
    for k in range(0,12):
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

create_satelite_dish("wide")
create_satelite()
radio_wave()
mainloop()
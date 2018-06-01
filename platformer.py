from Tkinter import *
import random



canvas_width = 800
canvas_height =800

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height,bg = '#16316E')
canvas.pack()

##Creates upper half of stars
def create_stars():
    for c in range(0, 80):
        x = random.randint(1, 801)
        y = random.randint(1, 580)
        canvas.create_oval((x,y),(x-6,y-6), fill = "white", outline = "White")

    ##creates lower left half of stars
    for k in range(0, 10):
        x = random.randint(1, 190)
        y = random.randint(580, 801)
        canvas.create_oval((x,y),(x-6,y-6), fill = "white", outline = "White")


def create_buttons():
    canvas.create_rectangle((630,670),(690,731),fill = '#00C5FF',outline='#16316E')
    ninety = Label(text = "Next", font=('Bodoni',45),bg="#2874A6", borderwidth=1)
    ninety.pack()
    ninety.place(x=690,y=671)


##Creates the Satelite
def create_satelite(w,z):
    ##Left Solar panel
    ##For the 90 degree position, use w=0
    y= 88
    x=176+w
    ##Lines on Solar Panel
    canvas.create_rectangle((160+w,88),(240+w,152), fill="#4863A0", width = 3)
    for j in range(0,5):
        canvas.create_line((x,88),(x,152))
        x = x+16

    for i in range(0,4):
        canvas.create_line((160+w, y), (240+w, y))
        y = y + 16

    ##Body of Satelite
    canvas.create_rectangle((240+w, 96), (296+w, 144), fill="Gray", width=3)

    ##Right solar Panel
    y = 88
    x = 312+w
    canvas.create_rectangle((296+w, 88), (376+w, 152), fill="#4863A0", width=3)
    ##Lines on Solar Panel
    for b in range(0, 5):
        canvas.create_line((x, 88), (x, 152))
        x = x + 16

    for a in range(0, 4):
        canvas.create_line((296+w, y), (376+w, y))
        y = y + 16

    ##Lower Part (Satelite Dish)
    canvas.create_line((268+w,144),(268+w,182),width=3)
    canvas.create_line((218+w,200),(268+w,160), (318+w,200),width=3,smooth=True)
    canvas.create_line((268+w,182),(268+w,218-z), width=3)
    canvas.create_oval((264+w,214-z),(272+w,222-z), fill="Black")

##Makes the Satelite Dish
def create_satelite_dish():
    canvas.create_line((199, 600), (400, 900), (601, 600), smooth=True, width=5, fill='gray')
    canvas.create_line((400, 750), (400, 682.66), width=5, fill='gray')
    canvas.create_oval((380, 662.66), (420, 702.66), width=5, fill='gray', outline="Gray")


def callback(event):
    global counter
    print(event.x, event.y)
    if (event.x < 690 and event.x > 630) and (event.y < 730 and event.y > 670):
        counter += 1
        if counter >= 3:
            counter = 0
        if counter == 0:
            move_satilite(0,0)
        if counter == 1:
            print('Hello_1')
            move_satilite(132,0)
        if counter == 2:
            print('Hello_2')
            move_satilite(192,5)


def radio_wave(counter):
    if counter == 0:
        x = 268
        y = 218
        t = 225.5
        r = 288

        canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width = 3, fill='green')
        for k in range(0,15):
            y = y + 15
            r = r - 40
            t = t + 15
            canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width = 3, fill='green')
            y = y + 15
            r = r + 40
            t = t + 15
            canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width = 3, fill='green')

        x = 268
        y = 686
        r = 275.5
        t = 666

        canvas.create_line((x, y), (r, t), (x + 15, y), smooth=True, width = 3, fill='green')
        for k in range(0,4):
            x = x + 15
            r = r + 15
            t = t + 40
            canvas.create_line((x, y), (r, t), (x + 15, y), smooth=True, width = 3, fill='green')
            x = x + 15
            r = r + 15
            t = t - 40
            canvas.create_line((x, y), (r, t), (x + 15, y), smooth=True, width = 3, fill='green')

    if counter == 1:
        x = 400
        y = 218
        t = 225.5
        r = 420

        canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')
        for k in range(0, 15):
            y = y + 15
            r = r - 40
            t = t + 15
            canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')
            y = y + 15
            r = r + 40
            t = t + 15
            canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')

    if counter == 2:
        x = 460
        y = 213
        r = 440
        t = 220.5


        canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')
        for k in range(0, 17):
            y = y + 15
            r = r + 40
            t = t + 15
            canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')
            if k==17:
                print("Hi")
            else:
                y = y + 15
                r = r - 40
                t = t + 15
                canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')

        x = 460
        y = 738
        r = 467.5
        t = 715.5

        canvas.create_line((x, y), (r, t), (x - 15, y - 15), smooth=True, width=3, fill='green')
        for k in range(0, 2):
            x = x - 15
            y = y - 15
            r = r - 45
            t = t + 15
            canvas.create_line((x, y), (r, t), (x - 15, y - 15), smooth=True, width=3, fill='green')
            if k==1:
                print("Hi")
            else:
                x = x - 15
                y = y - 15
                r = r + 15
                t = t - 45
                canvas.create_line((x, y), (r, t), (x - 15, y - 15), smooth=True, width=3, fill='green')


canvas.bind("<Button-1>", callback)
global counter
counter=0

def move_satilite(w,z):
    canvas.create_rectangle((0, 0), (800, 800), fill='#16316E')
    create_stars()
    create_satelite(w,z)
    create_buttons()
    create_satelite_dish()
    radio_wave(counter)


move_satilite(0,0)
mainloop()
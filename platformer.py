from Tkinter import *

canvas_width = 1000
canvas_height =1000

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height,bg = '#16316E')
canvas.pack()

##Creates the Satelite
def create_satelite():
    ##Left Solar panel
    y= 110
    x=50
    ##Lines on Solar Panel
    canvas.create_rectangle((30,110),(130,190), fill="#4863A0", width = 3)
    for j in range(0,5):
        canvas.create_line((x,110),(x,190))
        x = x+20

    for i in range(0,4):
        canvas.create_line((30, y), (130, y))
        y = y + 20

    ##Body of Satelite
    canvas.create_rectangle((130, 120), (200, 180), fill="Gray", width=3)

    ##Right solar Panel
    y = 110
    x = 200
    canvas.create_rectangle((200, 110), (300, 190), fill="#4863A0", width=3)
    ##Lines on Solar Panel
    for b in range(0, 5):
        canvas.create_line((x, 110), (x, 190))
        x = x + 20

    for a in range(0, 4):
        canvas.create_line((200, y), (300, y))
        y = y + 20

    ##Lower Part (Satelite Dish)
    canvas.create_line((165,180),(165,235),width=3)
    canvas.create_line((152,287),(142,217), (222,217),width=3,smooth=True)
    canvas.create_line((165,235),(192,257), width=3)
    canvas.create_oval((187,252),(197,262), fill="Black")

##Makes the Satelite Dish
def create_satelite_dish(width):
    if width == "narrow":
        canvas.create_line((600,850),(1200,1200),(850,600), smooth=True, width=5,fill = 'gray')
        canvas.create_line((702,702),(963,963),width=5,fill='gray')
        canvas.create_oval((725, 725),(675, 675),width=5,fill='gray', outline="Gray")
    if width == "wide":
        canvas.create_line((546, 876), (876, 876), (876, 546), smooth=True, width=5, fill='gray')
        canvas.create_line((575, 575), (795, 795), width=5, fill='gray')
        canvas.create_oval((600, 600), (550, 550), width=5, fill='gray', outline="Gray")
    if width == "straight":
        canvas.create_line((420, 950),(950, 420), width=5, fill='gray')
        canvas.create_line((575, 575), (685, 685), width=5, fill='gray')
        canvas.create_oval((600, 600), (550, 550), width=5, fill='gray', outline="Gray")

def callback(event):
    print(event.x, event.y)

canvas.bind("<Button-1>", callback)

create_satelite_dish("wide")
create_satelite()

mainloop()

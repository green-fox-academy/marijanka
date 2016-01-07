from tkinter import *
from ball import Ball

master = Tk()

canvas = Canvas(master, width= 400, height= 400)
canvas.pack()
canvas.create_rectangle(0, 0, 400, 400, fill= '#ffffff')
ball= Ball(200, 250 ,20)
bbox = ball.get_bbox()
canvas.create_oval(bbox, fill = '#000000')
mainloop()

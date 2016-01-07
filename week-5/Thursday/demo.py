from tkinter import *

master = Tk()

w = Canvas(master, width= 400, height= 300)

w.pack()

y = 0

for i in range(8):
    if i % 2 == 0:
        x = 0
        for n in range(4):
            w.create_rectangle(x, y, x+20, y+20, fill='#000000')
            x += 40
        y += 20
    else:
        x = 20
        for n in range(4):
            w.create_rectangle(x, y, x+20, y+20, fill='#000000')
            x += 40
        y += 20

mainloop()

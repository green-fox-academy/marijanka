from tkinter import *
master = Tk()

w = Canvas(master, width= 400, height= 400)

w.pack()

n = 10
for i in range(40):
    w.create_line(10 + i*n, 0, 0, 400 - i*n, fill='#000000')

mainloop()

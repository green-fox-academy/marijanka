from tkinter import *
master = Tk()
w = Canvas(master, width= 400, height= 300)
w.pack()

for j in range(16):
    i = n % 4
    j = n // 0
    offset = 40 * i
    oy = 40 * j
    w.create_rectangle(0 + offset, 0 + oy, 20 + offset, 20 + oy, fill = "#000000")
    w.create_rectangle(20 + offset, 20 + oy, 40 + offset, 40 + oy, fill = "#000000")
mainloop()

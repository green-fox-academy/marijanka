from tkinter import *
master = Tk()

w = Canvas(master, width= 400, height= 400)

w.pack()

w.create_line(200, 0, 200, 200, fill='#000000')
w.create_line(113.4, 50, 286.6, 150, fill='#000000')
w.create_line(113.4, 150, 286.6, 50, fill='#000000')

n = 10

for i in range(10):
    w.create_line(200 + i * ((0.75 * (n ** 2)) ** 0.5), 100 - i * (n/2), 200, 0 + i*n, fill='#000000')
    w.create_line(200 - i * ((0.75 * (n ** 2)) ** 0.5), 100 - i * (n/2), 200, 0 + i*n, fill='#000000')
    w.create_line(200 + i * ((0.75 * (n ** 2)) ** 0.5), 100 + i * (n/2), 200, 200 - i*n, fill='#000000')
    w.create_line(200 - i * ((0.75 * (n ** 2)) ** 0.5), 100 + i * (n/2), 200, 200 - i*n, fill='#000000')
    w.create_line(200 + i * ((0.75 * (n ** 2)) ** 0.5), 100 - i * (n/2), 286.6 - i * ((0.75 * (n ** 2)) ** 0.5), 150 - i * (n/2), fill='#000000')
    w.create_line(200 - i * ((0.75 * (n ** 2)) ** 0.5), 100 - i * (n/2), 113.4 + i * ((0.75 * (n ** 2)) ** 0.5), 150 -i * (n/2), fill='#000000')


mainloop()

from tkinter import *
master = Tk()

w = Canvas(master, width= 600, height= 600)

w.pack()

w.create_line(300, 0, 300, 600, fill='#000000')
w.create_line(40.2, 150, 559.8, 450, fill='#000000')
w.create_line(40.2, 450, 559.8, 150, fill='#000000')

n = 10

for i in range(30):
    w.create_line(300 + i * ((0.75 * (n ** 2)) ** 0.5), 300 - i * (n/2), 300, 0 + i*n, fill='#000000')
    w.create_line(300 - i * ((0.75 * (n ** 2)) ** 0.5), 300 - i * (n/2), 300, 0 + i*n, fill='#000000')
    w.create_line(300 + i * ((0.75 * (n ** 2)) ** 0.5), 300 + i * (n/2), 300, 600 - i*n, fill='#000000')
    w.create_line(300 - i * ((0.75 * (n ** 2)) ** 0.5), 300 + i * (n/2), 300, 600 - i*n, fill='#000000')
    w.create_line(300 + i * ((0.75 * (n ** 2)) ** 0.5), 300 - i * (n/2), 559.8 - i * ((0.75 * (n ** 2)) ** 0.5), 450 - i * (n/2), fill='#000000')
    w.create_line(300 - i * ((0.75 * (n ** 2)) ** 0.5), 300 - i * (n/2), 40.2 + i * ((0.75 * (n ** 2)) ** 0.5), 450 -i * (n/2), fill='#000000')


mainloop()

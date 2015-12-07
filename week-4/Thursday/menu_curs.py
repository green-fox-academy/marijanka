import unicurses
import todo
import main
screen = unicurses.initscr()
screen.keypad(1)
dims = screen.getmaxyx()

def menu():
    screen.nodelay(0)
    screen.clear()
    selection = -1
    option = 0
    while selection < 0:
        graphics = [0]*5
        graphics[option] = curses.A_REVERSE
        screen.addstr(0, dims[1]/2-3, "Menu")
        screen.addstr(dims[0]/2-2, dims[1]/2-2, "Sth", graphics[0])
        screen.addstr(dims[0]/2-1, dims[1]/2-6, "Instructions", graphics[1])
        screen.addstr(dims[0]/2, dims[1]/2-6, "Aby", graphics[2])
        screen.addstr(dims[0]/2+1, dims[1]/2-5, "adasf", graphics[3])
        screen.addstr(dims[0]/2+2, dims[1]/2-2, "Exit", graphics[4])
        screen.refresh()
        action = screen.getch()
        if action == curses.Key_UP:
            option = (option - 1) % 5
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 5
menu()
unicurses.edwin()

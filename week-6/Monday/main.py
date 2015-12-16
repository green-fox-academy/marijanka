from menu import *
import new_game

def main_menu():
     items = [
       MenuItem("1", "New Game", main_create_player),
       MenuItem("2", "Load Game", ''),
       MenuItem("0", "Exit", exit)
     ]
     return Menu(items)

def new_game_submenu():
    items = [
        MenuItem("1", "Reenter name", main_create_player),
        MenuItem("2", "Continue", main_continue_game),
        MenuItem("3", "Save", ''),
        MenuItem("0", "Quit", main_quit_submenu)
    ]
    return Menu(items)

def quit_submenu():
    items = [
        MenuItem("1", "Resume", ''),
        MenuItem("2", "Save and Quit", ''),
        MenuItem("0", "Quit without Save", exit)
    ]
    return Menu(items)

def continue_submenu():
    items = [
        MenuItem("1", "Reroll stats", main_continue_game),
        MenuItem("2", "Continue", main_select_potion),
        MenuItem("3", "Save", ''),
        MenuItem("0", "Quit", main_quit_submenu)
    ]
    return Menu(items)

def select_potion_submenu():
    items = [
        MenuItem("1", "Életerő főzet", main_potion_1),
        MenuItem("2", "Ügyesség főzet", main_potion_2),
        MenuItem("3", "Szerencse főzet", main_potion_3)
    ]
    return Menu(items)

def choose_potion_submenu():
    items = [
        MenuItem("1", "Reselect the Potion", main_select_potion),
        MenuItem("2", "Continue", main_begin_submenu),
        MenuItem("0", "Quit", main_quit_submenu)
    ]
    return Menu(items)

def begin_submenu():
    items = [
        MenuItem("1", "Begin", ''),
        MenuItem("2", "Save", ''),
        MenuItem("0", "Quit", main_quit_submenu)
    ]
    return Menu(items)

def main_main_menu():
    menu = main_menu()
    exception(menu)

def get_user_name():
    user_name = input('Please give your name(min. 4 character): ')
    print(user_name)
    if len(user_name) < 4:
        get_user_name()
    return user_name

def main_create_player():
    new_game.user.name = get_user_name()
    menu = new_game_submenu()
    exception(menu)

def main_quit_submenu():
    menu = quit_submenu()
    exception(menu)

def main_continue_game():
    new_game.roll_stats()
    menu = continue_submenu()
    exception(menu)

def main_select_potion():
    print('\n' + 'Válassz egy főzetet, amivel a játék során visszatérhetsz az alppontszámodra: ' + '\n')
    menu = select_potion_submenu()
    exception(menu)

def main_potion_1():
    new_game.user.inventory['potion'] = 1
    print('\n' + 'Életerő főzetet válsztottál.' + '\n')
    main_choose_potion()

def main_potion_2():
    new_game.user.inventory['potion'] = 2
    print('\n' + 'Ügyesség főzetet választottál.' + '\n')
    main_choose_potion()

def main_potion_3():
    new_game.user.inventory['potion'] = 3
    print('\n' + 'Szerencse főzetet választottál.' + '\n')
    main_choose_potion()

def main_choose_potion():
    menu = choose_potion_submenu()
    exception(menu)

def main_begin_submenu():
    new_game.character_stats()
    menu = begin_submenu()
    exception(menu)

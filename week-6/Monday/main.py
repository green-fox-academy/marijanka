from menu import *
import new_game
from exception import PocsolyszeError
from fight import *

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

PocsolyszeError()
def pocsolyszerror():
    raise PocsolyszeError

def quit_submenu():
    items = [
        MenuItem("1", "Resume", pocsolyszerror),
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
        MenuItem("1", "Health Potion", main_potion_1),
        MenuItem("2", "Dexterity Potion", main_potion_2),
        MenuItem("3", "Luck Potion", main_potion_3)
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
        MenuItem("1", "Begin", main_test_fight),
        MenuItem("2", "Save", ''),
        MenuItem("0", "Quit", main_quit_submenu)
    ]
    return Menu(items)

def test_fight():
    items = [
        MenuItem("1", "Strike", main_strike),
        MenuItem("2", "Retreat", ''),
        MenuItem("0", "Quit", main_quit_submenu)
    ]
    return Menu(items)

def after_strike():
    items = [
        MenuItem("1", "Continue", main_after_strike),
        MenuItem("2", "Try your luck", main_try_luck),
        MenuItem("3", "Retreat", ''),
        MenuItem("0", "Quit", main_quit_submenu)
    ]
    return Menu(items)

def main_main_menu():
    menu = main_menu()
    exception(menu)

def get_user_name():
    user_name = input('Please give your name(min. 4 character): ')
    print('\n', user_name, '\n')
    if len(user_name) < 4:
        get_user_name()
    return user_name

def main_create_player():
    new_game.user.name = get_user_name()
    menu = new_game_submenu()
    return menu

def main_quit_submenu():
    menu = quit_submenu()
    return menu

def main_continue_game():
    new_game.user.roll_stats()
    new_game.user.display_roll_stats()
    menu = continue_submenu()
    return menu

def main_select_potion():
    print('\n' + 'Choose a potion: ' + '\n')
    menu = select_potion_submenu()
    return menu

def main_potion_1():
    new_game.user.inventory['potion'] = 'Health potion'
    print('\n' + 'Your choice is health potion.' + '\n')
    return main_choose_potion()

def main_potion_2():
    new_game.user.inventory['potion'] = 'Dexterity potion'
    print('\n' + 'Your choice is dexterity potion.' + '\n')
    return main_choose_potion()

def main_potion_3():
    new_game.user.inventory['potion'] = 'Luck potion'
    print('\n' + 'Your choice is luck potion.' + '\n')
    return main_choose_potion()

def main_choose_potion():
    menu = choose_potion_submenu()
    return menu

def main_begin_submenu():
    new_game.user.display_roll_stats()
    new_game.user.character_stats()
    menu = begin_submenu()
    return menu

def main_test_fight():
    print('Test your Sword in a test fight')
    new_game.monster.get_name()
    new_game.monster.roll_stats()
    new_game.monster.display_roll_stats()
    menu = test_fight()
    return menu

def main_strike():
    game.strike()
    menu = after_strike()
    return menu

def main_after_strike():
    game.after_strike()
    menu = test_fight()
    return menu

def main_try_luck():
    game.try_luck()
    menu = test_fight()
    return menu

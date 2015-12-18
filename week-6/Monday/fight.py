from new_game import *

class Game:
    def strike(self):
        self.user_fight = user.game_dice()
        self.monster_fight =  monster.game_dice()
        if self.user_fight >= self.user_fight :
            print('You hit the monster.','\n')
        elif self.user_fight < self.user_fight :
            print('You hit the monster.','\n')

    def after_strike(self):
        if self.user_fight > self.monster_fight:
            monster.stats['Health'] -= 2
            monster.display_roll_stats()
        else:
            user.stats['Health'] -= 2
            user.display_roll_stats()

    def try_luck(self):
        roll_dice = user.dice() + user.dice()
        if self.user_fight < self.monster_fight:
            if roll_dice < user.stats['Luck']:
                user.stats['Health'] -= 3
            else:
                user.stats['Health'] -= 1
                user.stats['Luck'] -= 1
        else:
            if roll_dice < user.stats['Luck']:
                user.stats['Health'] -= 1
            else:
                user.stats['Health'] -= 4
                user.stats['Luck'] -= 1
        user.display_roll_stats()

game = Game()

import threading
import time
import random


class MegaGodzilla(threading.Thread):
    ###
    # You have to complete this class (locks will be a needed)
    ###

    def __init__(self, hp):
        super().__init__()
        self.hp = hp

    @property
    def alive(self):
        if self.hp > 0:
            return True
        return False

    ###
    # You have to develop the run method
    ###

    def attacked(self, soldier):
        self.hp -= soldier.attack
        if not self.alive:
            print('MegaGodzilla has died!!')
        else:
            print(
                'Mega-Godzilla has been attacked! The soldier has caused'
                ' damage ' + str(soldier.attack) + '. HP Godzilla '
                + str(self.hp))
            soldier.attacked(int(soldier.attack / 4))

            ###
            # You have to develop the attack method
            ###


class Soldier(threading.Thread):
    ###
    # You have to complete this class (locks will be needed)
    ###

    def __init__(self, MegaGodzilla, velocity, hp, attack):
        super().__init__()
        self.MegaGodzilla = MegaGodzilla
        self.velocity = velocity
        self.hp = hp
        self.ID = next(Soldier.get_i)
        self.attack = attack

    @property
    def alive(self):
        if self.hp > 0:
            return True
        return False

    ###
    # You have to develop the run method
    ###

    def attacked(self, attack):
        self.hp -= attack
        print('The soldier' + str(self.ID) +
              ' has been damaged!!  HP ' + str(self.hp))
        if not self.alive:
            print('The soldier' + str(self.ID) + ' has died :( !!!')

    def id_():
        i = 0
        while True:
            yield i
            i += 1

    get_i = id_()


if __name__ == '__main__':
    print('Starting simulation!')

    ###
    # You have to develop the main
    ###

import threading
import time
import random


class Godzilla(threading.Thread):
    def __init__(self, hp):
        super().__init__()
        self.hp = hp
        self.alive = True

    ###
    # You have to develop the run method
    ###

    def attacked(self, soldier):
        self.hp -= soldier.attack
        if self.hp <= 0:
            self.alive = False
            print('Godzilla has died!!')
            self.terminate()
        else:
            print(
                'Godzilla has been attacked!' + soldier.type +
                ' has caused damage ' + str(soldier.attack) +
                '. HP Godzilla ' + str(self.hp))
            soldier.attacked(int(soldier.attack / 4))

            ###
            # You have to develop the attack method
            ###


class Soldier(threading.Thread):
    def __init__(self, Godzilla, velocity, hp, attack):
        super().__init__()
        self.alive = True
        self.Godzilla = Godzilla
        self.velocity = velocity
        self.hp = hp
        self.ID = next(Soldier.get_i)
        self.attack = attack

    ###
    # You have to develop the run method
    ###

    def attacked(self, attack):
        self.hp -= attack
        print('The soldier' + str(self.ID) + ' has been damaged!! HP ' + str(
            self.hp))
        if self.hp <= 0:
            self.alive = False
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
    # You have to develop this main
    ###

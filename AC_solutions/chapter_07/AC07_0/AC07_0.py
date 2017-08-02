import threading
import time
import random


class Godzilla(threading.Thread):

    def __init__(self, hp):
        super().__init__()
        self.hp = hp
        self.alive = True

    def run(self):
        while self.hp > 0 and self.alive is True:
            time.sleep(8)
            if self.alive is True:  # Godzilla can die while he is waiting
                self.attack()
        print('The simulation has finished')


    def attacked(self, soldier):
        self.hp -= soldier.attack
        if self.hp <= 0:
            self.alive = False
            print('Godzilla has died!!')
        else:
            print(
                'Godzilla has been attacked! The soldier has caused damage '
                + str(soldier.attack) + '. HP Godzilla ' + str(self.hp))
            soldier.attacked(int(soldier.attack / 4))
    
    def attack(self):
        for i in soldiers_list:
            if i.alive is True:
                i.attacked(3)


class Soldier(threading.Thread):

    def __init__(self, Godzilla, velocity, hp, attack):
        super().__init__()
        self.alive = True
        self.Godzilla = Godzilla
        self.velocity = velocity
        self.hp = hp
        self.ID = next(Soldier.get_i)
        self.attack = attack


    def run(self):
        while self.hp > 0 and Godzilla.alive is True:
            time.sleep(self.velocity)
            if Godzilla.alive is True:
                # Godzilla can die while he is waiting
                Godzilla.attacked(self)
    

    def attacked(self, attack):
        self.hp -= attack
        print('The soldier' + str(self.ID) + ' has been damaged!! HP ' 
            + str(self.hp))
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

    num_soldiers = 20  # int(input('How many soldiers do you want?'))
    soldiers_list = []
    Godzilla = Godzilla(1000)
    Godzilla.start()
    for i in range(num_soldiers):
        soldier = Soldier(Godzilla, random.randint(4, 20), 60, 30)
        soldier.setDaemon(True)
        soldier.start()
        soldiers_list.append(soldier)


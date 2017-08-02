import threading
import time
import random


class MegaGodzilla(threading.Thread):

    lockgod = threading.Lock()

    def __init__(self, hp):
        super().__init__()
        self.hp = hp
        self.scream = False

    @property
    def alive(self):
        if self.hp > 0:
            return True
        return False

    def run(self):
        while self.hp > 0 and self.alive:
            attack_time = random.randint(3, 6)
            time.sleep(attack_time)
            if self.alive:
                attack_type = random.randint(0, 1)
                if attack_type == 0 or self.scream:
                    # Godzilla can die while he is waiting
                    self.attack(3)
                elif attack_type == 1 and not self.scream:
                    self.scream = True
                    print('MEGA-GODZILLA: 1 , 2 ,3 frozen!!!')
                    self.changestatus()
                    self.attack(6)

        print('The simulation has finished')


    def attacked(self, soldier):
        self.hp -= soldier.attack
        if not self.alive:
            print('MegaGodzilla has died!!')
        else:
            print('Mega-Godzilla has been attacked! The soldier has'
                  'caused damage' + str(soldier.attack) + 
                  '. HP Godzilla ' + str(self.hp))
            soldier.attacked(int(soldier.attack / 4))

    def changestatus(self, status=False):
        for i in soldiers_list:
            if i.alive:
                i.status = status
        if status:
            self.scream = False

    def attack(self, damage):
        for i in soldiers_list:
            if i.alive:
                i.attacked(damage)


class Soldier(threading.Thread):

    locksold = threading.Lock()
    lockattack = threading.Lock()

    def __init__(self, MegaGodzilla, velocity, hp, attack):
        super().__init__()
        self.MegaGodzilla = MegaGodzilla
        self.velocity = velocity
        self.hp = hp
        self.status = True
        self.ID = next(Soldier.get_i)
        self.attack = attack
        self.attacktime = random.randint(1, 3)

    @property
    def alive(self):
        if self.hp > 0:
            return True
        return False

    def run(self):
        while self.hp > 0 and MegaGodzilla.alive:
            time.sleep(self.velocity)
            Soldier.locksold.acquire()
            if not self.status:
                time.sleep(10)
                print('WE CAN CONTINUE!!')
                MegaGodzilla.changestatus(status=True)
            if MegaGodzilla.alive:
                Soldier.lockattack.acquire()
                MegaGodzilla.attacked(self)
                time.sleep(self.attacktime)
                Soldier.lockattack.release()
            Soldier.locksold.release()


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

    num_soldiers = 20  # int(input('How many soldiers do you want?'))
    soldiers_list = []
    MegaGodzilla = MegaGodzilla(1000)
    MegaGodzilla.start()
    for i in range(num_soldiers):
        soldier = Soldier(MegaGodzilla, random.randint(4, 20), 60, 30)
        soldier.setDaemon(True)
        soldier.start()
        soldiers_list.append(soldier)

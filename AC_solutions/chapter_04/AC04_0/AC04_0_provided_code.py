from AC04_0 import *
from random import *

programmers = ['Belen', 'Patricio', 'Jaime', 'Marco', 'Bastian',
               'Antonio', 'Ivania', 'Felipe', 'Matias', 'Carlos',
               'Ariel', 'Francisco', 'Francisca', 'Iacopo', 'Enrique',
               'Patricio', 'Vicente', 'Rodolfo', 'Eduardo', 'Diego',
               'Guillermo', 'Fernando', 'Karim', 'Juan', 'Nicolas',
               'Christian']


class Robot(metaclass=MetaRobot):
    def __init__(self, creators, initial):
        self.creators = creators
        self.actual = initial

    def Verify(self):
        if self.actual.hacker:
            return True
        return False


class Port:
    def __init__(self, ide, hacker):
        self.hacker = hacker
        self.ide = ide

    """
    The hacker attribute is an integer that behaves like a boolean,
    yes, in Python bool is a subclass of int

    """


if __name__ == '__main__':
    ports = {}
    for i in range(10):
        ports[i] = Port(i, randint(0, 1))
    robocop = Robot(programmers, ports[0])
    robocop.check_creator()
    robocop.change_node(ports[randint(0, 9)])
    robocop.disconnect()

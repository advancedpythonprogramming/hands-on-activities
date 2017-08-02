from abc import ABCMeta, abstractmethod, abstractproperty
from math import pi, sqrt, cos, sin, asin


def calculate_points(trasl, radius, angles):
    points = []
    for k in angles:
        """
        Here we are assuming that aux_list has the same dimension
        than the argument trasl.
        """
        aux_list = [radius * cos(k), radius * sin(k)]
        for i in range(len(aux_list)):
            aux_list[i] += trasl[i]
        points.append(aux_list)
    return points


class Figure(metaclass=ABCMeta):
    def __init__(self, center):
        self._center = center

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        self._center = value

    @abstractproperty
    def perimeter(self):
        pass

    @abstractproperty
    def area(self):
        pass

    @abstractmethod
    def grow_area(self, times):
        pass

    @abstractmethod
    def grow_perimeter(self, amount):
        pass

    def translate(self, vector):
        """
        A better implementation to this method is as follows:
        self.center = tuple(map(lambda x, y: x + y, self.center,
                        vector))

        We refer the reader to Chapter 3 - Functional Programming
        for more details about map and lambda functions.
        """
        if len(vector) == len(self.center):
            for i in range(len(vector)):
                self.center[i] += vector[i]
        else:
            print('Wrong vector size')
            return

    def __repr__(self):
        return '{} - Perimeter: {:.2f}, Area: {:.2f}, Center: {}' \
            .format(type(self).__name__,
                    self.perimeter, self.area, self.center)

    # Properties useful to implement the property vertices
    # This is one possible solution
    @abstractproperty
    def dist_center_vertex(self):
        pass

    @abstractproperty
    def angles(self):
        pass

    @property
    def vertices(self):
        return calculate_points(
            self.center, self.dist_center_vertex, self.angles)


class Rectangle(Figure):
    def __init__(self, a, b, center):
        super().__init__(center)
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    @property
    def perimeter(self):
        return 2 * (self._a + self._b)

    @property
    def area(self):
        return self._a * self._b

    def grow_area(self, times):
        self._a *= sqrt(times)
        self._b *= sqrt(times)

    def grow_perimeter(self, amount):
        self._a += self._a * amount / (2 * (self._a + self._b))
        self._b += self._b * amount / (2 * (self._a + self._b))

    # Properties useful for the vertices property
    @property
    def dist_center_vertex(self):
        return sqrt(self.a ** 2 + self.b ** 2) / 2

    @property
    def angles(self):
        angles = list()
        angles.append(2 * asin(self.b /
                               (2 * self.dist_center_vertex)))
        angles.append(pi)
        angles.append(pi + 2 * asin(self.b /
                                    (2 * self.dist_center_vertex)))
        angles.append(0)
        return angles


class EquilateralTriangle(Figure):
    def __init__(self, l, center):
        super().__init__(center)
        self._l = l

    @property
    def l(self):
        return self._l

    @l.setter
    def l(self, value):
        self._l = value

    @property
    def perimeter(self):
        return 3 * self._l

    @property
    def area(self):
        return (self._l ** 2) * sqrt(3) / 4

    def grow_area(self, times):
        self._l *= sqrt(times)

    def grow_perimeter(self, amount):
        self._l *= amount / 3

    # Properties useful for implementing the vertices property
    @property
    def dist_center_vertex(self):
        return self.l / sqrt(3)

    @property
    def angles(self):
        angles = list()
        angles.append(2 * pi / 3)
        angles.append(4 * pi / 3)
        angles.append(0)
        return angles


# Testing the solution

if __name__ == '__main__':
    figures = list()
    figures.append(EquilateralTriangle(5, [0, 0]))
    figures.append(Rectangle(6, 8, [0, 0]))

    print(*figures, sep="\n")
    print("*" * 20)

    for i in figures:
        i.grow_perimeter(0)

    print(*figures, sep="\n")
    print("*" * 20)

    for i in figures:
        i.grow_area(1)

    print(*figures, sep="\n")
    print("*" * 20)

    print("Before translating")
    for i in figures:
        print(i.vertices)
    print("*" * 20)

    print("After translating")
    for i in figures:
        i.translate((2, -1))
        print(i.vertices)
    print("*" * 20)

    print(*figures, sep="\n")
    print("*" * 20)

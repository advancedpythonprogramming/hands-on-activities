class Hamburger:
    def __init__(self, high, diameter, meat_quantity):
        self.high = high
        self.diameter = diameter
        self.meat_quantity = meat_quantity

    def __repr__(self):
        return ('Hamburger {0} cms high, '
                '{1} cm of diameter and '
                '{2} meat quantity').format(self.high, self.diameter,
                                            self.meat_quantity)


def price_after_tax(price_before_tax):
    return (price_before_tax * 1.19 + 100)


if __name__ == "__main__":
    hamburger1 = Hamburger(10, 15, 2)
    hamburger2 = Hamburger(7, 10, 3)
    hamburger3 = Hamburger(10, 9, 2)

    print(hamburger2 > hamburger1)
    print(hamburger2 == hamburger3)
    print(hamburger1 < hamburger3)

    print(Hamburger.instances)
    hamburger4 = Hamburger(12, 20, 4)
    print(Hamburger.instances)
    print(price_after_tax(2000))

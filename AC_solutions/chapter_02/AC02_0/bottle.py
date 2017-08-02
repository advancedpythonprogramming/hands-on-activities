class Bottle:
    def __init__(self, liters=1):
        self.liters = liters

    @property
    def label(self):
        return "DCC-Cola"

    def beber(self):
        print("Delicious soda {}".format(self.label))

    def __str__(self):
        return "{} liters of {}.".format(self.label, self.liters)

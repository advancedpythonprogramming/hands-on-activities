# Here we define some general needed functions
def _average(data):
    return sum(data) / len(data)


def _var(data):
    prom = _average(data)
    suma = 0
    for i in data:
        suma += (i - prom) ** 2
    return suma / len(data)


class Star:
    def __init__(self, star_class, RA, DEC, id, observations=None):
        self.star_class = star_class
        self.RA = RA
        self.DEC = DEC
        self.id = id
        if observations is None:
            observations = []
        self.observations = observations

    def get_magnitudes(self):
        return [i.magnitude for i in self.observations]

    def averageBrightness(self):
        magnitudes = self.get_magnitudes()
        return _average(magnitudes)

    def varBrightness(self):
        magnitudes = self.get_magnitudes()
        return _var(magnitudes)

    def addObservation(self, magnitude, tiempo, error):
        self.observations.append(Observation(magnitude, tiempo, error))


class Observation(object):
    def __init__(self, magnitude, tiempo, error):
        self.magnitude = magnitude
        self.tiempo = tiempo
        self.error = error


class Field:
    def __init__(self, stars=None):
        if stars is None:
            stars = []
        self.stars = stars

    def addStar(self, star):
        self.stars.append(star)


class Sky:
    def __init__(self, fields=None):
        if fields is None:
            fields = []
        self.fields = fields

    def addField(self, field):
        self.fields.append(field)


if __name__ == '__main__':
    sky = Sky()

    e0 = Star('RRLyrae', 0, 0, 0, [Observation(2, 1000, (1, 3)),
                                   Observation(3, 1000, (2, 3)),
                                   Observation(4, 1000, (3, 5))])

    e1 = Star('Eclipsing Binaries', 20, 30, 1, [Observation(2, 1000, (1, 3)),
                                                Observation(5, 1000, (2, 7)),
                                                Observation(6, 1000, (6, 9))])

    e2 = Star('Mira', 15, 50, 2, [Observation(7, 1000, (1, 10)),
                                  Observation(8, 1000, (1, 30)),
                                  Observation(9, 1000, (7, 10))])

    field0 = Field()

    e3 = Star('Cepheids', 50, 15, 3)
    e4 = Star('Cepheids', 120, 120, 4)
    e5 = Star('Eclipsing Binaries', 0, 90, 5)

    e3.addObservation(21, 1000, (15, 30))
    e3.addObservation(22, 1000, (15, 30))
    e3.addObservation(23, 1000, (15, 30))
    e4.addObservation(24, 1000, (15, 30))
    e4.addObservation(25, 1000, (15, 30))
    e4.addObservation(26, 1000, (15, 30))
    e5.addObservation(27, 1000, (15, 30))
    e5.addObservation(28, 1000, (15, 30))
    e5.addObservation(29, 1000, (15, 30))

    field0.addStar(e3)
    field0.addStar(e4)
    field0.addStar(e5)

    sky.addField(field0)
    sky.addField(Field([e0, e1, e2]))

    print(sky.fields[0].stars[0].get_magnitudes())

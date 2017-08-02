class Package:
    packages_id = 0

    def __init__(self):
        Package.packages_id += 1
        self.id = Package.packages_id
        self.bottles = []

    def agregar_bottle(self, bottle):
        self.bottles.append(bottle)

    def add_bottles(self, bottles):
        self.bottles.extend(bottles)

    def see_content(self):
        print("----------------------")
        print("Package #{}".format(self.id))
        for bottle in self.bottles:
            print(bottle)

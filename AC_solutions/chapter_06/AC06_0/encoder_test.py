import encryptor


# To verify that the function is biyective you can use:
def check_bijection(rot):
    dom = 26
    rec = []

    for x in dom:
        y = rot.get(x)
        assert y is not None
        rec.append(y)

    assert set(dom) == set(rec)


def setup_module(module):
    pass


class TestRotor:
    def setup_class(cls):
        cls.rotors = []
        for i in range(1, 4):
            cls.rotors.append(
                encryptor.Rotor('files/rotor{0}.txt'.format(i))
            )

    def test_function(self):
        # You can use the rotors by calling: self.rotors
        pass


class TestReflector:
    def setup_class(cls):
        cls.reflector = encryptor.Reflector('files/reflector.txt')

    def test_function(self):
        # You can use the reflector by calling: self.reflector
        pass


class TestEncoder:
    def setup_class(cls):
        pass

    def test_encoding(self):
        pass

    def test_exception(self):
        pass

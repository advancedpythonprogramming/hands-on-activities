import string
import encryptor as enc
import pytest


def check_bijection(rot):
    dom = range(26)
    rec = []

    for x in dom:
        y = rot.get(x)
        assert y is not None
        rec.append(y)

    assert set(dom) == set(rec)


def setup_module(module):
    enc.create_alphabet((list(string.ascii_lowercase)))


class TestRotor:
    def setup_class(cls):
        cls.rotors = []
        for i in range(1, 4):
            cls.rotors.append(enc.Rotor('files/rotor{0}.txt'.format(i)))

    def test_function(self):
        for rotor in self.rotors:
            check_bijection(rotor)


class TestReflector:
    def setup_class(cls):
        cls.reflector = enc.Reflector('files/reflector.txt')

    def test_function(self):
        dom = range(26)
        check_bijection(self.reflector)
        for x in dom:
            y = self.reflector.get(x)
            x2 = self.reflector.get(y)
            assert x2 is not None and x2 == x


class TestEncoding:
    def setup_class(cls):
        rots = ['files/rotor1.txt', 'files/rotor2.txt', 'files/rotor3.txt']
        refl = 'files/reflector.txt'
        cls.list_ = ['thequickbrownfoxjumpsoverthelazydog',
                     'python', 'bang', 'dragonfly', 'csharp']
        cls.encoder = enc.Encoder(rots, refl)

    def test_encoding(self):
        for text in self.list_:
            a = self.encoder.encrypt(text)
            assert a != text
            b = self.encoder.encrypt(a)
            assert text == b

    def test_exception(self):
        with pytest.raises(ValueError):
            self.encoder.encrypt('I AM SURE THIS WILL PASS')

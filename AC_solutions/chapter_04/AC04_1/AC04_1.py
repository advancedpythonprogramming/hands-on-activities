def create_property(name, _type):
    '''Creates a property for an attribute with name <name> which forces 
    the attribute to be of type <_type>'''

    def getter(self):
        '''Returns the objects attribute or None if its non-existent'''
        return self.__dict__.get(name)

    def setter(self, val):
        '''Only allows attribute setting if it is of the correct type'''
        if isinstance(val, _type):
            self.__dict__[name] = val
        else:
            print('ERROR: expect object of type {}'.format(_type))

    return property(getter, setter)


class Meta(type):

    def __new__(cls, clsname, bases, clsdict):

        # Iterates over the class dictionary looking for attributes that have
        # a type object associated
        for key, val in clsdict.items():

            if isinstance(val, type):
                # Changes that attributes content to a propety
                clsdict[key] = create_property(key, val)
        return super().__new__(cls, clsname, bases, clsdict)


class Person(metaclass=Meta):
    name = str
    age = int


class Company(metaclass=Meta):
    name = str
    stock_value = float
    employees = list


# END OF SOLUTION #

c = Company()
c.name = 'Apple'
c.stock_value = 125.78
c.employees = ['Tim Cook', 'Kevin Lynch']
print(c.name, c.stock_value, c.employees, sep=', ')


p = Person()
p.name = 'Karim'
p.age = 'hello'
# this will print 'ERROR'

print(p.name, p.age, sep=', ')


# BONUS CODE #


# This code achieves the same behaviour but it also allows
# creating objects with initial attribut values. This is
# a more complete and robust solution

# eg:
# p = Person('Marco', 20)


from collections import OrderedDict


class MetaOpt(type):

    @classmethod
    def __prepare__(metacls, name, bases):
        '''Constructs the class over an OrderedDict instead of a normal
        dictionary'''
        return OrderedDict()

    def __new__(cls, clsname, bases, clsdict):

        # Remembers the attribute names in order to construct the '__call__'
        # method
        attributes = list()

        for key, val in clsdict.items():
            if isinstance(val, type):
                attributes.append(key)
                clsdict[key] = create_property(key, val)

        # Saves the attribute names
        cls._attributes = attributes

        return super().__new__(cls, clsname, bases, dict(clsdict))

    def __call__(cls, *args, **kwargs):
        # calls type's '__call__' method in order to create a new object
        obj = super().__call__()

        # Associates <args> to the attribute names previously saved
        for key, value in zip(cls._attributes, args):
            # sets the attribute values of the new object
            setattr(obj, key, value)
        return obj


# END OF BONUS #


class Person(metaclass=MetaOpt):
    name = str
    age = int
    gender = str
    friends = tuple


p1 = Person('Marco', 20, 'male', ('Belen', 'Pato', 'Jaime', 'Rodrigo'))

print(p1.name, p1.age, p1.gender, p1.friends, sep='\n')

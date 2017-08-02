def compare_by(attr):
    """
    This is a class decorator generator that takes an attribute as
    an argument. Adds the ability to compare class objects by the
    given attribute. The attribute must be a comparable type.
    """

    def decorator(cls):
        def less_than(a, b):
            return getattr(a, attr) < getattr(b, attr)

        def less_equal(a, b):
            return getattr(a, attr) <= getattr(b, attr)

        def equal(a, b):
            return getattr(a, attr) == getattr(b, attr)

        def greater_equal(a, b):
            return getattr(a, attr) >= getattr(b, attr)

        def greater_than(a, b):
            return getattr(a, attr) > getattr(b, attr)

        # we now add the new methods to the class
        setattr(cls, '__lt__', less_than)
        setattr(cls, '__le__', less_equal)
        setattr(cls, '__eq__', equal)
        setattr(cls, '__ge__', greater_equal)
        setattr(cls, '__gt__', greater_than)

        # we return the modified class
        return cls

    return decorator


def save_instances(cls):
    """
    This decorator modifies a class's behaviour such that the
    class now posseses a static list attribute that contains all
    the instances that have been created. This list may be accessed
    through Class.instances.
    """

    # a reference to the original __init__ is saved
    prev_init = getattr(cls, '__init__')

    def new_init(self, *args, **kwargs):
        # The new __init__ shall call the previous and add the created
        # object to the class instances' list.

        prev_init(self, *args, **kwargs)
        cls.instances.append(self)

    # Class attributes are added/modified
    setattr(cls, 'instances', list())
    setattr(cls, '__init__', new_init)

    # The original class is returned after the modifications
    return cls


def change_tax(func):
    """This decorator modifies price calculating functions in order
    to consider a change in sales tax in the prices"""

    def inner(num):
        """
        We subtract the 100 spent in transport and then multiply
        by 1.23/1.19 in order to account for the change in sales tax.
        The 100 transport fee is then added back.
        """
        return (func(num) - 100) * 1.23 / 1.19 + 100

    return inner


@compare_by("meat_quantity")
@save_instances
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


@change_tax
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

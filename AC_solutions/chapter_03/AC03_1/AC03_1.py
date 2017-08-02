from datetime import date
from functools import reduce

path = "players.txt"


def read_file():
    def splitter(line):
        return tuple(line.split(";"))

    def transform_to_int(foo):
        return tuple(map(int, foo))

    splitted = list(map(splitter, [line for line in open(path)]))
    tuplas = map(lambda foo: foo[0:5] + transform_to_int(foo[5:11]),
                 splitted)
    return list(tuplas)


def has_the_name(_list):
    mi_nombre = ("Jaime", "Castro", "Retamal")

    def any_match(tupl):
        return any(map(lambda foo1, foo2: foo1 == foo2, tupl, mi_nombre))

    return list(filter(any_match, _list))


def chilean_lefties(_list):
    tupl = ("Chile", "izquierdo")
    return list(filter(lambda foo: foo[3:5] == tupl, _list))


def get_ages(_list):
    year = date.today().year
    return list(map(lambda foo: foo[0:2] + (year - foo[7],), _list))


def sub_17(_list):
    age_tuples = get_ages(_list)
    return list(filter(lambda foo: foo[2] <= 17, age_tuples))


def top_scorer(_list):
    def better_scorer(foo1, foo2):
        return foo1 if foo1[8] > foo2[8] else foo2

    return reduce(better_scorer, _list)


def highest_obesity_risk(_list):
    def bmi(tupl):
        return (tupl[3] / (tupl[2] / 100) ** 2,)

    def max_bmi(foo1, foo2):
        return foo1 if foo1[4] > foo2[4] else foo2

    # filter for chileans
    team = list(filter(lambda foo: foo[3] == 'Chile', _list))
    # map only the useful fields
    mapped = list(map(lambda foo: foo[0:2] + foo[9:11], team))
    # we add the BMIs
    bmi_tuples = list(map(lambda foo: foo + bmi(foo), mapped))

    return reduce(max_bmi, bmi_tuples)


def print_results(func, _list):
    result = func(_list)

    print(func.__name__.title())
    print("-" * len(func.__name__))

    if type(result) is list:
        print(*result, sep='\n')
    else:
        print(result)

    print("")


if __name__ == '__main__':
    tupls = read_file()
    print_results(has_the_name, tupls)
    print_results(chilean_lefties, tupls)
    print_results(get_ages, tupls)
    print_results(sub_17, tupls)
    print_results(top_scorer, tupls)
    print_results(highest_obesity_risk, tupls)

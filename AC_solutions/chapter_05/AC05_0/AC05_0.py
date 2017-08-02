import enum
from math import e, pi


class Operations(enum.Enum):
    sum = ('+', 'plus')
    substraction = ('-', 'minus')
    multiplication = ('*', 'times')
    division = ('/', 'divided')
    module = ('%', 'module')

    def find_operation(operacion_str):
        for operacion in Operations:
            if operacion.value[0] == operacion_str:
                return operacion

    def is_operation(value):
        for operacion in Operations:
            if operacion.value[0] == value:
                return True
        return False


def index_generator(n):
    for i in range(n):
        yield i


class Calculator:
    def __init__(self, letras_especiales):
        self.special_letters = letras_especiales

    def find_operations(self, statement):
        operations = []
        operands = []
        last = 0
        for i in range(len(statement)):
            if Operations.is_operation(statement[i]):
                operands.append(statement[last:i])
                operations.append(statement[i])
                last = i + 1
        if last != len(statement):
            operands.append(statement[last:])
        return operations, operands

    def read_operations(self, statement):
        statement = statement.replace(' ', '')
        operations, operand = self.find_operations(statement)
        operands_index = index_generator(len(operand))
        operator1 = self.digit_value(
            operand[next(operands_index)], statement)
        for current_operation in operations:
            try:
                operator2 = self.digit_value(
                    operand[next(operands_index)], statement)
            except StopIteration:
                print('[ERROR] {0}'.format(StopIteration.__name__))
                print('There\'s one missing operator in {0}'.format(statement))
            else:
                operation = Operations.find_operation(current_operation)
                result = self.do_operation(
                    operator1, operator2, operation, statement)
                operator1 = result

    def do_operation(self, operator1, operator2, operation, statement):
        try:
            if operation is Operations.sum:
                result = operator1 + operator2
            elif operation is Operations.substraction:
                result = operator1 - operator2
            elif operation is Operations.multiplication:
                result = operator1 * operator2
            elif operation is Operations.division:
                try:
                    result = operator1 / operator2
                except ZeroDivisionError:
                    print('[ERROR] {0}'.format(ZeroDivisionError.__name__))
                    result = 'infinite'
            else:
                result = operator1 % operator2
            print('{0} {1} {2} is equal to {3}'.format(
                operator1, operation.value[1], operator2, result))
            return result
        except:
            print('The operation wasn\'t exceuted {0}'.format(statement))

    def digit_value(self, number_letter, statement):

        if number_letter.isdigit():
            return int(number_letter)

        elif number_letter.isalpha():
            try:
                v = self.special_letters[number_letter]
            except KeyError:
                print('[ERROR] {0}'.format(KeyError.__name__))
                print(('\'{0}\' doesn\'t any assigned values .'
                       'You must added before using it.').format(
                    number_letter))
            else:
                return v

        elif Calculator.isfloat(number_letter):
            return float(number_letter)

        else:
            print(('[ERROR] The sintaxis \'{0}\' is incorrect. '
                   'Read the manual for more information.').format(statement))

    def isfloat(s):
        try:
            float(s)
            return True
        except ValueError:
            print('[ERROR] {0}'.format(ValueError.__name__))
            print('\'{0}\' cannot be parse to float'.format(s))
            return False

    def add_letter(self, letter, value):
        try:
            v = self.special_letters[letter]
        except KeyError:
            self.special_letters[letter] = value
        else:
            print('[ERROR] {0}'.format(KeyError.__name__))
            print(('Letter \'{0}\' won\'t be agregated. '
                   'It already exist in memory.').format(letter))


# DO NOT MODIFY THIS.
special_letters = {'g': 9.81, 'e': e, 'pi': pi}
calculator = Calculator(special_letters)
tested_operations = ['3+5', 'g*3', 'pi*4', '76 /2 + 35 / 5']
calculator.add_letter('g', 5757)
print('')
statements_for_testing = ['1/0', 'a+2', 'g+0', '88/2+0+', '1=2', '8.953 + 1']
for operations in statements_for_testing:
    calculator.read_operations(operations)
    print('')

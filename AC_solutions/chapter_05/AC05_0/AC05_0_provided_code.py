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
            operator2 = self.digit_value(
                operand[next(operands_index)], statement)
            operation = Operations.find_operation(current_operation)
            result = self.do_operation(
                operator1, operator2, operation, statement)
            operator1 = result

    def do_operation(self, operator1, operator2, operation, statement):
        if operation is Operations.sum:
            result = operator1 + operator2
        elif operation is Operations.substraction:
            result = operator1 - operator2
        elif operation is Operations.multiplication:
            result = operator1 * operator2
        elif operation is Operations.division:
            result = operator1 / operator2
        else:
            result = operator1 % operator2
        print('{0} {1} {2} is equal to {3}'.format(
            operator1, operation.value[1], operator2, result))
        return result

    def digit_value(self, number_letter, statement):

        if number_letter.isdigit():
            return int(number_letter)
        else:
            return self.special_letters[number_letter]

    def add_letter(self, letter, value):
        self.special_letters[letter] = value


# DO NOT MODIFY WHAT FOLLOWS
special_letters = {'g': 9.81, 'e': e, 'pi': pi}
calculator = Calculator(special_letters)
tested_operations = ['3+5', 'g*3', 'pi*4', '76 /2 + 35 / 5']
calculator.add_letter('g', 5757)
print('')
statements_for_testing = ['1/0', 'a+2', 'g+0', '88/2+0+', '1=2', '8.953 + 1']
for operations in statements_for_testing:
    calculator.read_operations(operations)
    print('')

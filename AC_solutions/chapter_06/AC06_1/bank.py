class User:

    def __init__(self, _id, name, password):
        self._id = _id
        self.name = name
        self.password = password
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class Bank:

    def __init__(self, name):
        self.name = name
        self.users = []

    def add_user(self, _id, name, password):
        user = User(_id, name, password)
        self.users.append(user)

    def verify_login(self, _id, password):
        self.actual_user = None
        for user in self.users:
            if user._id == _id:
                if user.password == password:
                    self.actual_user = user
                    return True
                else:
                    return False

    def find_third_person(self, _id):
        self.third_person = None
        for user in self.users:
            if user._id == _id:
                self.third_person = user
                return True
        return False

    def withdraw(self, user, amount):
        user.withdraw(amount)

    def deposit(self, user, amount):
        user.deposit(amount)


class ATM:

    def __init__(self, bank):
        self.bank = bank
        self.max_withdrawal = 200000
        self.max_transfer = 1000000

    def login(self, _id, password):
        if(self.bank.verify_login(_id, password)):
            print("You have successfully login to " + self.bank.name)
        else:
            print("Sorry, login couldn't be performed")

    def withdraw_money(self, _id, password, amount):
        self.login(_id, password)
        if(amount < self.max_withdrawal):
            self.bank.withdraw(self.bank.actual_user, amount)
            print("Successfull withdrawal", amount)
        else:
            print("Amount exceeds the limit")

    def transfer_money(self, _id, password, _id_destinatario, amount):
        self.login(_id, password)
        if (amount < self.max_transfer):
            self.bank.find_third_person(_id_destinatario)
            self.bank.withdraw(self.bank.actual_user, amount)
            print("Transference was done successfully", amount)
        else:
            print("Amount exceeds the limit")

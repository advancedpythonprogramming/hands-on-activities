import unittest
from bank import Bank, ATM


class Test_ATM(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Seguritas")
        self._id1 = "18.375.852-2"
        self.name1 = "John Dupre"
        self.password1 = 2345
        self._id2 = "13.432.113-k"
        self.name2 = "Emma Cashter"
        self.password2 = 5912
        self.bank.add_user(self._id1, self.name1, self.password1)
        self.bank.add_user(self._id2, self.name2, self.password2)
        self.atm = ATM(self.bank)

    def test_credentials(self):
        # first case: _id y password right
        self.atm.login(self._id1, self.password1)
        _idingresado = self.bank.actual_user._id
        self.assertEqual(self._id1, _idingresado)
        # second case: _id right but password incorrect
        self.atm.login(self._id1, 1234)
        self.assertIsNone(self.bank.actual_user)
        # tercer case: _id no está en la bank database
        self.atm.login("10.000.000-1", 1234)
        self.assertIsNone(self.bank.actual_user)

    def test_balance(self):
        self.atm.withdraw_money(self._id1, self.password1, 20000)
        balance = self.bank.actual_user.balance
        # the user must have balance 0, ya que nunca ha depositado
        self.assertEqual(0, balance)
        # the test fails, you can see that the balance results in
        # -20.000 when it should be 0

    def test_amount_updated(self):
        self.atm.login(self._id1, self.password1)
        # deposit of 10.000
        self.bank.deposit(self.bank.actual_user, 10000)
        # withdrawal of 5.000
        self.atm.withdraw_money(self._id1, self.password1, 5000)
        balance = self.bank.actual_user.balance
        # balance must end up in 5000
        self.assertEqual(5000, balance)

    def test_account_tercero(self):
        # Will try to transfer to an account that does not exist
        self.atm.login(self._id1, self.password1)
        self.bank.deposit(self.bank.actual_user, 10000)
        self.atm.transfer_money(
            self._id1, self.password1, "1.000.000-3", 5000)
        self.assertIsNone(self.bank.third_person)
        # Indeed the destination user is not created and it is not found

    def test_amounts_updated(self):
        self.atm.login(self._id1, self.password1)
        # account 1 receives 15.000
        self.bank.deposit(self.bank.actual_user, 15000)
        # 5.000 transfered from account 1 to account 2
        self.atm.transfer_money(self._id1, self.password1, self._id2,
                                3000)
        # we should prove that account 1 balance = 12.000 and account 
        # 2 balance = 3.000
        amountUser = self.bank.actual_user.balance
        amountThird = self.bank.third_person.balance
        self.assertEqual(amountUser, 12000)
        self.assertEqual(amountThird, 3000)
        # Here the test fails

    def test_verify_error(self):
        # what if the third user does not exist
        self.atm.login(self._id1, self.password1)
        # account 1 receives a 10.0000 deposit
        self.bank.deposit(self.bank.actual_user, 10000)
        # lets transfer to a non existing account
        self.atm.transfer_money(
            self._id1, self.password1, "1.000.000-3", 5000)
        # lets verify that the transference is not performed
        amountUser = self.bank.actual_user.balance
        self.assertEqual(amountUser, 10000)
        # we can see that anyway the 5.000 is substracted despite the
        # error the test fails


if __name__ == "__main__":
    unittest.main()

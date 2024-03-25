# Import required libraries and modules
import datetime
import pytz


# Defining a class names Account
class Account:
    """ Simple account class with balance """

    # Applying @staticmethod as a decorator to the _current_time() method within the class.
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self.transaction_list = []
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    thea = Account("Thea", 0) # Initialising the instance of Thea
    thea.show_balance()

    thea.deposit(1000)
    # thea.show_balance()
    thea.withdraw(500)
    # thea.show_balance()

    thea.withdraw(2000)

    thea.show_transactions()

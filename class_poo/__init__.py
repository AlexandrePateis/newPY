class CurrentAccount:

    def __init__ (self, holder, limit, balance):

        number_account = 500
        self.__holder = holder
        self.__limit = limit
        self.__balance = balance
        self.__number_account = number_account
        number_account += 1

    def shor_the_holder(self):
        print(f'The holder is {self.__holder}')

    def show_limit(self):
        if self.__limit > 0:
            print(f'THe limit is U$${self.__limit}')
        else:
            print(f'No limit or debtor.')

    def show_balance(self):
        if self.__balance > 0:
            print(f'The balance is U$${self.__balance}')

    def deposit(self, value):
        if value > 0:
            self.__balance += value

    def withdraw(self, value):
        if self.__balance <= value:
            print(f'Insufficient balance or withdrawal equals balance.')
        else:
            self.__balance -= value

    def transfer(self, value, account_destiny):
        if self.__balance <= value:
            print(f'Transfer denied.')
        else:
            self.__balance -= value
            account_destiny.__balance += value

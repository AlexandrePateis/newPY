from class_poo import CurrentAccount

account1 = CurrentAccount('Alexandre Pateis', 4500, 250)
account2 = CurrentAccount('Julia Fernandes', 1500, 250)
account2.transfer(50, account1)
account2.show_balance()
account1.show_balance()
account1.withdraw(500)
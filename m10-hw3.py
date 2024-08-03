# m10-hw3 ''
import threading
from random import random
from time import sleep


class BankAccount:
    def __init__(self):
        self.amount = 0
        print(f'amount: {self.amount}')

    def deposit(self, amount):
        self.amount += amount
        print(f'deposit  amount: {self.amount}')

    def withdraw(self, amount):
        self.amount -= amount
        print(f'withdraw amount: {self.amount}')


def deposit_task(account, amount):
    for _ in range(5):
        sleep(10 * random())
        with my_lock:
            account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        sleep(10 * random())
        with my_lock:
            account.withdraw(amount)


account_1 = BankAccount()
my_lock = threading.RLock()

deposit_thread_1 = threading.Thread(target=deposit_task, args=(account_1, 100))
withdraw_thread_1 = threading.Thread(target=withdraw_task, args=(account_1, 150))

deposit_thread_1.start()
withdraw_thread_1.start()

deposit_thread_1.join()
withdraw_thread_1.join()

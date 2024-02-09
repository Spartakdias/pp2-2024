class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение на {amount} тенге выполнено. Данный баланс: {self.balance} тенге")
        else:
            print("Ошибка: Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Снятие {amount} тенге выполнено. Данный баланс: {self.balance} тенге")
        else:
            print("Ошибка: Недостаточно средств для снятия или сумма снятия некорректна.")

a = input("Name: ")
b = int(input("Money = "))
if __name__ == "__main__":
    account = BankAccount(a, b)
    c = int(input())
    d = int(input())
    account.deposit(c) 
    account.withdraw(d)  
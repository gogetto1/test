class Result:
    def __init__(self, isSuccess, message, value=None):
        self.isSuccess = isSuccess
        self.message = message
        self.value = value


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        "tutaj coś co sprawdza pieniadze"
        self.balance += amount

    def try_withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return Result(True, "Wyplacono środki", amount)
        return Result(False, "za mało środków", amount)

    def __str__(self):
        return f"{self.balance}"


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def try_withdraw(self, amount):
        if(self.balance - amount) > self.minimumBalance:
            return super().try_withdraw(amount)
        else:
            return Result(False, "Nie udało się, próba przekroczenia progu", amount)

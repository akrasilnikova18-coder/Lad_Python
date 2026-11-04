# Создать «банковский счёт» в классе. Класс BankAccount с полями owner, balance (__init__),
# методами deposit(amount), withdraw(amount) и show(). Метод withdraw не должен позволять уйти в минус:
# если сумма больше остатка — выводить сообщение и ничего не менять. Создать 2 счёта,
# проверить операции на каждом.


class BankAccount:
    def __init__(self, owner: str, balance: int) -> None:
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f"Сообщение для: {self.owner}. Пополнение счета на: {amount} рублей, баланс: {self.balance} рублей")
        
    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            print(f"Сообщение для: {self.owner}. Баланс: {self.balance} рублей, нельзя снять сумму: {amount} рублей")
        else:
            self.balance -= amount
            print(f"Сообщение для: {self.owner}. Списание счета на: {amount} рублей, баланс: {self.balance} рублей")
            
    def show(self) -> None:
        print(f"Сообщение для: {self.owner}. Остаток на счете: {self.balance} рублей")
        
        
if __name__ == "__main__":
    bank_account1 = BankAccount(owner="Анна", balance=100000)
    bank_account1.deposit(amount=10000)
    bank_account1.withdraw(amount=5000)
    bank_account1.show()
    
    bank_account2 = BankAccount(owner="Алексей", balance=150000)
    bank_account2.deposit(amount=80000)
    bank_account2.withdraw(amount=3000)
    bank_account2.show()

    bank_account1.withdraw(amount=150000)
    bank_account1.show()

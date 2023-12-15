class Account:
    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.balance = 0
    def deposit(self,amount):
        self.balance +=amount 
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Yetersiz Bakiye!")
        else:
            self.balance -= amount

class SavingAccount(Account):
    def __init__(self, account_holder,interest_rate):
        super().__init__(account_holder)
        self.interest_rate = interest_rate
    def add_interest(self):
        gelir = self.balance* self.interest_rate        
        self.balance += gelir

class CheckingAccount(Account):
    def __init__(self, account_holder,overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > (self.balance)+(self.overdraft_limit):
            print("Yetersiz Bakiye!")
        else:
            self.balance -= amount

acc1 = Account("isim1")
acc1.deposit(100)
print(acc1.balance)
acc1.withdraw(50)
print(acc1.balance)

acc2 = SavingAccount("isim2",1/10)
acc2.deposit(1000)
acc2.add_interest()
print(acc2.balance)

acc3 = CheckingAccount("isim3",1000)
acc3.withdraw(900)
print(acc3.balance)
acc3.withdraw(200)
print(acc3.balance)
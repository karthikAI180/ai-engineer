from bank_account import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,interest):
        super().__init__(owner,balance)
        self.interest=interest
    def __repr__(self):
        return "SavingsAccount(owner='{}', balance={})".format(self.owner,int(self.balance))
    def __str__(self):
        return "{}'s savings account | Balance: ${:.2f}".format(self.owner,self.balance)
    def withdraw(self, amount):
        amount=amount+2
        if amount>self.balance:
            raise ValueError("Insufficient funds")
        else:
            self.balance-=amount
    @property
    def apply_interest(self):
        print("balance before->{}".format(self.balance))
        self.balance*=self.interest
        print("balance after  →{}".format(self.balance))

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,balance):
        if balance<0:
            raise ValueError(...)
        self._balance=balance

acc1=SavingsAccount("Alice",500,1.04)
acc1.balance=29
print(repr(acc1))
acc1.apply_interest
print(str(acc1))
acc1.withdraw(1)
print(str(acc1))
print(BankAccount.total_accounts)
"""Task 1
Inside your class declare a variable
that tracks total accounts created.
It should not be inside any method.
Task 2
Add __init__ method that accepts:
- owner
- balance
And does:
- assigns owner as instance variable
- assigns balance as instance variable
- increases total_account by 1
Task 3
Inside deposit method:
- accept amount as parameter
- if amount is negative → print error message
- if amount is valid → add to balance
- print new balance
Task 4
Add withdraw method that accepts amount
and does:
- if amount > balance → print insufficient funds
- if amount is valid  → deduct from balance
- print new balance
Task 5
Add get_details method that prints:
- owner name
- current balance
Task 6 
Add __str__ method that returns
owner name and balance
so when you print(acc1)
it shows clean output
Task 7
Add __repr__ method that returns
output that looks like Python code
to recreate the object
hint: BankAccount('Karthik reddy', 10000)
Task 8
Add from_string classmethod that accepts
a string like "Karthik,10000"
splits it by comma
and creates a new BankAccount object
Task 9
Add is_valid_amount staticmethod that:
- accepts amount as parameter
- returns True if amount > 0
- returns False if amount <= 0
Task 10
At the bottom of your file test:
- create 2 objects normally
- create 1 object using from_string
- deposit on acc1
- withdraw on acc2
- try insufficient funds
- print(acc1)
- repr(acc1)
- details()
- valid_amount() with 100 and -50
- print total_accounts
"""
class BankAccount:
    total_accounts=0
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        BankAccount.total_accounts+=1
    @staticmethod
    def valid_amount(amount):
        if amount>0:
            return True
        else:
            return False
    @classmethod
    def from_string(cls,acc_str):
        owner,balance=acc_str.split(",")
        return cls(owner,int(balance))
    def __str__(self):
        return "owner name '{}' and balance {}".format(self.owner,self.balance)
    def __repr__(self):
        return "BankAccount('{}', {})".format(self.owner,self.balance)
    def deposit(self,amount):
        if amount<0:
            print("ERROR")
        else:
            self.balance+=amount
            print(self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance-=amount
            print(self.balance)
    def details(self):
        print("Bank account owner name is {} and have {} in their account".format(self.owner,self.balance))
if __name__ == "__main__":
    acc1=BankAccount("Karthik reddy",10000)
    acc2=BankAccount("Manasareddy",30000)
    acc3=BankAccount.from_string("kavyareddy,20000")
    acc1.deposit(500)
    acc2.withdraw(1000)
    acc3.withdraw(25000)
    print(acc1)
    print(repr(acc1))
    acc1.details()
    print(BankAccount.valid_amount(100))
    print(BankAccount.valid_amount(-50))
    print(BankAccount.total_accounts)






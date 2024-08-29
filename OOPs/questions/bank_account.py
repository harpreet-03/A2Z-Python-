'''
Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance.

'''

class Account:
    def __init__(self, bal, accNo):
        self.balance = bal
        self.account_no = accNo
      
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, " was debited") 
        print("Account Balance: ", self.balance)
        
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, " was Credited") 
        print("Account Balance: ", self.balance)
    
    def getBalance(self):
        return self.balance
    
#user 1
acc1 = Account(1000, 122333)
acc1.debit(500)
acc1.credit(700)
print(acc1)

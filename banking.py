class Banking:
     def __init__(self, user_name, initial_balance):
          self.name  = user_name
          self.balance = initial_balance
          
     def deposit(self, amount):
         if amount>0:
             self.balance += amount
         return amount
     
     def get_balance(self):
         return self.balance
     
     def withdraw(self, amount):
          if amount < self.balance:
              self.balance -= amount
              return amount
          else:
              return f"Insufficient Balance"
         
          
Akash = Banking("Akash", 10000)
print(f"Account Name: {Akash.name}")
print(f"Initial Balance is: {Akash.balance}")
print(f"Deposit Balance: {Akash.deposit(1000)}")
print(f"After deposit, Your Balance is: {Akash.get_balance()}")
print(f"Withdraw Balance: {Akash.withdraw(2000)}")
print(f"After withdraw, Your Balance is: {Akash.get_balance()}")
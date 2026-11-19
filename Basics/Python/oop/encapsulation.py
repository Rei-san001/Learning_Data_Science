# access modifiers ->
# 1. public - can be accessible from anywhere
# 2. private (__variable) - can be accessible but requires some methods i.e. getter/setter
# 3. Protected (_variable)- unlike private


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # basically we made it private 
        
    # getter function
    def get_balance(self):
        return self.__balance
    
    # setter function
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount
    

acc = BankAccount(1000)
balance = acc.get_balance()
print(f"Main balance : {balance}")


acc.deposit(500)
balance = acc.get_balance()
print(f"After deposit, balance =  {balance}")

acc.withdraw(500)
balance = acc.get_balance()
print(f"After Withdraw, balance =  {balance}")
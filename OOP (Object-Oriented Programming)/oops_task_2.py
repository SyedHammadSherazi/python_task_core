# Create a BankAccount class with deposit/withdraw methods; balance must never go
# negative. 
class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Welcome to the Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Net Available Balance =", self.balance)



if __name__ == "__main__":
    s = BankAccount() 

    s.deposit()        
    s.withdraw()       
    s.display()        
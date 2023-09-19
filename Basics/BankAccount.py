class Account:
    def __init__(self, accId, name, pin, balance):
        self.accId = accId
        self.name = name
        self.pin = pin
        self.balance = balance



    def deposit (self, amount):
        self.balance += amount



    def withdrow (self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Balance is now enough!")

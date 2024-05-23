class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,refill):
        self.balance+=refill
        print('Balance:'+str(self.balance))
    def withdraw(self,withdraw):
        if self.balance<withdraw:
            print('Insufficient funds for withdrawal')
            return 0
        else:
            self.balance-=withdraw
            print('Balance:'+str(self.balance))
owner=Account("Kairat Nurtas", 500)
owner.deposit(100)
owner.withdraw(750)


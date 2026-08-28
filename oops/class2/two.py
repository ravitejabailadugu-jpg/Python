class account:
    min_bal=500
    bank="SBI"

          #class variable

    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    def deposit(self,amount):
        self.acc_bal=self.acc_bal+amount

    def wihtdraw(self,amount):
        self.acc_bal=self.acc_bal amount
    def get_bal(self):
        return self.acc_bal-self.min_bal


a1=account(1,"ravi",5000)
a2=account(2,"teja",6000)
a3=account(3,"siva",7000)

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__) 


a1.deposit(500)
a2.deposit(600)
a3.deposit(700)

a1.wihtdraw(20)


print(a1.get_bal())
print(a2.get_bal())
print(a3.get_bal())

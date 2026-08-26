class Account:
    min_bal=500
    bank_name="SBI"
    def  __init__(self,id,nane,amount):
        self.acc_id=id
        self.acc_name=nane
        self.acc_bal=amount

    def deposit(self):
        print("amount deposit sucessfull")

a1=Account(1,"ravi",5000)
a2=Account(2,"siva",6000)
a3=Account(3,"ram",7000)
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)

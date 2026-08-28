class Account:
    min_bal=500  #static/class variable
    def __init__(self,id,name,amount):
        self.acc_id=id 
        self.acc_nmae=name 
        self.acc_bal=amount 

    def deposit_amount(self,amout):
        self.acc_bal=self.acc_bal+amout

    def withdrawl_amount(self,amount):
        pass
    @classmethod
    def update_minbal(cls,amount):
        pass
    @staticmethod
    def cal_interest(p,ri):
        pass 


a1=Account(101,'RG',5000)
a2=Account(102,'SG',6000)
print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)
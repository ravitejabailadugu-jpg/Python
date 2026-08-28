class Test:
    a=10
    #class variables

    def __init__(self):
        self.b=20
        self.c=30
    def m1(self):
        self.d=40

    @classmethod
    def m2(cls):
        Test.g=70

t1=Test() here if you are object to the most inverting so that it's very difficult distancein Python is supporting itself to polymark is supporting objects in the abstraction I sort of size one more definite that is using a start to capture and using one more method method using abstract we will discuss so I want to have essentially I don't know I implemented which implementation I am going to use so what is encapsulation finding data and method it will be a method a similar and writing data plus method as one single single what is the so reusing the existing function and adding the in the use in the existing guns in gas in gas on whichin glass missionary and adding new field new functional new field or you can say generating the properties from all services
t2.m1()
print(Test.__dict__)
print(t1.__dict__)
print(t2.__dict__)

print("Instance variable")
t2.e=50
t1.f=60



print(t1.__dict__)
print(t2.__dict__)

print("class variable")
Test.m2()
print(Test.__dict__)






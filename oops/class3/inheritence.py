class Parent:
    def m1(self):
        print("Parent Class m1 - instance method") 
    def m2(self):
            print("Parent Class m2 - instance method")
class Child(Parent):
    def m3(self):
            print("Child Class m3 - instance method") 


c1=Child()

c1.m1()
c1.m2()
c1.m3()

#Inheritance means one class can acquire the properties and methods of another class.

#python using
#Hierarchical inheritance
#Hybrid inheritance
#Single inheritance
#Multiple inheritance
#Multilevel inheritance

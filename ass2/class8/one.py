#lucky dip functionality using random module
import random
enames=['Simrith','vikas','Kavya','Lavanya','KS','Babji','Seshu','Ravi','Mohith','charan','Siddarth']

print(dir(random))

lucky_fellow=random.choice(enames)
lucky_fellows=random.choices(enames,)
print(lucky_fellow)
print(lucky_fellows)
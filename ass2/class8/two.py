#similate rolling 6 side die 10 times and print each result
import random


die_values=[1,2,3,4,5,6]
for num in range(10):
    result=random.choice(die_values)
    print(num+1,"-time and die result:",result)
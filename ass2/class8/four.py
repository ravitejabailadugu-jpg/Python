import random

#print(random.sample(range(1,50),k=6))

number=range(1,50)

result_list=random.sample(number,k=7)

for result in result_list:
    print(result)
numbers=[1,2,3,4,5,6,7,8,9,10]

even_numbers=[]

for num in numbers:
    if num%2==0:
        even_numbers.append(num)


print(even_numbers)

#lambda filter

filter_obj= filter(lambda n:n%2==0,[1,2,3,4,5,6,7,8,9,10])


even_numbers =list(filter_obj)

print(even_numbers) 



#with filter

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def verify(n):
    return n%2==0

print(list(filter(verify,numbers)))


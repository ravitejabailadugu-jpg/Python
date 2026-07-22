numbers=[10,20,30,40,]
new_numbers=[]
for num in numbers:
    new_numbers.append(num+1)


print(new_numbers)    




numbers=[10,20,30,40]

map_obj=map(lambda n:n+1,numbers)
new_numbers=list(map_obj)

print(new_numbers)


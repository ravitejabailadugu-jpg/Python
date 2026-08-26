#extract data
import csv
fp1=open('users.csv','r')
csv_reader=csv.reader()
users=list(csv_reader)

user=users[1:]

print(len(user))


#transform data

male_users=[]
for user in users:
    if user[2]=="male":
        male user.append




#load data


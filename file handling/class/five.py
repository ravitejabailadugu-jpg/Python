import json
fp1=open('users.json','r')
users=json.load(fp1)

#tranform
male_users=[]
female_users=[]

for user in users:
    if user['gender']=='Male' :
        male_users.append(user)
    elif user['gender']=='Female':
        female_users.append(user)

print=len(male_users) 

#load
fp2=open('Male.json','w')
fp3=open('Female.json','w')
json.dump(male_users,fp2)
json.dump(female_users,fp3)
print("New json file successfully")

fp1.close()
fp2.close()
fp3.close()
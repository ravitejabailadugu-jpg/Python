#Extract data from Rest API URL
import requests 
import json
user_resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=user_resp.json()

#Transform according to requirement
users_json=[]
users_csv=[]
for user in users:
     users_json.append({"userid":user['id'],
                        "username":user['username'],
                        "location":user['address']['city'],
                        "company":user['company']['name']
                       })
   


print(users_json)




import json
fp1=open('users.json','w')
json.dump(users_json,fp1)
print("New JSON file created successfully")

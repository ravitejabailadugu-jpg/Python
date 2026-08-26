#write a python script to read -data.txt and print data
fp=open('data.txt','r')
data=fp.read()
print(data)


#write apy script to read -user.txt file write data into emp.txt
fp1=open('user.txt','r')
fp2=open('emp.txt','r')

data=fp1.read()
fp2.write(data)
print("new file created successfully")

fp1.close()
fp2.close()
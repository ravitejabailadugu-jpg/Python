#write a python script
# #read emp.json file print all  female/male employees names

import json 

emp_json_str=''''
{"eid":101,"ename":"ravi","avail":t rue}
'''

emp=json.loads(emp_json_str)
print(emp)
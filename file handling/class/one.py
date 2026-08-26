import json
emp_json_str='''
        [{"eid":101,"ename":"gangu","avail":true,"loc":null},
         {"eid":102,"ename":"subhu","avail":false},
         {"eid":103,"ename":"teja","avail":false},
         {"eid":104,"ename":"ravi","avail":true},
         {"eid":105,"ename":"seshu","avail":true}
        ]
        '''
emp_list=json.loads(emp_json_str)
print(emp_list)

for emp in emp_list:
    print(emp['ename'])

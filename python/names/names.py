students = [
	 {'first_name':  'Michael', 'last_name' : 'Jordan'},
	 {'first_name' : 'John', 'last_name' : 'Rosales'},
	 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
	 {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
	 {'first_name':  'Michael', 'last_name' : 'Jordan'},
	 {'first_name' : 'John', 'last_name' : 'Rosales'},
	 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
	 {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
	 {'first_name' : 'Michael', 'last_name' : 'Choi'},
	 {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printName(dicts):
	 for val in dicts:
		 print val['first_name'], val['last_name']

def printUsers(dicts):
	for key, data in dicts.items():
		print key
		for idx, val in enumerate(data):
			 print idx+1, '-' ,val['first_name'].upper(),val['last_name'].upper(),'-',len(val['last_name'])+len(val['first_name'])

printName(students)
printUsers(users)

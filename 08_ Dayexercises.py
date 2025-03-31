dog = {}

dog = {'name':'perla',
       'color':'blanco',
       'breed':'meztizo',
       'legs':4,
       'age':3}

student = {
    'first_name':'Jorge',
    'last_name':'Baez',
    'gender':'masculino',
    'age':20,
    'marital_status':'soltero',
    'skills':['Python','SQL','HTML','CSS','JS'],
    'country':'mexico',
    'city':'aguascalientes',
    'addres':{
        'street':'Av. hacienda de ojocaliente',
        'zipcode':'20196',
    }
}

print(f'The lenght of the student dictionary is {len(student)}')
print(f'The data type of student skills is {type(student["skills"])}')

student['skills'].append('PHP')
print(student['skills'])

keyList = list(student.keys())
print(keyList)

valList = list(student.values())
print(valList)

studentTuple = student.items()
print(studentTuple)

student.pop('gender')
print(student)

del dog

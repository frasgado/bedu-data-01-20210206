'''
How the dictionaries work in Python
'''

student_1 = {
    'name': 'Galileo',
    'age': 31,
    'city': 'Puerto Escondido',
    'state': 'Oaxaca'
}
student_2 = {
    'name': 'Fabiola',
    'age': 47,
    'city': 'Juchitan',
    'state': 'Oaxaca'
}

print(student_1)
print(type(student_1))
print(student_1["name"])
print(student_1["age"])

print(f'{student_1["name"]} is {student_1["age"]} years old.')

fabi = 'fabiola'
print('upper')
print(fabi.upper())
print(fabi.lower())
print(fabi.capitalize())

student_2 = {
    'name': 'Fabiola',
    'age': 47,
    'city': 'Juchitan'
}

#print(student_2['state'])
print(student_2.get('state', 'N/A'))

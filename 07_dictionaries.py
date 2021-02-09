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
    'city': 'Juchitan'
}

print('About of Student 1')
print(student_1)
print(f'Data type: {type(student_1)}')

print(f'name: {student_1["name"]}')
print(f'age: {student_1["age"]}')

print(f'{student_1["name"]} is {student_1["age"]} years old.')

print('\n-----------------------------------------------')
print('About transformations to letters')
v_name = 'fabiola'
print('upper')
print(v_name.upper())
print(v_name.lower())
print(v_name.capitalize())

print('\n-----------------------------------------------')
print('About of Student 2')
#print(student_2['state'])
print(student_2)
print(f'State: {student_2.get('state', 'N/A')}')

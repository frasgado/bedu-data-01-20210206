'''
Sample code of how the string interpolation works in Python
'''

name = 'Fabiola'
last_name = 'Rasgado'

print('1 - ', end='')
print(name + last_name)

print('2 - ', end='')
print(name + ' ' + last_name)

# f-strings
print('3 - ', end='')
full_name = f'{name} {last_name}'
print(full_name)

# String formatting
print('4 - ', end='')
full_name_formating = '{} {}'.format(name, last_name)
print(full_name_formating)

# String formatting 
print('5 - ', end='')
full_name_formating = '{n} {l}'.format(n=name, l=last_name)
print(full_name_formating)
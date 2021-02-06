'''
Sample code of how the string interpolation works in Python
'''

name = 'Fabiola'
last_name = 'Rasgado'

print(name + last_name)

print(name + ' ' + last_name)

# f-strings
full_name = f'{name} {last_name}'
print(full_name)

# String formatting
full_name_formating = '{} {}'.format(name, last_name)
print(full_name_formating)

full_name_formating = '{n} {l}'.format(n=name, l=last_name)
print(full_name_formating)
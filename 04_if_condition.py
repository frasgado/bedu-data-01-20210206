'''
IF condition
'''

import time

name = input('What is your name? ')

print(f'Hello {name}')

magic_number = 6

time.sleep(2.0)
if len(name) > magic_number:
    print('Sorry, but you lost.')
elif len(name) == magic_number:
    print('Congrats, you got a special prize.')
else:
    print('You won!!! :D')

time.sleep(2.0)
print('Good bye!!! :D')
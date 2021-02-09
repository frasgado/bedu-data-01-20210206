'''
Fecha: 06-Febrero-2021
Elaboró: Fabiola Rasgado
Program to calculate the multiplication table of given a number in a range from 1 to 10.
Escribe un programa que calcule la tabla de multiplicar de un número entre 1 - 10
'''
import re
expreg = re.compile(r'[-+]?\d+$')

while True:
    number = input('Input number (between 1 to 10) to get the multiplication table (Q/q for quit): ')
    if number.lower().startswith("q"):
        break
    if expreg.match(number) is None:  
        print('Try again!!. The data must is in a range from 1 to 10.')
    else:
        try:
            numero = int(number)
            if numero >=1 and numero <=10:
                print('-----------------')
                for x in range(1,11):
                    print(f'| {numero} *{x:3} = {(numero * x):3}', end='')
                    print("  |", end='\n')
                print('-----------------')
            else:
                print('Try again!!. The number is out of range.')
        except ValueError:
            print('Sorry, input number between 1 to 10 or Q/q for quit.')
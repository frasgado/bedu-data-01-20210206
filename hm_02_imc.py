'''
Fecha: 06-Febrero-2021
Elaboró: Fabiola Rasgado
Dado información del usuario, calcular su indice de masa corporal e imprimir su grado de obesidad.
'''
#import textwrap
import re
expreg = re.compile(r'((\d+)(\.\d)?)+$')


peso = input('Introduce tu peso (Kg): ')
altura = input('Introduce tu altura (cm): ')

if expreg.match(peso) is None or expreg.match(altura) is None:  
    print('¡Intentalo otra vez!. Los datos deben ser numéricos.')
else:
    peso = float(peso)
    altura = float(altura)
    imc = round(peso / altura**2, 2)
    if imc <= 18.5:
        label = 'PESO CON INSUFICIENCIA PONDERAL'
        espacio = 12
    elif imc >= 18.5 and imc <= 24.9:
        label = 'PESO CON INTERVALO NORMAL'
        espacio = 10
    elif imc >= 25.0 and imc <= 29.9:
        label = 'CON SOBREPESO'
        espacio = 8
    elif imc >= 30.0 and imc <= 34.9:
        label = 'OBESIDAD GRADO 1 (BAJO RIESGO)'
        espacio = 8
    elif imc >= 35.0 and imc <= 39.9:
        label = 'OBESIDAD GRADO 2 (RIESGO MODERADO)'
        espacio = 6
    elif imc >= 40.0 and imc <= 49.9:
        label = 'OBESIDAD GRADO 3 (ALTO RIESGO, OBESIDAD MORBIDA)'
        espacio = 2
    elif imc >= 50.0:
        label = 'OBESIDAD GRADO 4 (OBESIDAD EXTREMA)'
        espacio = 5
    print('------------------------------------------------------------------------')
    print(f'| Indice Masa Corporal es igual a {imc:.2f}', end='')
    print('{:>33}'.format('|'))
    print(f'| Grado de Obesidad: {label:50}', end='')
    print(f'|')
    print('------------------------------------------------------------------------')
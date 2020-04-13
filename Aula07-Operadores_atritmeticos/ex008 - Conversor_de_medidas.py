"""
ex008 - Escreva um programa que leia o valor em metros e o exiba convertido e cm e mm.
"""
meter = float(input('Digite o valor em metros: '))
centimeter = meter * 100
milimeter = meter * 1000
print()
print(f'A medida de {meter}m, é equivalente a: ....\n{centimeter}cm e \n{milimeter}mm')
print()

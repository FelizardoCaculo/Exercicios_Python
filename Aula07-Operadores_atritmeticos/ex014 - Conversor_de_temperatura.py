"""
ex014 - Escreva um programa que converta uma temperatura digitada e ºC e converta para ºF.
"""
celsius_temperature = float(input('Digite a temperatura em ºC: '))
fahrenheit = (celsius_temperature * 9) / 5 + 32
print(f'A temperatura de {celsius_temperature}ºC, corresponde a {fahrenheit:.1f}ºF.')
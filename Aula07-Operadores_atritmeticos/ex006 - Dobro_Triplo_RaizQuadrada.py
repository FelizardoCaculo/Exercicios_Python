"""
ex006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada.
"""
from math import sqrt
number = int(input('Digite um número: '))
two_times = number * 2
three_times = number * 3
square_root = number ** (1 / 2)
# Cálculo da raíz na rorma Pythonica
square_root1 = sqrt(number)
print(f'O número escolhido foi {number}')
print(f'Seu dobro é: {two_times}\nO triplo é: {three_times}\nE a raíz é: {square_root}')


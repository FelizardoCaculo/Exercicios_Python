"""
ex009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
"""
print('Para calcular a tabuada ... ...')
number = int(input('Digite um número: '))
print()
print('=' * 13)
print(f'{number:02} x { 1:02} = {number *  1:02}')
print(f'{number:02} x { 2:02} = {number *  2:02}')
print(f'{number:02} x { 3:02} = {number *  3:02}')
print(f'{number:02} x { 4:02} = {number *  4:02}')
print(f'{number:02} x { 5:02} = {number *  5:02}')
print(f'{number:02} x { 6:02} = {number *  6:02}')
print(f'{number:02} x { 7:02} = {number *  7:02}')
print(f'{number:02} x { 8:02} = {number *  8:02}')
print(f'{number:02} x { 9:02} = {number *  9:02}')
print(f'{number:02} x {10:02} = {number * 10:02}')
print(f'{number:02} x {11:02} = {number * 11:02}')
print(f'{number:02} x {12:02} = {number * 12:02}')
print('=' * 13)


# Resolvendo com o laço for
"""
print('Para calcular a tabuada ... ...')
number = int(input('Digite um número: '))
print()
print('=' * 13)
for c in range(1, 13):
    print(f'{number:02} x {c:02} = {number * c:02}')
print('=' * 13)

"""
"""
ex007 - Desenvolva um programa que leia as 2 notas de um aluno, calcule e mostre a sua média.
"""
value1 = float(input('Digite a 1ª Nota: '))
value2 = float(input('Digite a 2ª Nota: '))
arithmetic_average = (value1 + value2) / 2
print()
print(f'O aluno que teve na 1ª prova: {value1:.1f} \nE na 2ª prova: {value2:.1f} \nTem a média {arithmetic_average:.1f}')

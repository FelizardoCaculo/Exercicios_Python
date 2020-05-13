"""
ex013 - 13.	Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salary = float(input('Digite o valor do salário actual: '))
new_salary = salary + salary * (15 / 100)
print(f'Um funcionário que ganhava AKZ {salary}, com o aumento de 15%, passa a receber AKZ {new_salary:.2f} ')

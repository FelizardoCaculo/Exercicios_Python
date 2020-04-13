"""
ex004 -
"""
variable = input('Digite qualquer coisa: ')
print()
print(f'O tipo primirivo de {variable}, é: {type(variable)}\n')
print('=' * 40)
print(f'{variable}, é um número?\nR: {variable.isnumeric()}')
print(f'{variable}, é alfabético?\nR: {variable.isalpha()}')
print(f'{variable}, é alfanumérico?\nR: {variable.isalnum()}')
print(f'{variable}, só tem espaços?\nR: {variable.isspace()}')
print(f'{variable}, está em maiúsculas?\nR: {variable.isupper()}')
print(f'{variable}, está em minúsculas?\n: {variable.islower()}')
print(f'{variable}, está capitalizada?\nR: {variable.istitle()}')
print(f'{variable}, é decimal?\nR: {variable.isdecimal()}')
print('=' * 40)

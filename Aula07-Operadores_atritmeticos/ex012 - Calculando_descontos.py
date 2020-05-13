"""
ex012 - 12.	Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
price = float(input('Digite o preço actual: '))
new_price = price - price * (5 / 100)
print(f'O produto que custava AKZ {price}, na promoção com o desconto de 5%, vai custar AKZ {new_price:.2f}')

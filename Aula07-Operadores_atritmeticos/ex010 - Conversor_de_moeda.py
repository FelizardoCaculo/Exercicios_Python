"""
ex010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
"""
kwanza = float(input('Digite o valor em Kwanzas: '))
exchange_rate_dollar = float(input('Qual é o câmbio em dolar: '))
currency_convertor = kwanza / exchange_rate_dollar
print()
print(f'Com o valor AKZ {kwanza:.2f}, voce pode comprar USD {currency_convertor:.2f}')


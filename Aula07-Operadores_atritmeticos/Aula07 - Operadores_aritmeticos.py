""" ############################# Operadores Aritméticos ##############################

" + " Adição
" - " Subtração
" * " Multiplicação
" / " Divisão
" ** " Potência
" // " Divisão inteira
" % " Resto da Divisão

 ############################### Ordem de precedência #################################

1º ()
2º **
3º *, /, **, %
4º +, -

"""
print('Testando os operadores ...')
print('=' * 15)
print('Adição')
print(5 + 2)
print('Subtração')
print(5 - 2)
print('Multiplicação')
print(5 * 2)
print('Divisão')
print(5 / 2)
print('Potência')
print(5 ** 2)
print('Divisão inteira')
print(5 // 2)
print('Resto da divisão')
print(5 % 2)
print('=' * 15)
print('Testando ordem de precedência ... ...')
print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)

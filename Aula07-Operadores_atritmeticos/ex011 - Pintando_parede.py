"""
ex011 - 11.	Faça um programa que leia a largura e a altura de uma parede em metros,
        calcule a área e a quantidade de tinta necessária para pintá-la, sabendo que
        cada litro de tinta, pinta uma área de 2m2.
"""
width = float(input('Digite a largura: '))
height = float(input('Digite a altura: '))
area = width * height
ink = area / 2
print(f'A sua parede tem a dimensão de {width}x{height} e a sua área é de {area} metros quadrado')
print(f'Para pintar essa parede, voce precisará de {ink} litros de tinta.')

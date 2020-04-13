"""
ex005 - Crie um programa que leia um número inteito e mostre na tela o seu antecessor e o seu sucessor
"""
number = int(input('Digite um número: '))
antecessor = number - 1
sucessor = number + 1
print()
print(f'O número informado foi {number}. \nO seu antecessor é: {antecessor} e \nO seu sucessor é: {sucessor}')

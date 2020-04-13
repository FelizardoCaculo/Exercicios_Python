"""
1- print => é a função usada para escrever informações na tela, é uma referência ao comando "escreva".
2 - input => è a função usada para receber dados do usuário e armazenar numa variável, inicialmente ele recebe todos
            dados como "string", mas podemos inserir um tipo primitivo para converter os dados inseridos pelo usuário
3 - Para concatenar usamos "," ou "+".


"""

# Teste prático com Modo interativo
nome = input('Qual é o seu nome? \n').title()
idade = input('Quantos anos voce tem? \n')
peso = input('Qual é o seu peso? \n')
print('Resumindo ... ...')
# print formatado
print(f'Seu nome é {nome}, voce tem {idade} anos de idade e pesa {peso} Kg')



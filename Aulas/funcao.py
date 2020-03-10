# -*- coding: utf-8 -*-

# def soma(x, y):
#     return x + y

# print(soma(10,11))

# produtos = []

# def cadastrar_produto(produto):
#     global produtos
#     produtos.append(produto)


# def deleta_produto(produto):
#     global produtos
#     produtos.remove(produto)

# def listar_produtos():
#     global produtos
#     for p in produtos:
#         print(p)

# cadastrar_produto('abacaxi')
# cadastrar_produto('cajú')
# cadastrar_produto('uva')
# cadastrar_produto('maçã')
# cadastrar_produto('laranja')

# print('\n\n\nprimeira lista \n\n\n')
# listar_produtos()

# deleta_produto('uva')
# print('\n\n\nsegunda lista \n\n\n')

# listar_produtos()

# def linux():
#     teste = 'Red Hat'
#     print(linux)

# def python():
#     print('python') 
#     print(teste)   #teste não será printado por ser escopo local em vez de global

# import requests
# def status_code():
#     SITE = 'https://google.com'
#     return requests.get(SITE)

# print(status_code())


# def linux(): 
#     nome = 'linux'
#     return nome

# def python(): 
#     nome = 'python'
#     return nome

# print(linux())
# print(python())

# def nome(seu_nome): 
    # print(seu_nome)

# def alterarServidor(atual, novo):
#     print('Atual Servidor: ', atual)
#     print('Novo Servidor: ',novo)

# alterarServidor('DNS', 'WEB')

# frutas = []

# def adiciona_frutas(*itens): 
#     global frutas
#     for i in itens: 
#         frutas.append(i)

# adiciona_frutas('abacaxi','limão', 'maçã', 'laranja', 'uva', 'pêssego','cajú','manga')

# print(frutas)


# carros = []
# def adiciona_carros(**modelos):
#     global carros
#     carros.append(modelos)


# adiciona_carros(modelo01='fusca', modelo02='Fox', modelo03='Fiat 147')
# print(carros)


# pessoas = []

# def cadastro(nome, cpf, idade):
#     global pessoas
#     pessoa = dict(user_name= nome, user_cpf=cpf, user_idade= idade)
#     pessoas.append(pessoa)


# cadastro('Renato', '12345678905', 26)
# print(pessoas)


# soma = lambda x,y: x+y
# print(soma(10,20))

numeros = [1,2,3,4,5,6,7,8,9]

# dobro = list(map(lambda x: x*2, numeros))
# print(dobro)

# from functools import reduce
# soma = reduce(lambda x, y: x+y, numeros)
# print(soma)

# n_par = filter(lambda x: x % 2 == 0, numeros)
# print(list(n_par))
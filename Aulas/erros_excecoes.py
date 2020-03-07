# -*- coding: utf-8 -*-

# while True:
#     try:
#         x = int(input('Digite o primeiro número: '))
#         y = int(input('Digite o segundo número: '))
#         print(f'Resultado: {x/y}')
#         break
#     except ValueError as e:
#         print(e)
#         print('Digite apenas números')
#         continue
#     except ZeroDivisionError as z:
#         print(z)
#         print('Impossível realizar divisão por 0')
#         continue
#     finally: 
#         print('Script finalizado')
#         break

funcionarios = ['rafael', 'mariana', 'paulo']

try:
    f = input('Nome: ')
    if f in funcionarios:
        print('você é um funcionário')
    else:
        raise NameError, 'você não é funcionário'
except NameError as n:
    print(n)
    



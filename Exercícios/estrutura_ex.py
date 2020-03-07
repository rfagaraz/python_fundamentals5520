# dada a lista

# times = ['time', ['Corinthians', 'Palmeiras', 'São Paulo'], 'cores', ['Preto', 'Branco', 'Verde', 'Vermelho']]

# # imprima na tela as seguintes mensagens:
# print (f'{times[0]}: {times[1][0]}, {times[2]}: {times[3][0]}, {times[3][1]}')
# print (f'{times[0]}: {times[1][1]}, {times[2]}: {times[3][2]}, {times[3][1]}')
# print (f'{times[0]}: {times[1][2]}, {times[2]}: {times[3][0]}, {times[3][1]}, {times[3][3]}')

# time: <nome_time>, cores: <cores_time> 



# dado o dicionario:

# dados = {
#     "estados": {
#         "sp":{
#             "nome": 'São Paulo',
#             'municipios': 645,
#             "populacao": 44.04
#         },
#         "rj":{
#             "nome": 'Rio de Janeiro',
#             'municipios': 92,
#             "populacao": 16.72
#         },
#         "mg":{
#             "nome": 'Minas Gerais',
#             'municipios': 31,
#             "populacao": 20.87
#         }
#     }

# }

# Imprima as seguintes informações:

# # 1. Nome dos estados
# print(dados)
# print(f'O Nome do primeiro Estado é: {dados["estados"]["sp"]["nome"]}')
# print(f'O Nome do segundo Estado é: {dados["estados"]["rj"]["nome"]}')
# print(f'O Nome do terceiro Estado é: {dados["estados"]["mg"]["nome"]}')




# # 2. Nome dos estados, quantidade de municipios e população
# print(f'O nome, quantidade de municípios e população do estado, respectivamente é: {dados["estados"]["sp"].values()}')
# print(f'O nome, quantidade de municípios e população do estado, respectivamente é: {dados["estados"]["rj"].values()}')
# print(f'O nome, quantidade de municípios e população do estado, respectivamente é: {dados["estados"]["mg"].values()}')

# print('Exercício 1!')
# nota1 = float(input('Digite a nota de sua primeira prova: '))
# nota2 = float(input('Digite a nota de sua segunda prova: '))
# nota3 = float(input('Digite a nota de sua terceira prova: '))
# nota4 = float(input('Digite a nota de sua quarta prova: '))

# if (nota1+nota2+nota3+nota4)/4 >= 7:
#     print('Você foi aprovado ao final do ano!')
# else:
#     print('Você foi reprovado ao final do ano =(')

print('\n\n\nExercício 2!')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print('Seu primeiro número é maior que seu segundo número')
elif num1 < num2:
    print('Seu segundo número é maior que seu segundo número')
else:
    print('Seus números são idênticos')
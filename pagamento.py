#!python3
# -*- coding: utf-8 -*-



while True:
    try:
        salarioHora = float(input('Digite o quanto você recebe por hora:'  ))
        horasTrabalhadas = float(input('Digite quantas horas você trabalha mensalmente: '))
        break
    except ValueError as e:
        print(e)
        print('Favor insira apenas números!')
        continue

salarioBruto = (salarioHora * horasTrabalhadas)
fgts = (salarioBruto * 0.11)
sindicato = (salarioBruto * 0.03)

if salarioBruto <= 1900:
    descontoIR = 0
elif salarioBruto <= 2800:
    descontoIR = 0.7
elif salarioBruto <= 3700:
    descontoIR = 0.15
elif salarioBruto <= 4600:
    descontoIR = 0.22
else:
    descontoIR = 0.27

totalDescontos =  (salarioBruto * descontoIR) + sindicato
print('\n\n\n'+ ('-'*20))
print(f'Valor da hora: R${salarioHora}')
print(f'Quantidade de horas trabalhadas: {horasTrabalhadas}')
print(f'Salário Bruto: ({horasTrabalhadas} * {salarioHora}): R${salarioBruto}')
print(f'(-)IR: ({descontoIR *100}%): R${salarioBruto * descontoIR}')
print(f'(-)Sindicato: (3%): R${sindicato}')
print(f'FGTS: (11%): R${fgts}')
print(f'Total de descontos: R${totalDescontos}')
print(f'Salário Líquido: R${salarioBruto - totalDescontos}')

print('\n\n\n'+ ('-'*20))
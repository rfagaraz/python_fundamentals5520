#!python3
# -*- coding:utf-8 -*-
import datetime as dt

class ClientBankAccount():
    def __init__(self, bank_Account, client_Name, client_Balance=0): 
        self.bankID = '999'
        self.bankAgency = '08'
        self.bankAccount = bank_Account
        self.clientName = client_Name
        self.clientBalance = client_Balance

    def deposit(self, amount):
        try:
            self.clientBalance += int(amount)
            print('-'*20)
            print(f'Foram depositados R${amount},00 reais.')
        except ValueError as e:
            print('Apenas valores numéricos!')
   

    def withdraw(self, amount):
        if self.clientBalance >= amount:
            try:
                self.clientBalance -= int(amount)
                print('-'*20)
                print(f'Foram sacados R${amount},00 reais.')
            except ValueError:
                print('Apenas valores numéricos!')
        else:
            print('Saldo insuficiente.')
            print('-'*20)

    def bankStatement(self): 
        print('-'*20)
        print(f'Banco Old Bank - {self.bankID}')
        print(f'Data de consulta: {dt.datetime.now()}')
        print(f'Agência: {self.bankAgency} Conta: {self.bankAccount}')
        print('O seu saldo é de R${},00 reais.'.format(self.clientBalance))
    



print('OldBank')
print('Bem vindo(a)!')
accountInput = (input('Favor digite o número de sua conta: '))
nameInput = (input('Favor digite seu nome: '))
access = ClientBankAccount(accountInput, nameInput)



while True:
    print('Selecione a opção abaixo:')
    print('Para extrato digite 1')
    print('Para saque digite 2')
    print('Para deposito digite 3')
    print('Para sair digite 0')
    menu = input()
    if menu == '1':
        access.bankStatement()
    elif menu == '2':
        access.withdraw(int(input('Digite quanto você deseja sacar:\n')))
    elif menu == '3':
        access.deposit(int(input('Digite o quanto você deseja depositar:\n ')))
    elif menu == '0':
        print('Encerrando acesso!')
        exit()
    else:
        print('Não foi possível identificar a operação digitada')

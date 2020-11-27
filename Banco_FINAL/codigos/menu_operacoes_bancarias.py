from operacoes_bancarias import *
from tratamentos import limpar_tela, positivo

def operacoes_bancarias(numero_conta):
    menu = 0
    while True:
        limpar_tela()
        print('****OPERAÇÕES BANCARIAS!****')
        print('1 - Deposito')
        print('2 - Saque')
        print('3 - Transferencia')
        print('4- Extrato')
        print('0 -Sair!')
        menu = input('Digide a operação desejada:')
        if (menu == '1'):
            limpar_tela()
            print('***DEPOSITO:***')
            valor = input('Digite o valor a ser depositado na sua conta: ')
            valor = positivo(valor)
            senha= input('Digite sua senha: ')
            deposito(valor, numero_conta,senha)

        if (menu == '2'):
            limpar_tela()
            print('**SAQUE***')
            valor = input('Digite o valor a ser sacado da sua conta: ')
            valor = positivo(valor)
            saque(valor, numero_conta)

        if (menu == '3'):
            limpar_tela()
            print('**TRANSFERENCIA***')
            conta_destino = input('Digite o numero da conta que recebera a transferencia: ')
            valor = input('Digite o valor a ser transferido: ')
            valor = positivo(valor)
            transferencia(valor, conta_destino, numero_conta)


        if (menu == '4'):
            ler_extrato(numero_conta)
            break

        if (menu == '0'):
            break


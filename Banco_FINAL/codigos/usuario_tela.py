from menu_operacoes_bancarias import operacoes_bancarias
from menu_configuracoes import configuracoes_usuario
from tratamentos import limpar_tela

def tela_usuario(numero_conta):
    menu = 0
    while True:
        limpar_tela()
        print('***MENU USUARIO - BEM VINDO!!!****')
        print('1 - Operacoes Bancarias')
        print('2 - Configuracoes do Usuario')
        print('0 -Sair!')
        menu = input('Digide a operação desejada:')

        if (menu == '1'):
            operacoes_bancarias(numero_conta)

        if (menu == '2'):
            configuracoes_usuario(numero_conta)

        if (menu == '0'):
            break



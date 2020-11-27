from login import funcao_login
from cadastrar import funcao_cadastrar
from tratamentos import limpar_tela

menu = 0
while True:

        print('BEM VINDO!')
        print('1 - Login')
        print('2 - Cadastro')
        print('0 -Sair!')
        menu= input('Digide a operação desejada:')
        if(menu == '1'):
                funcao_login()
        if(menu == '2'):
                funcao_cadastrar()
        if(menu == '0'):
                break
        limpar_tela()



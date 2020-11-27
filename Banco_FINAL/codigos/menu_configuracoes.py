from alteracao_dados import alterar_informacoes
from leitura_e_escrita import remover_pasta
from tratamentos import limpar_tela

def configuracoes_usuario(numero_conta):
    while True:
        limpar_tela()
        print('***CONFIGURAÇÕES DE CONTA**** ')
        print('1 - Alterar Informações Pessoais')
        print('2 - Encerrar Conta')
        print('0 -Sair!')
        menu = input('Digide a operação desejada:')

        if (menu == '1'):
            alterar_informacoes(numero_conta)
        if (menu == '2'):
            remover_pasta(numero_conta)

        if (menu == '0'):
            break


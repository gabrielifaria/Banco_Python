from verificacao import verificar_senha
from leitura_e_escrita import *
from cadastrar import *
from tratamentos import limpar_tela

def mudar_dados(nome_pasta,nome_arquivo, dado):
    senha = input('Para realizar mudanças digite sua senha: ')
    if verificar_senha(nome_pasta, senha) is True:

        escrever_arquivo(nome_pasta, nome_arquivo, dado)

    else:
        print('Senha Invalida, Erro!')

def mudar_senha(nome_pasta,nome_arquivo,dado):
    escrever_arquivo(nome_pasta, nome_arquivo, dado)




def alterar_numero_conta(nome_pasta):
    novo_numero = gerar_numero_conta()
    renomear_pasta(nome_pasta, novo_numero)
    print('O novo número da sua conta é:', novo_numero)



def alterar_informacoes(nome_pasta):
    menu = 0
    while True:
        print('Quais informações deseja mudar?')
        print('1 - Nome')
        print('2 - Email')
        print('3 - Senha')
        print('4- Gerar novo numero de conta')
        print('0 -Voltar')
        menu = input('Digite a operação desejada: ')
        limpar_tela()

        if (menu == '1'):
            nome = input('Digite seu nome atual: ')
            mudar_dados(nome_pasta,'nome', nome)
            limpar_tela()

        if (menu == '2'):
            email = input('Digite seu email atual: ')
            mudar_dados(nome_pasta, 'email', email)
            limpar_tela()

        if (menu == '3'):
            senha = input('Digite sua senha atual: ')
            if verificar_senha(nome_pasta, senha) is True:

                senha = input('Digite a nova senha: ')
                mudar_senha(nome_pasta,'senha', senha)
            else:
                print('Senha incorreta!')
            limpar_tela()

        if (menu == '4'):

            print('Seu novo numero de conta é: ')
            renomear_pasta(nome_pasta, gerar_numero_conta())
            limpar_tela()

        if (menu == '0'):
            break

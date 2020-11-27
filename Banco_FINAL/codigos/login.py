from verificacao import verificar_senha

from usuario_tela import tela_usuario
from tratamentos import limpar_tela

def funcao_login():
    limpar_tela()
    print('***LOGIN***')
    numero_conta = input('Informe o número de sua conta: ').strip()
    senha = input('Informe a sua senha: ').strip()

    if(verificar_senha(numero_conta, senha) is True):
        tela_usuario(numero_conta)
    else:
        print('Senha Incorreta')




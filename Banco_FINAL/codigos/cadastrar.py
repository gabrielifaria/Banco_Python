import os
import random
from leitura_e_escrita import escrever_arquivo
from tratamentos import *

def cadastro(nome, email, cpf, data_nascimento, senha, saldo, extrato, nome_pasta):
    nome_pasta = nome_pasta
    os.mkdir(f'usuarios\\{nome_pasta}')

    escrever_arquivo(nome_pasta, 'nome', nome)
    escrever_arquivo(nome_pasta, 'email', email)
    escrever_arquivo(nome_pasta, 'cpf', cpf)
    escrever_arquivo(nome_pasta, 'data_nascimento', data_nascimento)
    escrever_arquivo(nome_pasta, 'senha', senha)
    escrever_arquivo(nome_pasta, 'saldo', saldo)
    escrever_arquivo(nome_pasta, 'extrato', extrato)
    print('Seu numero de conta é: ',nome_pasta)

    os.system('pause')
    os.system('cls')
    return True

def gerar_numero_conta():

    while True:

        numero_conta = random.randrange(10000, 99999)
        numero_conta = str(numero_conta)
        print(numero_conta)

        caminho = 'usuarios\\' + numero_conta

        existe = os.path.exists(caminho)
        if not existe:
            break

    return numero_conta


def funcao_cadastrar():
    limpar_tela()

    print('***CADASTRAR CONTA***')

    nome = input('Informe o seu nome: ').strip().title()

    email = input('Informe o seu e-mail: ').strip()

    cpf = input('Informe seu CPF: ').strip()
    eh_numerico(cpf)


    data_nascimento = input('Informe a data de seu nascimento no formato (dia/mês/ano): ').strip()

    senha = input('Digite sua senha: ').strip()

    confirma = input('Confirme a senha: ').strip()
    confirma_senha(senha, confirma)

    saldo = input('Informe seu Saldo inicial: ').strip()

    eh_numerico(saldo)

    extrato = f'SALDO INICIAL: {saldo}'

    cadastro(nome, email, cpf, data_nascimento, senha, saldo, extrato, gerar_numero_conta())




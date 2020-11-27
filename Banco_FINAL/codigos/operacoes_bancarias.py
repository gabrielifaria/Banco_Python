from verificacao import verificar_senha
from leitura_e_escrita import *
from tratamentos import limpar_tela

def somar_saldo(saldo, nome_pasta):
    saldo = float(saldo)
    diretorio = f'usuarios\\{nome_pasta}\\saldo.txt'
    valor = float(lerArquivo(diretorio))
    salvar_conteudo = valor + saldo

    salve = str(salvar_conteudo)

    escrever_arquivo(nome_pasta, 'saldo', salve)


def subtrair_saldo(saldo, nome_pasta):
    saldo = float(saldo)
    diretorio = f'usuarios\\{nome_pasta}\\saldo.txt'
    valor = float(lerArquivo(diretorio))

    salvar_conteudo = valor - saldo

    salve = str(salvar_conteudo)

    escrever_arquivo(nome_pasta, 'saldo', salve)


def atualizar_saldo(saldo, nome_pasta):
    escrever_arquivo(nome_pasta, 'saldo', saldo)


def ver_saldo(nome_pasta):
    #saldo = float(saldo)
    diretorio = f'usuarios\\{nome_pasta}\\saldo.txt'

    valor = float(lerArquivo(diretorio))
    return valor

def atualizar_extrato(texto, nome_pasta):
    acrescentar_texto_arquivo(nome_pasta, texto)

def ler_extrato(nome_pasta):
    limpar_tela()
    print('EXTRATO BANCARIO:')
    diretorio = f'usuarios\\{nome_pasta}\\extrato.txt'
    print(lerArquivo(diretorio))

def transferencia(valor,conta_destino,conta_origem):

    saldo = float(ver_saldo(conta_origem))
    valor = float(valor)
    valor2= valor
    if (saldo >= valor):
        saldo_atual = ver_saldo(conta_origem) - valor
        saldo_atual = str(saldo_atual)
        atualizar_saldo(saldo_atual, conta_origem)
        valor = str(valor)
        extrato = f'\nTransferencia efetuada: R$ - {valor} *** NOVO SALDO: R$ {ver_saldo(conta_origem)}'
        atualizar_extrato(extrato, conta_origem)
        print(extrato)

        saldo_atual = ver_saldo(conta_destino) + valor2
        saldo_atual = str(saldo_atual)
        atualizar_saldo(saldo_atual, conta_destino)
        valor2 = str(valor2)
        extrato = f'\nTransferencia recebida: R$ - {valor2} *** NOVO SALDO: R$ {ver_saldo(conta_destino)}'
        atualizar_extrato(extrato, conta_destino)


    else:
        print("Saldo Insufuciente!")


def saque(valor_saque, nome_pasta):
    saldo=float(ver_saldo(nome_pasta))
    valor_saque = float(valor_saque)
    if ( saldo >= valor_saque):
        saldo_atual = ver_saldo(nome_pasta) - valor_saque
        saldo_atual=str(saldo_atual)
        atualizar_saldo(saldo_atual, nome_pasta)

        valor_saque=str(valor_saque)

        extrato = f'\nSaque efetuado: R$ - {valor_saque} *** NOVO SALDO: R$ {ver_saldo(nome_pasta)}'
        atualizar_extrato(extrato, nome_pasta)
        print(extrato)
    else:
        print("Saldo Insufuciente!")


def deposito(valor, nome_pasta, senha):
    if verificar_senha(nome_pasta, senha) is True:
        somar_saldo(valor, nome_pasta)
        extrato = f'\nDeposito efetuado: R$ + {valor} *** NOVO SALDO: R$ {ver_saldo(nome_pasta)}'
        atualizar_extrato(extrato, nome_pasta)
        print(extrato)
    else:
        print("Erro!")


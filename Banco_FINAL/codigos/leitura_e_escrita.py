import os

def lerArquivo(local):

    arquivo = open(local, 'r')
    conteudo_arquivo = arquivo.read()
    arquivo.close()

    return conteudo_arquivo

def criar_arquivo(nome_pasta, nome_arquivo):
    diretorio = f'usuarios\\{nome_pasta}\\{nome_arquivo}.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(nome_arquivo)
    arquivo.close()


def escrever_arquivo(nome_pasta, nome_arquivo, texto):
    diretorio = f'usuarios\\{nome_pasta}\\{nome_arquivo}.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def limpar_pasta(nome_pasta):
    diretorio = f'usuarios\\{nome_pasta}'
    arquivos =  ['cpf.txt', 'data_nascimento.txt', 'email.txt', 'extrato.txt', 'nome.txt','saldo.txt','senha.txt']
    for nome_arquivo in arquivos:
        arquivo = f'{diretorio}\\{nome_arquivo}'
        os.remove(arquivo)

def acrescentar_texto_arquivo(nome_pasta, texto):
    diretorio = f'usuarios\\{nome_pasta}\\extrato.txt'
    arquivo = open(diretorio, 'a')
    arquivo.write(texto)
    arquivo.close()

def remover_pasta(nome_pasta):
        limpar_pasta(nome_pasta)
        diretorio = f'usuarios\\{nome_pasta}'
        os.removedirs(diretorio)


def renomear_pasta(nome_pasta,novo_nome):
        diretorio = f'usuarios\\{nome_pasta}'
        novo_nome = f'usuarios\\{novo_nome}'
        os.rename(diretorio,novo_nome)


def renomear_arquivo(nome_pasta,nome_arquivo,novo_nome):
        diretorio = f'usuarios\\{nome_pasta}\\{nome_arquivo}.txt'
        novo_nome= f'usuarios\\{nome_pasta}\\{novo_nome}.txt'
        os.rename(diretorio,novo_nome)


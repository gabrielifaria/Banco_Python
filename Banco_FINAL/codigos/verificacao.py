import os

def verificar_numero_conta(nome_pasta):
    caminho = 'usuarios\\' + nome_pasta
    existe = os.path.exists(caminho)
    if not existe:
        print('essa conta não existe')

        return False
    else:
        return True


def verificar_senha(nome_pasta, senha):
    if verificar_numero_conta(nome_pasta) is True:
        diretorio = f'usuarios\\{nome_pasta}\\senha.txt'
        arquivo = open(diretorio,'r')

        conteudo = arquivo.read()

        if (conteudo == senha):
            #print('Senha Correta!')
            return True
        else:
            #print('Senha Errada!')
            return False

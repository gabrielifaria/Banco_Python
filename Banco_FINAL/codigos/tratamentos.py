import os

def limpar_tela():
    os.system('pause')
    os.system('cls')

def positivo(num):
    num = float(num)
    while num < 0:
        num = float(input('Digite um valor positivo! novo valor: '))
    return num

def eh_numerico(num):
    while not num.isnumeric():
        print('Entrada Inválida! O valor precisa ser numerico!')
        num = input('digite a entrada novamente: ').strip()

def confirma_senha(senha,confirma):
    while senha != confirma:
        print('Senha Inválida! Senha incorreta!')
        confirma = input('Didite a senha novamente: ').strip()

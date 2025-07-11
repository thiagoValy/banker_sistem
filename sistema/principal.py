from menu import *
from funcao import *

saldo = 0
deposito = 0
numero_saques = 0
limite = 500
LIMITE_SAQUES = 3
usuarios = []
contas = []
extrato = []
AGENCIA = "0001"

while True:
    resposta = menu(["ExTRATO", "DEPÓSITO", "SAQUE", "CRIAR USUARIO", "CRIAR CONTA", "LISTAR CONTAS", "SAIR"])

    if resposta == 1:
        exibir_extrato(saldo, extrato=extrato)

    elif resposta == 2:
        valor = float(input("Digite o valor a ser depositado: R$ "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif resposta == 3:
        valor = float(input("Qual o valor do saque: R$ "))
        saque(saldo=saldo, valor=valor,extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)
    elif resposta == 4:
        criar_usuario(usuarios)
    
    elif resposta == 5 :
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
            
    elif resposta == 6:
        listar_contas(contas)
            
    
    elif resposta == 7:
        print("Sair do sistema")
        break
    else:
        print("digite uma opção valida")

from menu import *
deposito = 0
saldo = 0
cont  = 0
cont1 = 0
valor = 0
extrato =[]

while True:
    reposta = menu(["ESTRATO", "DEPÓSITO", "SAQUE", "SAIR"])

    if reposta == 1:
        print("extrato")
    elif reposta == 2:
        print("deposito")
    elif reposta == 3:
        print("saque")
    elif reposta == 4:
        print("Sair do sistema")
        break
    else:
        print("digite uma opção valida")

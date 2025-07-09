deposito = 0
saldo = 0
cont  = 0
cont1 = 0
valor = 0
extrato =[]




print(f"===" * 10)
print("Bem vindo ao Banco Melanin")
print(f"===" * 10)
print("MENU")
print("1 - EXTRATO \n"
"2 - DEPOSITO \n"
"3 - SACAR \n"
"4 - SAIR")


while True:
    opcao = int(input("Olá!! Qual a opção que deseja escolher " ))
    if opcao == 1:
        print(f"========== EXTRATO ============" )
        for moviento in extrato:
            print(moviento)
        print(f"Saldo Total ********* R$ {saldo}")
        
    elif opcao == 2:
        deposito = int(input("Quanto deseja depositar: "))
        if deposito > 0 :
            saldo += deposito
            extrato.append(f"Deposito ********* R${deposito}")
            cont += 1
            print("Deposito Realizado com Sucesso")
            print()
            print("Deseja realizar outro deposito: Digite 2 se não escolha outra opção")
        else:
            print("Valor invalido!! Provavelmente você digitou um valor negativo tente outra vez")
    
    elif opcao == 3:
            if saldo > 0:
              if cont1 == 3 :
                    print("LIMITE TOTAL DE SAQUES EXCEDIDO!!! \n" 
                    " TENTE AMANHA NOVAMENTE")
              else:
                valor  = int(input("Quanto deseja sacar: "))
                if valor > 0:
                    if valor <= 500:
                        saldo -= valor
                        cont1 += 1 
                        print("Saque Realizado com Sucesso")
                        extrato.append(f"Saque ********** R$ {valor}")
                    
                    elif valor > saldo:
                        print("VOCÊ NÃO TEM SALDO SUFICIENTE!!!")
                    
                    else:
                        print("LIMETE EXCEDIDO")
                if valor < 0 :
                    print("VALOR INVALIDO ")

    
    else:
        print("sair")
        break
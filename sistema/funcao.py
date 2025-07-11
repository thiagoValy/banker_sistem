from menu import *
def depositar(saldo, valor, extrato,/):
    deposito = valor
    if valor > 0:
        saldo += valor
        extrato.append(f"Deposito ********* R${deposito}")
        print("/n Deposito realizado com Sucesso")
    else:
        print("Valor invalido!!! Digite um valor válido!!!")

    return saldo, extrato


def saque(*,saldo,valor,extrato,limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("saldo insuficiente!!")
    elif execedeu_limite:
        print("Operação invalida você excedeu o limite de valor!!!")

    elif excedeu_saques:
        print("Excedeu o limite total de saques!!")

    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque ********** R$ {valor}")
        print("Saque realizado com sucesso")
    
    else:
        print("Operação invalida!! Digite um valor valido!!!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f"========== EXTRATO ============" )
    for moviento in extrato:
        print(moviento)
    print(f"Saldo Total ********* R$ {saldo}")


def filtrar_usuario(cpf, usuarios):
        usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF(somente numero): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuario com esse CPF")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd - mm - aaaa:  ")
    endereço = input("Informe seu Endereço(Logradouro, Nº - Bairro - Cidade): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf})

    print("Usuaro Criado com Sucesso!!!!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta Criada com Sucesso!!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado, criação de conta encerrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\ 
        Agencia: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
    """
        
        print("=" * 42)
        print(linha)
    
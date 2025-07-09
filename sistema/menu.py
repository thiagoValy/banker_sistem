def validar(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, Digite uma opçao válida.\ 033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[Usuario não digiteou opção. \033[m")
            return 0 
        else:
            return n 


def linha(tam = 10):
    return '===' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def menu(lista):
    cabecalho("Menu")
    c = 1 
    for item in lista:
        print(f"{c} - {item}")
        c += 1 
    print(linha())
    opc = validar("Digite um Opção: ")
    return opc

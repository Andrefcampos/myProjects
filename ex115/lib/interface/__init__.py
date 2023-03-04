def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\33[31mERRO. Por favor, digite uma opção válida.\33[m')
        except KeyboardInterrupt:
            print('\n\33[31mUsuário preferiu não digitar esse número.\33[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\33[33m{c} - \33[34m{item}\33[m')
        c += 1
    print(linha())
    opc = leiaInt('\33[32mSua opçã0: \33[m')
    return opc

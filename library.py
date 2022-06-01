def leia_int(txt):
    while True:
        try:
            i = int(input(txt))
        except (TypeError, ValueError):
            print(pinta('ERRO. DIGITE UM NÚMERO VÁLIDO', 'red'))
            continue
        except (KeyboardInterrupt):
            print(pinta('Operação cancelada pelo usuário.', 'red'))
            return 0
        else:
            return i


def leia_float(txt):
    while True:
        try:
            i = float(input(txt).replace(',', '.'))
        except (TypeError, ValueError):
            print(pinta('ERRO. DIGITE UM NÚMERO VÁLIDO', 'red'))
            continue
        except (KeyboardInterrupt):
            print(pinta('Operação cancelada pelo usuário.', 'red'))
            return 0
        else:
            return i


def pinta(txt, cor):
    cores = [
        {'cor': 'red', 'cod': f'\033[31m{txt}\033[m'},
        {'cor': 'blue', 'cod': f'\033[34m{txt}\033[m'},
        {'cor': 'yellow', 'cod': f'\033[33m{txt}\033[m'},
        {'cor': 'white', 'cod': f'\033[30m{txt}\033[m'},
        {'cor': 'purple', 'cod': f'\033[35m{txt}\033[m'},
        {'cor': 'green', 'cod': f'\033[32m{txt}\033[m'},
        {'cor': 'cian', 'cod': f'\033[36m{txt}\033[m'}
            ]
    for c in cores:
        if c['cor'] == cor:
            return c['cod']


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.upper().center(42))
    print(linha())


def menu(itens, txt):
    cabecalho(txt)
    for n, i in enumerate(itens):
        print(f'{pinta(n + 1, "yellow")} - {i}')
    print(linha())
    step1 = leia_int('Escolha uma opção da lista: ')
    return step1


def cria_arq(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except:
        print(f'Primeiro uso do programa.\n' +
              pinta(f'Criaremos um banco de dados com nome "{nome}.txt"', 'green'))
        try:
            arq = open(nome, 'wt+')
            arq.close()
        except Exception as erro:
            print(pinta('ERRO AO CRIAR O ARQUIVO', 'red'))
            print(f'O erro foi: {erro.__class__}')


def cadastro(arq, prod, price, qtd=0):
    ler_arquivo = open(arq, 'rt')
    alt_arquivo = open(arq, 'at')
    produto_novo = True
    for linha in ler_arquivo:
        dado = linha.split(';')
        if dado[0].lower() == prod.lower():
            produto_novo = False
    if produto_novo:
        alt_arquivo.write(f'{prod};{price:.2f};{qtd}\n')
        print('Cadastro concluído')
    else:
        print(pinta('ESTE PRODUTO JÁ FOI CADASTRADO!', 'red'))
        print('Utilize a opção de atualizar estoque no menu principal')
    ler_arquivo.close()
    alt_arquivo.close()


def imprime_arq(arq):
    arquivo = open(arq, 'rt')
    cabecalho('produtos em estoque')
    print(f'{"CÓDIGO":^10}{"PRODUTO":<10}{"PREÇO":<10}{"QUANTIDADE":^10}')
    for n, l in enumerate(arquivo):
        dado = l.split(';')
        dado[2] = dado[2].replace('\n', '')
        print(f'{n+1:^10}{dado[0]:<10}{"R$"+dado[1]:<10}{dado[2]:^10}')
    arquivo.close()


def edit_arq(arq, cod):
    with open(arq, 'r') as arquivo:
        lista = arquivo.readlines()

        for l, p in enumerate(lista):
            p = p.replace('\n', '')
            lista[l]= p.split(';')
        cabecalho('produto selecionado')
        print(f'{"CÓDIGO":^10}{"PRODUTO":<10}{"PREÇO":<10}{"QUANTIDADE":^10}')
        print(f'{cod:^10}{lista[cod-1][0]:<10}{"R$" + lista[cod-1][1]:<10}{lista[cod-1][2]:^10}')
        opc = ['Mudar nome do produto', 'Mudar preço', 'Atualizar quantidade em estoque', 'concluir alteração']

        while True:
            choice = menu(opc, 'O que deseja alterar?')
            if choice == 1:
                lista[cod-1][0] = input('Digite o novo nome do produto: ')
                print(f'{"CÓDIGO":^10}{"PRODUTO":<10}{"PREÇO":<10}{"QUANTIDADE":^10}')
                print(f'{cod:^10}{lista[cod - 1][0]:<10}{"R$" + lista[cod - 1][1]:<10}{lista[cod - 1][2]:^10}')

            if choice == 2:
                lista[cod-1][1] = leia_float('Digite o novo preço do produto: R$')
                print(f'{"CÓDIGO":^10}{"PRODUTO":<10}{"PREÇO":<10}{"QUANTIDADE":^10}')
                print(f'{cod:^10}{lista[cod - 1][0]:<10}{"R$" + lista[cod - 1][1]:<10}{lista[cod - 1][2]:^10}')
            if choice == 3:
                lista[cod-1][2] = leia_int('Digite a nova quantidade do produto: ')
                print(f'{"CÓDIGO":^10}{"PRODUTO":<10}{"PREÇO":<10}{"QUANTIDADE":^10}')
                print(f'{cod:^10}{lista[cod - 1][0]:<10}{"R$" + lista[cod - 1][1]:<10}{lista[cod - 1][2]:^10}')
            if choice == 4:
                print(pinta('ATUALIZAÇÃO CONCLUÍDA', 'green'))
                break

        with open(arq, 'w') as arquivo:
            for item in lista:
                arquivo.write(f'{item[0]};{item[1]};{item[2]}\n')



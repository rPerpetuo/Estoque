from library import *


arq = 'dados.txt'
cria_arq(arq)
itens_menu = ['Cadastrar novo produto', 'Atualizar estoque', 'Consultar estoque', 'Encerrar programa']


while True:
    menu_principal = menu(itens_menu, 'menu inicial')
    if menu_principal == 1:
        prod = input('Digite o nome do novo produto: ')
        price = leia_float('Digite o preço do produto: R$ ')
        qtd = leia_int('Digite a quantidade do produto em estoque: ')
        cadastro(arq, prod, price, qtd)

    elif menu_principal == 2:
       choice = leia_int('Digite o código do produto (999 para cancelar): ')
       if choice == 999:
           pass
       else:
           edit_arq(arq, choice)

    elif menu_principal == 3:
        imprime_arq(arq)

    elif menu_principal == 4:
        print('Programa encerrado pelo usuário.\nVOLTE SEMPRE')
        break
    else:
        print(pinta('Item inexistente', 'red'))


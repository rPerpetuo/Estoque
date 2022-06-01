from library import *


arq = 'dados.txt'
cria_arq(arq)
itens_menu = ['Cadastrar novo produto', 'Atualizar estoque', 'Consultar estoque', 'Encerrar programa']


while True:
    menu_principal = menu(itens_menu)
    if menu_principal == 1:
        prod = input('Digite o nome do novo produto: ')
        price = leia_float('Digite o preço do produto: R$ ')
        qtd = leia_int('Digite a quantidade do produto em estoque: ')
        cadastro(arq, prod, price, qtd)

    elif menu_principal == 2:
        pass #função de att a qtd de cada produto no estoque
    elif menu_principal == 3:
        pass #função de printar o estoque
    elif menu_principal == 4:
        print('Programa encerrado pelo usuário.\nVOLTE SEMPRE')
        break
    else:
        print(pinta('Item inexistente', 'red'))


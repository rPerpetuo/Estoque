from library import *

itens_menu = ['Cadastrar novo produto', 'Atualizar estoque', 'Consultar estoque', 'Encerrar programa']

while True:
    menu_principal = menu(itens_menu)
    if menu_principal == 1:
        pass #função de cadastro
    elif menu_principal == 2:
        pass #função de att a qtd de cada produto no estoque
    elif menu_principal == 3:
        pass #função de printar o estoque
    elif menu_principal == 4:
        print('Programa encerrado pelo usuário.\nVOLTE SEMPRE')
        break
    else:
        print(pinta('Item inexistente', 'red'))
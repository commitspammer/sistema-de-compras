import replit
from functions.utility import *
from functions.database import *
from time import sleep

# Variables
is_running = True
state = 'MENU'
cart = []

# Functions
create_arq('products.txt')
replit.clear()

# Main
while is_running:


  while state == 'MENU':
    clear()
    title('Menu')
    display(['Ver estoque', 'Ver carrinho', 'Sair do programa'])
    x = int_input('Opção: ')
    if x == 1:
      state = 'SEARCH'
      break
    elif x == 2:
      state = 'CART'
      break
    elif x == 3:
      is_running = False
      break
    else:
      print(color('red', 'Opção inválida. Digite novamente'))

  
  while state == 'SEARCH':
    clear()
    title('Estoque')
    display(['Pesquisar produto', 'Voltar ao menu'])
    x = int_input('Opção: ')
    if x == 1:
      text = str(input('Barra de pesquisa: '))
      state = 'ADD'
      break
    elif x == 2:
      state = 'MENU'
      break
    else:
      print(color('red', 'Opção inválida. Digite novamente'))


  while state == 'ADD':
    clear()
    title('Resultados')
    print_products(search(text, 'products.txt'))
    display(['Adicionar produto ao carrinho', 'Voltar à pesquisa'])
    x = int_input('Opção: ')
    if x == 1:
      id = int_input('Digite o número do produto: ')
      quant = int_input('Digite a quantidade de itens: ')
      add_product(id, quant, cart, 'products.txt')
      state = 'SEARCH'
      break
    elif x == 2:
      state = 'SEARCH'
      break
    else:
      print(color('red', 'Opção inválida. Digite novamente'))


  while state == 'CART':
    clear()
    title('Carrinho')
    print_products(cart)
    display(['Remover produto do carrinho', 'Finalizar compra', 'Voltar ao menu'])
    x = int_input('Opção: ')
    if x == 1:
      id = int_input('Digite o número do produto: ')
      del_product(id, cart, 'products.txt') 
      state = 'CART'
      break
    elif x == 2:
      state = 'PAYMENT'
      break
    elif x == 3:
      state = 'MENU'
    else:
      print(color('red', 'Opção inválida. Digite novamente'))
    
    
  while state == 'PAYMENT':
    clear()
    title('Pagamento')
    print_prices(5, cart)
    display(['Pagar no crédito', 'Pagar no boleto', 'Voltar ao carrinho'])
    x = int_input('Opção: ')
    if x == 1:
      print(color('green', 'Pagamento realizado!'))
      is_running = False
      break
    elif x == 2:
      print(color('green', 'Pagamento realizado!'))
      is_running = False
      break
    elif x == 3:
      state = 'CART'
      break
    else:
      print(color('red', 'Opção inválida. Digite novamente'))


clear()
title('Obrigado!')
title('Volte sempre!')

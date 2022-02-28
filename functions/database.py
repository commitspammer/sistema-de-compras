from functions.utility import *

def create_arq(name):
  try:
    f = open(name, 'w')
  except:
    print(color('red', 'ERRO! Não foi possível criar arquivo!'))
  else:
    f.write('''ID-NOME-PRECO-QUANT-
###
1-Camisa vermelha-34.99-30-
2-Sapato Oxford-134.99-20-
3-Calça jeans-169.99-25-
4-Casaco preto-199.00-15-
5-Tênis Nike-80.00-10-
6-Salgado de frango-2.00-100-
7-Biscoito de morango-3.99-45-
8-Maçã-1.15-18-
9-Laranja-1.25-17-
10-Sanduíche de patê-10.00-12-
11-Refrigerante de coca-5.50-15-
12-Cremosinho-1.99-25-
13-Halls-2.00-5-
14-Chocolate amargo-4.00-10-
15-Energético Monster-11.90-3-
16-Feijão marrom-2.30-15-
17-Arroz branco-2.10-19-
18-Bife-21.45-10-
19-Peito de frango-22.20-15-
20-Fio dental-1.50-8-
21-Escova de dente-7.75-9-
22-Sabonete erva doce-1.25-20-
23-Shampoo-8.88-11-
24-Condicionador-7.99-14-
25-Amaciante-13.75-5-
26-Água sánitaria-9.90-7-
27-Saco de lixo-3.33-50-
28-Sandália Havaianas-19.30-25-
29-Pipoca de microondas-13.60-12-
30-Suco em caixa-5.25-17-
31-Panetone-19.99-50-
32-Caixa de leite-43.50-12-
33-Leite Moça-8.39-10-
34-Desodorante-11.90-19-
35-Whisky-63.90-7-
36-Café em pó-18.60-120-
37-Azeite de oliva-15.98-7-
38-Toddynho-2.30-60-
39-Nescau-3.00-45-
40-Cereal Nestle-14.26-22-
41-Leite em pó-21.10-19-
42-Whey protein-70.00-15-
43-Heineken Long Neck-5.49-33-
44-Mel de abelha-48.90-27-
45-Nutella-21.45-7-
46-Abacaxi-7.70-3-
47-Ovos de galinha-12.00-20-
48-Pão francês-1.40-100-
49-Peru fatiado-51.99-10-
50-Escova de cabelo-14.90-4-
51-Dolly Guaraná-24.69-100-
52-Ameixa seca-5.99-15-
53-Boneco inflável-1000-2-
54-Semente de alface-0.50-100-
55-Portal gun-1000000-1-
56-Bolacha de biscoito-3.50-10-
57-Picolé caicó-1.50-50-
58-Calcinha-17.99-1-
59-Mouse Razer-350.00-3-
60-Corote de pêssego-5-100-
61-Manteiga-10-10-
62-Seringa-2.49-3-
63-Tortuguita-0.99-500-
64-Biscoito Trakinas-2.50-12-
65-Violão-599.99-6-
66-GTA 5-89.90-4-
67-Piano de calda-36500-1-
68-Uno 2018 seminovo-35000-1-
69-Nokia 1999-99.99-2-
70-Saco de lixo-1.00-40-
71-Cimento-24.90-6-
72-Lula inflável-150-2-
73-Guarda chuva-30-10-
74-Protetor solar UV-350-1-
75-Sacolé-5-10-
76-Oléo de soja-10-5-
77-Margarina-8-15-
78-Toblerone-11.99-3-
79-Órgão harmônia-45000-1-
80-Roupa de banho-139.90-5-
81-Cacetinho-1.99-15-
82-Cabernet Sauvignon-69.90-15-
83-Cyberpunk 2077-199.99-4-
84-Abobrinha-3.20-25-
85-Benegrip-40.00-4-
86-Colar de diamantes-15000-1-
87-Cola bastão-3-8-
88-Lapisseira poli-16.00-5-
89-Camisinha-10.90-5-
90-Suco de morango-5.00-8-
91-Diazepam-12-1-
92-Revista Veja-9.90-25-
93-Mamadeira-5.99-25-
94-Codeína impura-15000-1-
95-Machado de guerra nórdico-150-3-
96-Cybertruck-356335-1-
97-Guia de matemática para ENEM-15-8-
98-Apontador-2.45-15-
99-Ar condicionado-1201-1-
100-Pá de jardinagem-9-69-
''')
  finally:
    f.close()


def search(text, file):
  try:
    f = open(file, 'r')
  except:
    print(color('red', 'ERRO! Não foi possível ler arquivo!'))
  else:
    l = str
    while not l == '###\n':
      l = f.readline()
    results = []
    for line in f:
      atts = line.split('-')
      if len(atts) >= 2:
        if text.strip().lower() in str(atts[1]).strip().lower():
          results.append(line)
    return results
  finally:
    f.close()


def print_products(products_list):
  print('='*30)
  if products_list == []:
    print('[x] Nenhum produto foi encontrado')
  else:
    for prod in products_list:
      atts = prod.split('-')
      print(f'[{atts[0]}] {atts[1].capitalize()} R${float(atts[2]):.2f} x{atts[3]}')
  print('='*30)


def change_quantity(id, quant, file):
  try:
    f = open(file, 'r')
  except:
    print(color('red', 'ERRO! Não foi possível ler arquivo!'))
  else:
    lines_list = f.readlines()
  finally:
    f.close()

  try:
    f = open(file, 'w')
  except:
    print(color('red', 'ERRO! Não foi possível editar arquivo!'))
  else:
    for line in lines_list:
      atts = line.split('-')
      if atts[0] == f'{id}':
        lines_list[lines_list.index(line)] = f'{atts[0]}-{atts[1]}-{atts[2]}-{int(atts[3])+quant}-\n'
        break
    f.writelines(lines_list)
  finally:
    f.close()


def add_product(id, quant, cart, file):
  try:
    f = open(file, 'r')
  except:
    print(color('red', 'ERRO! Não foi possível ler arquivo!'))
  else:
    is_found = False
    for line in f:
      atts = line.split('-')
      if atts[0] == f'{id}':
        is_found = True
        if int(atts[3]) > 0:
          if int(atts[3]) >= quant:
            newline = f'{atts[0]}-{atts[1]}-{atts[2]}-{quant}-'
            cart.append(newline)
            change_quantity(id, -1*quant, file)
            print(color('green', 'Produto adicionado!'))
          else:
            print(color('red', 'Quantidade excede estoque!'))
        else:
          print(color('red', 'Produto fora de estoque!'))
    if is_found == False:
      print(color('red', 'Produto não encontrado!'))
  finally:
    f.close()


def del_product(id, cart, file):
  is_deleted = False
  for prod in cart:
    atts = prod.split('-')
    if atts[0] == f'{id}':
      cart.remove(prod)
      change_quantity(id, int(atts[3]), file)
      is_deleted = True
  if is_deleted == False:
    print(color('red', 'Produto não encontrado!'))
  else:
    print(color('green', 'Produto removido!'))


def print_prices(discount, cart):
  total = 0
  for prod in cart:
    atts = prod.split('-')
    total += float(atts[2]) * int(atts[3])
  print('='*30)
  print(f'Total no crédito: R${total:.2f}')
  print(f'Total no boleto: R${total - total * (discount / 100):.2f} (-{discount}%)')
  print('='*30)

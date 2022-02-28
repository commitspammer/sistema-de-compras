import replit
from time import sleep


def int_input(text):
  while True:
    try:
      value = int(input(text))
    except ValueError:
      print(color('red' ,'Comando inválido. Digite novamente'))
      continue

    if value < 0:
      print(color('red', 'Comando inválido. Digite novamente'))
      continue
    else:
      break
  return value
 

def title(title):
  print('='*30)
  print(color('orange', f'{title}'.center(30).upper()))
  print('='*30)


def display(options):
  print('='*30)
  for opt in options:
    print(color('yellow', f'[{options.index(opt)+1}] {opt}'))
  print('='*30)


def color(color, text):
  if color == 'red':
    return f'\033[31m{text}\033[0m'
  elif color == 'yellow':
    return f'\033[93m{text}\033[0m'
  elif color == 'green':
    return f'\033[32m{text}\033[0m'
  elif color == 'blue':
    return f'\033[34m{text}\033[0m'
  elif color == 'orange':
    return f'\033[33m{text}\033[0m'
  else:
    return f'\033[30m{text}\033[0m'


def clear():
  sleep(1)
  replit.clear()

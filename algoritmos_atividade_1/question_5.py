import sys
from utils.convert_to_currency import convert_to_currency

km = input('Insira a quantidade de km percorridos: ')

days = input('Insira a quantidade de dias pelos quais o carro foi alugado: ')

try:
  km = float(km)
except:
  sys.exit("Inválido!")  

try:
  days = int(days)
except:
  sys.exit("Inválido!")   
  
rentValue = (days * 60) + (km * 0.15)

print("Valor do aluguel: " + convert_to_currency(rentValue))
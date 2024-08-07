import sys
import requests
import json
from utils.convert_to_currency import convert_to_currency

def get_dollar_today():
    try:
        result = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL').json()
        return float(result['USDBRL']['bid'])
    except:
        sys.exit("Falha ao buscar a cotação atual do dólar!")   
        return None

value = input('Insira o valor em Dólar que deseja converter para Real: ')

try:
  value = float(value)
except:
  sys.exit("Inválido!")   

fee = input('Insira a taxa de conversão ou PRESSIONE ENTER para INSERIR AUTOMATICAMENTE a cotação atual do dólar:')

if not fee:
    fee = get_dollar_today()
else:
  try:
    fee = float(fee)
  except:
    sys.exit("Inválido!")  

result = value * fee

print("O resultado da conversão é: " + convert_to_currency(result))
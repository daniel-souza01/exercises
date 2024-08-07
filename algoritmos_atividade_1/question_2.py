import sys
from utils.convert_to_currency import convert_to_currency

productPrice = input('Insira o preço de um produto: ')

try:
  productPrice = float(productPrice)
except:
  sys.exit("Inválido!")   

discount = input('Insira porcentagem de desconto a ser aplicada: ')

try:
    discount = float(discount)
except:
    sys.exit("Inválido!")  
    
percentDiscount = productPrice * (discount / 100)

result = productPrice - percentDiscount

print("Valor final do produto: " + convert_to_currency(result))
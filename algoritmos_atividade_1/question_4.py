import sys
from datetime import datetime

date = input('Insira seu ano de nascimento: ')

try:
  date = int(date)
except:
  sys.exit("Inválido!")   

actualYear = datetime.today().year - 1

age = actualYear - date

print("Sua idade é: " + str(age))
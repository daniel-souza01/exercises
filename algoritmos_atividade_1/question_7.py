import sys

celsius = input('Insira a temperatura em graus Celsius: ')

try:
  celsius = float(celsius)
except:
  sys.exit("Inválido!")   
  
fahrenheit = (celsius * 9/5) + 32

print("Esse valor representa em Fahrenheit: " + str(fahrenheit))
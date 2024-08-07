import sys

cigarettesPerDay = 0
smokedYears = 0

try:
    cigarettesPerDay = int(input("Insira Pergunte a quantidade de cigarros fumados por dia: "))
except:
  sys.exit("Inválido!") 
  
try:
    smokedYears = int(input("Insira quantos anos você já fumou: "))
except:
  sys.exit("Inválido!") 

totalCigarettesSmoked = smokedYears * 365 * cigarettesPerDay 

totalMinutesLost = totalCigarettesSmoked * 10

totalDaysLost = totalMinutesLost / (24 * 60)

print(f"Sua vida foi reduzida em {int(totalDaysLost)} dias ")
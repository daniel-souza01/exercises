import sys

note_1 = 0
note_2 = 0
note_3 = 0

try:
    note_1 = float(input("Insira sua primeira nota: "))
except:
  sys.exit("Inválido!") 
  
try:
    note_2 = float(input("Insira sua segunda nota: "))
except:
  sys.exit("Inválido!") 
  
try:
    note_3 = float(input("Insira sua terceira nota: "))
except:
  sys.exit("Inválido!") 
  
avarage = (note_1 + note_2 + note_3) / 3

print(f"Sua média é {avarage}")
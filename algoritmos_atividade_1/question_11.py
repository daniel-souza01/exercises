import sys

nums = input("Insira um número com 3 dígitos: ")

if not nums.isdigit() or not len(nums) == 3:
  sys.exit("Inválido!")   

result = 0

for digit in nums:
    result += int(digit)

print("A soma dos dígitos corresponde a: " + str(result))
import math
print('Задача 5. Число Эйлера')

result = 0
count = 0
num = 1

while num > 1e-5 :
  num = 1 / math.factorial(count)
  result+=num
  count+=1

print(result)

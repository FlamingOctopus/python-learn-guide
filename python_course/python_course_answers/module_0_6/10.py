left = 1
right = 100
while True:
  current = (left+right)//2
  is_right = int(input(f'Ваше число:{current}?(да, больше, меньше)'))
  if is_right == 1:
    print('Число угадано')
    break
  elif is_right == 2 :
    left = current + 1
  else:
    right = current - 1

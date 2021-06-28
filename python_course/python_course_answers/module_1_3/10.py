print('Задача 10. Аннуитетный платёж')

def credit(s,n,i,month = 0):
  if month != 0:
    count = month
    s = main_func(s,n,i,count)
  else:
    count = 99999
    s = main_func(s,n,i,count)
  return s

def main_func(s,n,i, count):
  i = i/100
  K = (i*(1 + i) ** n) / ((1 + i) ** n - 1)
  A = round(K*s,2)
  for j in range(1,count+1):
    if s > 1:
      print("Период:", j)
      print("Остаток долга на начало периода:", s)
      sum_proc = s * i
      sum_kr = A - sum_proc
      print("Выплачено процентов: ",  sum_proc)
      print("Выплачено тела кредита:", sum_kr)
      s -= sum_kr
    else:
      break
  print("Остаток долга:", s)
  return s

s = float(input("Сумма кредита"))
n = float(input("На сколько лет выдан?"))
i = float(input("Сколько процентов годовых?"))

s = credit(s,n,i,3)
print("=================================================")
new_n = float(input("На сколько лет продляется договор?"))
new_i = float(input("Увеличение ставки до:"))
n+=new_n-3

credit(s,n,new_i)

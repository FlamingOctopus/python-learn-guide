print('Задача 10. Метод бутерброда')

x = input("Введите защифрованное слово ")
count=1
str_fir = ''
str_sec = ''
for i in x:
  if count%2 != 0:
    str_fir=str_fir+i
  else:
    str_sec=i+str_sec
  count+=1

print(str_fir+str_sec)
#
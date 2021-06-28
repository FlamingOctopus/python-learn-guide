

def cheking(check_num):
    if len(ip_adress) != 4:
        return "Адрес - это четыре числа, разделенные точками"
    else:
        for number in ip_adress:
            if not number.isdigit():
                return f"{number}- не целое число"
            if int(number) > 255:
                return f"{number} превышает 255"
    return "IP-адрес корректен"


ip_adress = input("Введите IP:").split('.')
print(cheking(ip_adress))

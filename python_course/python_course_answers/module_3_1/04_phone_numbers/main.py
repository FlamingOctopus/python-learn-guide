import re

phone_numbers_list = ['9999999999', '999999-999', '99999x9999', '8999999999']

for tel in enumerate(phone_numbers_list):
    if re.findall(r'\b[89]\d{9}', tel[1]):
        print(f'{tel[0] + 1} номер: {tel[1]} подходит')
    else:
        print(f'{tel[0] + 1} номер: {tel[1]} не подходит')

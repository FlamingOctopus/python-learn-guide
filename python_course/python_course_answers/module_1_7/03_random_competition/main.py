from random import uniform

first_list = [round(uniform(5, 10), 2) for number in range(20)]
second_list = [round(uniform(5, 10), 2) for number in range(20)]

wins_list = [first_list[count] if first_list[count] >= second_list[count] else second_list[count] for count in
             range(0, len(first_list))]
print(f"Первая команда: {first_list}\nВторая команда: {second_list}\nПобедители тура: {wins_list}")
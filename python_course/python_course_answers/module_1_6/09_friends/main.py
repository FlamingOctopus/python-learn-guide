def debt(friend_count, debts_count):
    debts_list = [[person, 0] for person in range(1, friend_count + 1)]
    for debts_papper in range(1, debts_count + 1):
        print(f"{debts_papper} расписка")
        cash_in, cash_out, cash = int(input("Кому: ")), int(input("От кого: ")), int(input("Сколько: "))
        for debt_person in debts_list:
            if debt_person[0] == cash_in:
                debt_person[1] += cash
        for debt_person in debts_list:
            if debt_person[0] == cash_out:
                debt_person[1] -= cash
    print("Баланс друзей:")
    for debt in debts_list:
        print(debt[0], ":", debt[1])


x, y = int(input("Кол-во друзей:")), int(input("Долговых расписок: "))
debt(x, y)

def game():
    score_table = {}
    roundes_count = int(input("Сколько записей вносится в протокол? "))
    for note in range(1, roundes_count + 1):
        values = input(f"{note} запись: ").split()
        score, name = int(values[0]), values[1]
        score = int(score)
        if name in score_table:
            if score > score_table[name][0]:
                score_table[name][0] = score
                score_table[name][1] = note
        else:
            score_table[name] = [score, note]
    print(list(score_table.items()))
    return list(score_table.items())


def sort_func(item):
    return item[1][0] - item[1][1]


def sort_winners(scores):
    scores.sort(key=sort_func, reverse=True)
    # sorted(scores, key=sort_func, reverse = True)
    for winner in range(0, 3):
        print(f"{winner + 1} место. {scores[winner][0]} ({scores[winner][1][0]})")


sort_winners(game())

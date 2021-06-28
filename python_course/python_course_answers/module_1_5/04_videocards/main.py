def max_delete(videocards_list):
    max_videocard = 0
    new_videocards_list = []
    for card in videocards_list:
        if card > max_videocard:
            max_videocard = card
    for card in videocards_list:
        if card == max_videocard:
            continue
        else:
            new_videocards_list.append(card)
    return new_videocards_list


list = [3070, 2060, 3090, 3070, 3090]
print("Новый список видеокарт: ", max_delete(list))

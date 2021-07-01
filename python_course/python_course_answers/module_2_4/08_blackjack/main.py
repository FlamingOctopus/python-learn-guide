import random
from collections import deque

class Card:
    """генерация карт"""
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __add__(self, card):
        return self.value + card.value

class Deck:
    """генерация колоды"""
    def __init__(self, suit):
        self.suit = suit
        self.cards_comm = 10
        self.cards_list = []

    def card_pict_gen(self):
        for i in range(1, self.suit + 1):
            self.cards_list.append(Card("Король", 10))
            self.cards_list.append(Card("Дама", 10))
            self.cards_list.append(Card("Валет", 10))

    def cards_comm_gen(self):
        for i in range(1, self.cards_comm + 1):
            for j in range(1, self.suit + 1):
                if i == 1:
                    self.cards_list.append((Card("Туз", 11)))
                else:
                    self.cards_list.append((Card(str(i), i)))

    def deck_generator(self):
        self.cards_list = []
        self.card_pict_gen()
        self.cards_comm_gen()
        random.shuffle(self.cards_list)

class Game:
    """Класс игры"""
    def __init__(self, deck):
        self.deck = deck
        self.deck.deck_generator()
        self.deque_cards = deque(self.deck.cards_list)
        self.user_cards_list = [self.deque_cards.pop() for x in range(2)]
        self.computer_cards_list = [self.deque_cards.pop() for x in range(2)]

    def game(self):
        print(
        f"Ваши карты - {' '.join(i.name for i in self.user_cards_list)} их сумма {sum(i.value for i in self.user_cards_list)}")
        responce = input("Взять карту(1) или закончить(2)? ")
        if responce == "1":
            self.user_cards_list.append(self.deque_cards.pop())
        user_sum = sum(i.value for i in self.user_cards_list)
        comp_sum = sum(i.value for i in self.computer_cards_list)
        if 21 >= user_sum > comp_sum:
            print("Вы победили!")
        elif user_sum < comp_sum <= 21:
            print("Вы проиграли!")
        elif user_sum > 21:
            print("Ваши карты сгорели")
        else:
            user_sum = sum(i.value for i in self.user_cards_list)
            comp_sum = sum(i.value for i in self.computer_cards_list)
            if 21 >= user_sum > comp_sum:
                print("Вы победили!")
            elif user_sum < comp_sum <= 21:
                print("Вы проиграли!")

deck = Deck(4)
game = Game(deck)
game.game()
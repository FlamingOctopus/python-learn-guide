class Playground:
    """"Рисуем игровое поле"""
    def __init__(self):
        self.size = 3
        self.board = list(range(1, self.size ** 2 + 1))

    def draw_playground(self):

        for i in range(3):
            print(self.board[0 + i * self.size], "|", self.board[1 + i * self.size], "|",
            self.board[2 + i * self.size], )
            if i == 2:
                continue
            print("-" * self.size ** 2)

class Game:
    def __init__(self, playground):
        self.playground = playground

    def input_func(self, symbol):
        """Обработка ввода"""
        while True:
            response = input(f"\nХод {symbol}(1,9): ")
            try:
                response = int(response)
            except:
                print("Некорректный ввод.")
                continue
            if 1 <= response <= 9:
                if str(self.playground.board[response - 1]) not in "XO":
                    self.playground.board[response - 1] = symbol
                    break
                else:
                    print("Эта клетка занята")
            else:
                print("Некорректный ввод.")

    def game(self):
        """Метод игры"""
        counter = 0
        while True:
            self.playground.draw_playground()
            if counter % 2 == 0:
                self.input_func("X")
            else:
                self.input_func("O")
            counter += 1
            if counter > 4:
                tmp = self.check_win()
                if tmp:
                    print(tmp, "выиграл!")
                    break
            if counter == 9:
                print("Ничья!")
                break
        self.playground.draw_playground()

    def check_win(self):
        """Проверка поля на победную позицию"""
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.playground.board[each[0]] == self.playground.board[each[1]] == self.playground.board[each[2]]:
                return self.playground.board[each[0]]
        return False

playground = Playground()
game = Game(playground)
game.game()
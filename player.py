class PlayerCPU():
    def __init__(self, name, card):
        self.name = name
        self.card = card
        self.win = None

    def step(self, num, answer=None):
        self.card.del_num(num)
        if self.card.check_end():
            self.win = True


class PlayerHuman(PlayerCPU):
    def step(self, num, answer=None):
        # Если ответ y
        if answer == 'y':
            # И если число есть в карточке, то зачеркиваем
            if num in self.card:
                self.card.del_num(num)
                # Если последнее число, то выиграл
                if self.card.check_end():
                    self.win = True
            # В противном случае(ответ y, а числа нет)
            else:
                self.win = False
        # В противном случае(ответ нет)
        else:
            # Если число есть, то проиграл
            if num in self.card:
                self.win = False
            # Если нет то продолжаем

class AbstractPlayer:
    def __init__(self, position):
        self.position = position
        self.cards = []
        self.isPlay = True
        self.card_sum = 0

    def get_cards(self):
        cards = "["
        for n, c in enumerate(self.cards):
            cards += str(c)
            if n != len(self.cards) - 1:
                cards += ", "
        return cards + "]"

    def get_card_sum(self):
        s = 0
        for c in self.cards:
            s += c.value
        return s


class Dealer(AbstractPlayer):
    def __init__(self, position):
        super().__init__(position)

    def __str__(self):
        return f"Дилер имеет на руках: {self.get_cards()}"


class Player(AbstractPlayer):
    def __init__(self, position):
        super().__init__(position)
        self.chips = 10000
        self.bet = 0

    def __str__(self):
        return f"Игрок на позиции: {self.position} имеет на руках: {self.get_cards()}"

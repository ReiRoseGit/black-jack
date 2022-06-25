from Deck import Deck
from Player import Player, Dealer


# todo: контроль ввода значений, создание ботов, перевод игрока в режим бота

class Game:
    def __init__(self):
        self.players = []
        self.dealer = None
        self.deck = Deck()

    def create_game(self):
        count_of_players = int(input("Введите кол-во игроков:"))
        for p in range(count_of_players):
            pl = Player(position=p)
            #pl.cards = self.deck.start_hand()
            self.players.append(pl)
        self.dealer = Dealer(position=count_of_players)
        #self.dealer.cards = [self.deck.take_card()]
        # self.dealer.cards.append(self.deck.take_card())
        print("Your game has been created!")

    def players_turn(self):
        for p in self.players:
            p.bet = 0
            while True:
                bet = int(
                    input(f"Игрок на позиции {p.position}, у вас: {p.chips} фишек, сделайте вашу ставку: "))
                if 0 < bet <= p.chips:
                    p.bet = bet
                    break
                else:
                    print("Некорректный ввод, повторите попытку")
            p.chips -= p.bet
            print(
                f"Ход игрока на позиции: {p.position}, его карты: {p.get_cards()}, сумма которых: {p.get_card_sum()}")
            while True:
                sum = p.get_card_sum()
                if sum == 21:
                    print(
                        f"Игрок на позиции: {p.position} собрал blackjack!")
                    p.card_sum = 21
                    break
                elif sum > 21:
                    print(
                        f"Игрок на позиции: {p.position} проигрывает, набрав {sum} очков")
                    p.isPlay = False
                    p.card_sum = sum
                    break
                choice = input(
                    "Введите more, если вы хотите взять еще одну карту, в противном случае, введите stop: ")
                if choice == "more":
                    card = self.deck.take_card()
                    p.cards.append(card)
                    print(
                        f"Вы взяли {card}, ваши карты: {p.get_cards()}, сумма которых: {p.get_card_sum()}")
                else:
                    sum = p.get_card_sum()
                    print(
                        f"Игрок на позиции {p.position} больше не берет карты")
                    print(
                        f"Его карты {p.get_cards()}, сумма которых: {sum}")
                    p.card_sum = sum
                    break
        for p in self.players:
            print(
                f"Игрок на позиции: {p.position} имеет карты: {p.get_cards()}, сумма которых: {p.get_card_sum()}")
        print("Ход Диллера")

    def get_max_value(self):
        max_value = 0
        for p in self.players:
            if p.isPlay and p.card_sum > max_value:
                max_value = p.card_sum
        return max_value

    def dealer_turn(self):
        value_to_beat = self.get_max_value()
        while True:
            s = self.dealer.get_card_sum()
            print(
                f"Карты диллера: {self.dealer.get_cards()}, сумма которых {s}")
            if s > 21:
                print(f"Диллер проигрывает, набрав: {s} очков!")
                self.dealer.isPlay = False
                self.dealer.card_sum = s
                break
            else:
                if 17 <= s or value_to_beat < s:
                    print(
                        f"Диллер останавливает набор карт, набрав: {s} очков, его карты: {self.dealer.get_cards()}, их сумма: {s}")
                    self.dealer.card_sum = s
                    break
                else:
                    c = self.deck.take_card()
                    print(f"Диллер берет карту {c}")
                    self.dealer.cards.append(c)

    def one_turn(self):
        self.players_turn()
        self.dealer_turn()
        print("Итоги кона:")
        print(
            f"Диллер имеет на руках: {self.dealer.get_cards()}, сумма которых {self.dealer.card_sum}")
        for p in self.players:
            print(
                f"Игрок на позиции: {p.position} имеет карты: {p.get_cards()}, сумма которых: {p.card_sum}")
            if not p.isPlay:
                print(
                    f"Игрок на позиции: {p.position} проигрывает диллеру {p.bet} фишек!")
                print(
                    f"Текущий баланс игрока на позиции: {p.position} составляет: {p.chips}")
            else:
                if self.dealer.isPlay:
                    if p.card_sum > self.dealer.card_sum:
                        p.chips += p.bet * 2
                        print(
                            f"Игрок на позиции: {p.position} обыгрывает диллера!")
                        print(
                            f"Текущий баланс игрока на позиции: {p.position} составляет: {p.chips}")
                    elif p.card_sum == self.dealer.card_sum:
                        p.chips += p.bet
                        print(
                            f"Игрок на позиции: {p.position} играет с диллером в ничью!")
                        print(
                            f"Текущий баланс игрока на позиции: {p.position} составляет: {p.chips}")
                    else:
                        print(
                            f"Игрок на позиции: {p.position} проигрывает диллеру!")
                        print(
                            f"Текущий баланс игрока на позиции: {p.position} составляет: {p.chips}")
                else:
                    print(
                        f"Игрок на позиции: {p.position} обыгрывает диллера!")
                    p.chips += p.bet * 2
                    print(
                        f"Текущий баланс игрока на позиции: {p.position} составляет: {p.chips}")

    def ask_for_continue(self):
        dont_want_to_play = []
        for p in self.players:
            if p.chips <= 0:
                dont_want_to_play.append(p)
                continue
            choice = input(
                f"Желает ли продолжить игру игрок на позиции {p.position}? 'yes / no': ")
            if choice == 'no':
                dont_want_to_play.append(p)
        return dont_want_to_play

    def make_start_terms(self):
        self.deck = Deck()
        for p in self.players:
            p.bet = 0
            p.isPlay = True
            p.cards = self.deck.start_hand()
            p.card_sum = 0
        self.dealer.isPlay = True
        self.dealer.cards = [self.deck.take_card()]

    def game(self):
        self.create_game()
        players_left = []
        while True:
            self.make_start_terms()
            dont_want_to_play = self.ask_for_continue()
            for p in dont_want_to_play:
                self.players.remove(p)
                players_left.append(p)
            if len(self.players) == 0:
                print("Игра окончена, все игроки ушли!")
                break
            self.one_turn()
        print("Состояние фишек:")
        for p in players_left:
            print(f"Игрок на позиции: {p.position} имеет: {p.chips}")

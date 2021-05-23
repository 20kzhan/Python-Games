import random
import os, sys

# for windows OS
if os.name == "nt":
    os.system("cls")

    import ctypes


    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]


    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = False
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))


class Card:
    CARD_RANKS = ["A░", "2░", "3░", "4░", "5░", "6░", "7░", "8░", "9░", "10", "J░", "Q░", "K░", "░░"]
    CARD_SUITS = ['♠', '♥', '♣', '♦', '░']

    CARD_IMAGE = [
        '┌─────────┐\t',
        '│░░░░░░░░░│\t',
        ['│░', '░░░░░░│\t'],
        '│░░░░░░░░░│\t',
        ['│░░░░', '░░░░│\t'],
        '│░░░░░░░░░│\t',
        '│░░░░░░░░░│\t',
        '└─────────┘\t'
    ]

    CARD_IMAGE_TOP = '┌─────────┐\t'
    CARD_IMAGE_MIDDLE = '│░░░░░░░░░│\t'
    CARD_IMAGE_LEFT = '│░'
    CARD_IMAGE_RIGHT = '░░░░░░│\t'
    CARD_IMAGE_SUIT_LEFT = '│░░░░'
    CARD_IMAGE_SUIT_RIGHT = '░░░░│\t'
    CARD_IMAGE_BOTTOM = '└─────────┘\t'

    def __init__(self, value=-1):
        if value > 51 or value < 0:
            value = random.randint(0, 51)
        self._value = value

    def get_rank_value(self):
        return self._value % 13

    def get_rank_image(self):
        return self.CARD_RANKS[self._value % 13]

    def get_suit_image(self):
        return self.CARD_SUITS[self._value // 13]

    def __str__(self, covered=False):
        '''
        Returns the card's image in string, line by line with "\n" to end each
        line.  This is similar to Python's __str__() method.
        '''
        some_str = ''
        for index, line in enumerate(self.CARD_IMAGE):
            if index == 2:
                some_str += line[0] + \
                            (self.get_rank_image() if not covered else self.CARD_RANKS[-1]) + \
                            line[1]
            elif index == 4:
                some_str += line[0] + \
                            (self.get_suit_image() if not covered else self.CARD_SUITS[-1]) + \
                            line[1]
            else:
                some_str += line
            some_str += '\n'

        return some_str

    def get_card_image(self, covered=False):
        # will return a list of strings
        image = []
        for index, line in enumerate(self.CARD_IMAGE):
            if index == 2:
                image.append(line[0] + \
                             (self.get_rank_image() if not covered else self.CARD_RANKS[-1]) + \
                             line[1])
            elif index == 4:
                image.append(line[0] + \
                             (self.get_suit_image() if not covered else self.CARD_SUITS[-1]) + \
                             line[1])
            else:
                image.append(line)

        return image


class BJHand:
    # This class implements a hand of BJ cards with following functionality
    #   1. printing the cards out
    #   2. Computes the hand's total value, whether the hand is a bust, etc
    CARD_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def __init__(self, name):
        self._player_name = name
        self._hand = []

    def print(self, col_size=2, cover_first_card=False):
        # prints the entire hand vertically, how many cards across?
        card_img_list = []
        print(f"{self._player_name}'s hand:")
        for i in range(len(self._hand)):
            if i == 0:
                card_img_list.append(self._hand[i].get_card_image(cover_first_card))
            else:
                card_img_list.append(self._hand[i].get_card_image())
        # for x in range(8):
        #     test = [i[x] for i in card_img_list]
        #     for y in range(len(test)):
        #         print(test[y], end='')
        #     print()
        for multiple in range(len(card_img_list) // col_size + 1):
            for image_line_index in range(len(card_img_list[0])):
                for i in range(col_size):
                    card_img_id = multiple * col_size + i
                    if card_img_id < len(card_img_list):
                        print(card_img_list[card_img_id][image_line_index], end='')
                print()
        print()

    def get_score(self):
        # returns the value of the entire hand
        value = 0
        has_ace = False
        for c in self._hand:
            value += self.CARD_VALUES[c.get_rank_value()]
            if c.get_rank_value() == 0:
                has_ace = True

        if has_ace and value + 10 <= 21:
            return value + 10
        return value

    def is_bust(self):
        # returns True/False whether the hand is a bust
        return self.get_score() > 21

    def get_num_cards(self):
        return len(self._hand)

    def add_card(self, card=Card()):
        self._hand.append(card)


class CardDeck:
    def __init__(self):
        # This function initializes the deck
        # You should create a list of 52 cards in sequence from 0 to 51
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))
        self.shuffle()

    def shuffle(self):
        # This function shuffles the deck of cards
        # Hint: just shuffle the list of Cards (object)
        random.shuffle(self._card_list)

    def deal_card(self):
        # This function deals a card from the deck
        # Just pot a card from the list and return it
        # Did you accidentally misspell pop?..
        return self._card_list.pop()

    def num_cards_remaining(self):
        # This function returns the # of cards left in the deck
        return len(self._card_list)

    def print(self):
        for c in self._card_list:
            print(str(c))


class BJGame:
    def __init__(self):
        pass

    def player(self):
        state = 0

        while True:
            if state == 0:
                deck = CardDeck()
                deck.shuffle()
                state = 1

            if state == 1:
                deck.shuffle()
                player = BJHand("Player")
                dealer = BJHand("Dealer")
                for i in range(2):
                    dealer.add_card(deck.deal_card())
                    player.add_card(deck.deal_card())
                player.print(cover_first_card=False)
                dealer.print(cover_first_card=True)
                state = 2

            if state == 2:
                if player.get_score() == 21:
                    state = 4
                if input("Hit or stay? (Enter h or s) ") == 'h':
                    player.add_card(deck.deal_card())
                    player.print(cover_first_card=False)
                    dealer.print(cover_first_card=False)
                    if player.get_score() == 21:
                        state = 4

                    elif player.is_bust():
                        state = 4
                else:
                    state = 3

            if state == 3:
                print('b')
                if dealer.get_score() <= 16:
                    dealer.add_card(deck.deal_card())
                    if dealer.is_bust():
                        state = 4
                else:
                    state = 4

            if state == 4:
                player.print(cover_first_card=False)
                dealer.print(cover_first_card=False)
                if player.get_score() == dealer.get_score():
                    print("It's a tie!\n")
                elif player.get_score() < dealer.get_score():
                    print('Dealer won!\n')
                elif player.get_score() < dealer.get_score():
                    print('Player won!\n')
                elif player.get_score() == 21:
                    print('**************Blackjack!**************')
                    print('Player won!\n')
                elif dealer.get_score() == 21:
                    print('**************Blackjack!**************')
                    print('Dealer won!\n')
                elif player.is_bust():
                    print('**************Player bust!**************')
                    print('Dealer won!')
                elif dealer.is_bust():
                    print('**************Dealer bust!**************')
                    print('Player won!')
                self.reset_game()
                state = 1

    # def play(self):
    #     player_stand = False
    #
    #     if input("Hit or stay? (Enter h or s) ") == 'h' and not player_stand:
    #         self._player.add_card()
    #     else:
    #         player_stand = True
    #     if self._player.is_bust():
    #         print('**************Player bust!**************')
    #         print('Dealer won!')
    #         self.reset_game()
    #     elif self._player.get_score() == 21:
    #         print('**************Blackjack!**************')
    #         print('Player won!\n')
    #         self.reset_game()
    #
    #     if self._dealer.get_score() < 16:
    #         self._dealer.add_card()
    #     elif random.randint(1, 4) == 4:
    #         self._dealer.add_card()
    #
    #     if player_stand:
    #         print("Dealer's turn to play:")
    #     self._player.print(cover_first_card=False)
    #     self._dealer.print(cover_first_card=False)
    #
    #
    #
    #     if self._dealer.is_bust():
    #         print('**************Dealer bust!**************')
    #         print('Player won!')
    #         self.reset_game()
    #     elif self._dealer.get_score() == 21:
    #         print('**************Blackjack!**************')
    #         print('Dealer won!\n')
    #         self.reset_game()

    def reset_game(self):
        if input('Do you want to play another game? (y/n) ') == 'y':
            pass
        else:
            os.system(exit())


if __name__ == '__main__':
    game = BJGame()
    while True:
        game.player()
    # card_deck1 = CardDeck()
    #
    # player = BJHand()
    # dealer = BJHand()
    #
    # player.add_card((card_deck1.deal_card()))
    # player.add_card((card_deck1.deal_card()))
    # player.add_card((card_deck1.deal_card()))
    #
    # player.print()

    # while True:
    #     card1 = Card(value=-1)
    #
    #     # print(card1)
    #     # input('Press Enter to regenerate card')
    #     card_deck1.print()
    #     input()
    #     card_deck1.shuffle()

'''
#########################################
# simple test on Card and Card_Deck classes 
#########################################

# create a new deck of cards
deck = Card_Deck()

card1 = deck.deal_card()
card2 = deck.deal_card()
card3 = deck.deal_card()

card1.print_card(cover_first_card=True)
card1.print_card()
card2.print_card()
card3.print_card()

deck = Card_Deck()

# deal 52 cards and print out each card (should be in order)
for i in range(52):
    print("i:", i)
    card = deck.deal_card()
    card.print_card()
    if not i:
        card.print_card(cover_first_card=True)

# now shuffle the deck of cards
deck.shuffle()

# deal 52 cards and print out each card (should be shuffled, random)
for i in range(52):
    print("i:", i)
    card = deck.deal_card()
    card.print_card()
    if not i:
        card.print_card(cover_first_card=True)

# test the get_card_image() function
deck.shuffle()
card = deck.deal_card()
card_text = card.get_card_image()
print("Card Text:")
print(card_text)
'''

import random

class Card:
    CARD_RANKS = ["A░", "2░", "3░", "4░", "5░", "6░", "7░", "8░", "9░", "10", "J░", "Q░", "K░", "░░"]
    CARD_SUITS = ['♠', '♥', '♣', '♦', '░']

    CARD_IMAGE_TOP = '┌─────────┐\t'
    CARD_IMAGE_MIDDLE = '│░░░░░░░░░│\t'
    CARD_IMAGE_LEFT = '│░'
    CARD_IMAGE_RIGHT = '░░░░░░│\t'
    CARD_IMAGE_SUIT_LEFT = '│░░░░'
    CARD_IMAGE_SUIT_RIGHT = '░░░░│\t'
    CARD_IMAGE_BOTTOM = '└─────────┘\t'
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

    def __init__(self, value=-1):
        if value > 51 or value < 0:
            value = random.randint(0, 51)
        self._value = value

    @property
    def rank_value(self):
        return self._value % 13

    @property
    def rank_image(self):
        return self.CARD_RANKS[self._value % 13]

    @property
    def suit(self):
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
                            (self.rank_image if not covered else self.CARD_RANKS[-1]) + \
                            line[1]
            elif index == 4:
                some_str += line[0] + \
                            (self.suit_image if not covered else self.CARD_SUITS[-1]) + \
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
                             (self.rank_image if not covered else self.CARD_RANKS[-1]) + \
                             line[1])
            elif index == 4:
                image.append(line[0] + \
                             (self.suit_image if not covered else self.CARD_SUITS[-1]) + \
                             line[1])
            else:
                image.append(line)

        return image


class CardHand:
    # This class implements a hand of poker cards with following functionality
    #   1. printing the cards out

    #CARD_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def __init__(self, name="", cards=[]):
        self._player_name = name
        self._hand = []
        self.add_cards(cards)

    @property
    def name(self):
        return self._player_name

    def print(self, msg, col_size=2, num_cards_to_cover=0):
        # if cover_all_cards is True, then cover all cards
        # if cover_all_cards is False and cover_first_card is True, then only cover first card
        # else print cards face up

        # prints the entire hand vertically, how many cards across?
        ct = []
        print(msg)
        print(f"Player: {self.name}")
        for i, c in enumerate(self._hand):
            if num_cards_to_cover == 0:
                ct.append(c.get_card_image())
            elif num_cards_to_cover == -1:
                ct.append(c.get_card_image(True))
            else:
                ct.append(c.get_card_image(i < num_cards_to_cover))

        print(ct)

        for r in range((len(self._hand) - 1) // col_size + 1):
            print_this = ct[r * col_size : (r + 1) * col_size]
            for line_num in range(len(ct[0])):
                for card_text in print_this:
                    print(card_text[line_num], end='')
                print()
            print()

    def num_cards(self):
        return len(self._hand)



    def add_card(self, card):
        # adding a single card
        self._hand.append(card)

    def add_cards(self, cards):
        # adding a list of cards
        self._hand += cards

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

if __name__ == "__main__":
    card = Card(0)

    print(card)

    card_str = card.get_card_image()
    print(card_str)

    card_str = card.get_card_image(True)
    print(card_str)

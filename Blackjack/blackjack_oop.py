import random

class Card:
    CARD_RANKS = ["A░", "2░","3░","4░","5░","6░","7░","8░","9░","10","J░","Q░","K░"]
    CARD_SUITS = ['♠', '♥', '♣', '♦', '░']
    


    def __init__(self, value):
        if value > 51 or value < 0:
            value = random.randint(0, 51)
        self._value = value
        self._rank_value = random.randint(0, 12)
        self.CARD_IMAGE_TOP =        '┌─────────┐\t'
        self.CARD_IMAGE_MIDDLE =     '│░░░░░░░░░│\t'
        self.CARD_IMAGE_LEFT =       '│░'
        self.CARD_IMAGE_RIGHT =          '░░░░░░│\t'
        self.CARD_IMAGE_SUIT_LEFT =  '│░░░░'
        self.CARD_IMAGE_SUIT_RIGHT =       '░░░░│\t'
        self.CARD_IMAGE_BOTTOM =     '└─────────┘\t'

    def get_suit_image(self):
        if self._value > 0 and self._value <= 12:
            return '♠'
        elif self._value >= 13 or self._value <= 25:
            return '♥'
        elif self._value >= 26 or self._value <= 38:
            return '♣'
        elif self._value >= 39 or self._value <= 51:
            return '♦'

    def get_value(self):
        return str(self._value)

    def get_rank_image(self):
        return self.CARD_RANKS[self._rank_value]

    def print(self, covered=False):
        print(self.CARD_IMAGE_TOP)
        print(self.CARD_IMAGE_MIDDLE)
        print(self.CARD_IMAGE_LEFT + self.get_rank_image() + self.CARD_IMAGE_RIGHT)
        print(self.CARD_IMAGE_MIDDLE)
        print(self.CARD_IMAGE_SUIT_LEFT + self.get_suit_image() + self.CARD_IMAGE_SUIT_RIGHT)
        for i in range(2):
            print(self.CARD_IMAGE_MIDDLE)
        print(self.CARD_IMAGE_BOTTOM)
        pass

    def get_card_image(self, covered=False):
        '''
        Returns the card's image in string, line by line with "\n" to end eeach
        line.  This is similar to Python's __str__() method.
        '''
        pass

class BJ_Hand:
    # This class implements a hand of BJ cards with following functionality
    #   1. printing the cards out
    #   2. Computes the hand's total value, whether the hand is a bust, etc
    CARD_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def __init__(self, cards=None):
        pass

    def print(self, msg="", col_size=5, cover_first_card=False):
      # prints the entire hand horizontally, how many cards across?
        pass

    def score(self):
      # returns the value of the entire hand
        pass

    def is_bust(self):
        # returns True/False whether the hand is a bust
        pass

    def get_num_cards(self):
        pass

    def add_card(self, card):
        pass



class Card_Deck:
    def __init__(self):
        # This function initializes the deck
        # You should create a list of 52 cards in sequence from 0 to 51
        pass

    def shuffle(self):
        # This function shuffles the deck of cards
        # Hint: just shuffle the list of Cards (object)
        pass

    def deal_card(self):
        # This function deals a card from the deck
        # Just pot a card from the list and return it
        pass

    def get_cards_remaining(self):
        # This function returns the # of cards left in the deck
        pass

class BJ_Game:
    def __init__(self):
        pass

    def play(self):
        pass

while True:
    card1 = Card(value=-1)
    card1.print()
    input('Press Enter to regenerate card')

    '''
    #########################################
    # simple test on Card and Card_Deck classes 
    #########################################

    # create a new deck of cards
    deck = Card_Deck()

    card1 = deck.deal_card()
    card2 = deck.deal_card()
    card3 = deck.deal_card()

    card1.print_card(show_back=True)
    card1.print_card()
    card2.print_card()
    card3.print_card()

    deck=Card_Deck()

    # deal 52 cards and print out each card (should be in order)
    for i in range(52):
      print("i:",i)
      card=deck.deal_card()
      card.print_card()
      if not i:
        card.print_card(show_back=True)

    # now shuffle the deck of cards
    deck.shuffle()

    # deal 52 cards and print out each card (should be shuffled, random)
    for i in range(52):
      print("i:",i)
      card=deck.deal_card()
      card.print_card()
      if not i:
        card.print_card(show_back=True)

    # test the get_card_image() function
    deck.shuffle()
    card=deck.deal_card()
    card_text=card.get_card_image()
    print("Card Text:")
    print(card_text)
    '''


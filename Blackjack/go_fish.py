from pokercards import *

class GoFishHand(CardHand):
    CARD_RANK = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')

    def __init__(self, name="", cards=[]):
        # You need to keep track of two things in this class:
        #   1. the cards in this hand
        #   2. the rank of (4 of a kind, cards with the same values)  You can
        #     compute the score from this.
        super().__init__(name, cards)

        self._four_ofa_kinds = []

    def get_rank_cards(self, rank):
        # removes cards with the given rank from this "hand" and returns
        # the cards as a list to the caller
        # If there aren't any cards with the given rank, then return an
        # empty list
        rank_cards = []
        raise NotImplementedError("Need to fix this code to remove from self._hand after you build rank_cards list")
        for card in self._hand:
            if card.rank_image == rank:
                rank_cards.append(card)
        return rank_cards

    def add_cards(self, cards):
        # Just like in BJHand, add cards to this "hand" but with an additional
        # function of checking if you have the full suit of a given rank
        cards_tobe_removed = []
        self._hand += cards

        card_values = [card.rank_value for card in self._hand]
        card_ranks = set(card_values)
        for each_rank in card_ranks:
            if card_values.count(each_rank) == 4:
                # remove the four of a kind rank cards from self._hand
                # add this rank value into self._four_ofa_kinds
                cards_tobe_removed.append(each_rank)
                self._four_ofa_kinds.append(each_rank)
        for rank in cards_tobe_removed:
            card_values.remove(rank)


    def get_score(self):
        # returns the number of four a kind this hand has
        pass

    def get_four_ofa_kind(self):
        # returns a list of the 4 of a kind in this "hand", you can just return
        # a list of the ranks of these four a kind
        # you can use Card.get_value() for the rank value
        return self._four_ofa_kinds


if __name__ == "__main__":
    cards = CardDeck()
    cards.shuffle()
    cards.deal_card().print()
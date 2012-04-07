class Card(object):
    cards = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

    def __init__(self, string):
        self.validate(string)
        self.value = self.cards[string[0]]
        self.suit = string[1]

    def validate(self, string):
        if not self.cards.has_key(string[0]):
            raise ValueError
        
class PokerSolver(object):
    def __init__(self):
        pass

    hands = {'high_card':1, 'pair':2, 'two_pairs':3, 'three_of_a_kind':4, 'straight':5, 'flush':6, 'full_house':7, 'four_of_a_kind':8, 'straight_flush':9}

    def solve(self, string):
        players = string.split('  ');
        
        black = players[0].split(':')
        white = players[1].split(':')

        black_name = black[0]
        white_name = white[0]

        black_cards = [Card(card) for card in black[1].split(' ')[1:6]]
        white_cards = [Card(card) for card in white[1].split(' ')[1:6]]

        black_score = self._evaluate_hand(black_cards)
        white_score = self._evaluate_hand(white_cards)

        if black_score[0] > white_score[0]:
            return black_name
        if white_score[0] > black_score[0]:
            return white_name
        if black_score[0] == white_score[0]:
            if black_score[1] > white_score[1]:
                return black_name
            if white_score[1] > black_score[1]:
                return white_name
            if black_score[1] == white_score[1]:
                return 'tie'

    def _evaluate_hand(self, hand):
        hand = self._sort_hand(hand)
 
        fifth_card_value = hand[4].value
        fourth_card_value = hand[3].value
        third_card_value = hand[2].value
        second_card_value = hand[1].value
        first_card_value = hand[0].value
 
        if self._detect_straight_flush(hand):
            return (self.hands['straight_flush'], self._detect_straight_flush(hand))
        if self._detect_some_of_a_kind(hand, 4):
            return (self.hands['four_of_a_kind'], [self._detect_some_of_a_kind(hand, 4), fifth_card_value])
        if self._detect_full_house(hand):
            return (self.hands['full_house'], self._detect_full_house(hand))
        if self._detect_flush(hand):
            return (self.hands['flush'], self._detect_flush(hand))
        if self._detect_straight(hand):
            return (self.hands['straight'], self._detect_straight(hand))
        if self._detect_some_of_a_kind(hand, 3):
            return (self.hands['three_of_a_kind'], [self._detect_some_of_a_kind(hand, 3), fifth_card_value, fourth_card_value])
        if self._detect_two_pairs(hand):
            return (self.hands['two_pairs'], [self._detect_two_pairs(hand), fifth_card_value])
        if self._detect_some_of_a_kind(hand, 2):
            return (self.hands['pair'], [self._detect_some_of_a_kind(hand, 2), fifth_card_value, fourth_card_value, third_card_value])
        return (self.hands['high_card'], [fifth_card_value, fourth_card_value, third_card_value, second_card_value, first_card_value])
    
    def _sort_hand(self, hand):
        return sorted(hand, key=lambda card: card.value)

    def _detect_two_pairs(self, hand):
        counter = {}
        pair = False
        for card in hand:
            if not counter.has_key(card.value):
                counter[card.value] = 1
            counter[card.value] += 1
            if counter[card.value] == 2:
                if pair:
                    return card.value
                pair = True
        return None

    def _detect_straight(self, hand):
        hand_in_value = sorted(list(set([card.value for card in hand])))
        if len(hand_in_value) == 5:
            if (hand_in_value[4] - hand_in_value[0]) == 4:
                return hand_in_value[4]
        return None

    def _detect_flush(self, hand):
        if (hand[0].suit == hand[1].suit) & (hand[0].suit == hand[2].suit) & (hand[0].suit == hand[3].suit) & (hand[0].suit == hand[4].suit):
            return hand[4].value
        return None

    def _detect_full_house(self, hand):
        pair = self._detect_some_of_a_kind(hand, 2)
        three_of_a_kind = self._detect_some_of_a_kind(hand, 3)
        if bool(pair) & bool(three_of_a_kind):
            return [three_of_a_kind, pair]
        return None

    def _detect_straight_flush(self, hand):
        straight = self._detect_straight(hand)
        flush = self._detect_flush(hand)
        if bool(straight) & bool(flush):
            return straight
        return None

    def _detect_some_of_a_kind(self, hand, some):
        counter = {}
        for card in hand:
            if not counter.has_key(card.value):
                counter[card.value] = 1
            counter[card.value] += 1
            if counter[card.value] == some:
                return card.value
        return None

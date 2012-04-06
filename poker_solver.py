class PokerSolver(object):
    def __init__(self):
        pass
        
    cards = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}
    hands = {'nothing':None, 'high_card':1, 'pair':2, 'two_pairs':3, 'three_of_a_kind':4, 'straight':5, 'flush':6, 'full_house':7, 'four_of_a_kind':8, 'straight_flush':9}
    
    def solve(self, hand):
        part = hand.split(' ');
        black_hand = part[1:6]
        white_hand = part[8:]
        
        black_score = self._evaluate_hand(black_hand)
        white_score = self._evaluate_hand(white_hand)
        
        if black_score[0] > white_score[0]:
            return 'black'
        if white_score[0] > black_score[0]:
            return 'white'
        if black_score[0] == white_score[0]:
            if black_score[1] > white_score[1]:
                return 'black'
            if white_score[1] > black_score[1]:
                return 'white'
            return 'tie'
    
    def _evaluate_hand(self, hand):
        if self._detect_straight(hand):
            return (self.hands['straight'], self._detect_straight(hand))
        if self._detect_three_of_a_kind(hand):
            return (self.hands['three_of_a_kind'], self._detect_three_of_a_kind(hand))
        if self._detect_two_pairs(hand):
            return (self.hands['two_pairs'], self._detect_two_pairs(hand))
        if self._detect_pairs(hand):
            return (self.hands['pair'], self._detect_pairs(hand))
        if self._detect_high_card(hand):
            return (self.hands['high_card'], self._detect_high_card(hand))
        return (self.hands['nothing'], None)

    def _detect_high_card(self, hand):
        high_card = 0
        for card in hand:
            if self.cards[card[0]] > high_card:
                high_card = self.cards[card[0]]
        return high_card

    def _detect_pairs(self, hand):
        counter = dict([(card, 0) for card in self.cards.viewkeys()]) 
        for card in hand:
            counter[card[0]] += 1
            if counter[card[0]] == 2:
                return self.cards[card[0]]
        return None

    def _detect_two_pairs(self, hand):
        counter = dict([(card, 0) for card in self.cards.keys()])
        pair = False
        for card in hand:
            counter[card[0]] += 1
            if counter[card[0]] == 2:
                if pair:
                    return self.cards[card[0]]
                pair = True
        return None

    def _detect_three_of_a_kind(self, hand):
        counter = dict([(card, 0) for card in self.cards.keys()]) 
        for card in hand:
            counter[card[0]] += 1
            if counter[card[0]] == 3:
                return self.cards[card[0]]
        return None
    
    def _detect_straight(self, hand):
        counter = dict([(card, 0) for card in self.cards.keys()])
        for card in hand:
            counter[card[0]] += 1
        return None

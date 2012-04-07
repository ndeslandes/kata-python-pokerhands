class PokerSolver(object):
    def __init__(self):
        pass
        
    cards = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
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
        if self._detect_pair(hand):
            return (self.hands['pair'], self._detect_pair(hand))
        if self._detect_high_card(hand):
            return (self.hands['high_card'], self._detect_high_card(hand))
        return (self.hands['nothing'], None)
    
    def _convert_in_value(self, hand):
        hand_in_value = []
        for card in hand:
            hand_in_value.append(self.cards[card[0]])
        return hand_in_value

    def _detect_high_card(self, hand):
        hand_in_value = self._convert_in_value(hand)
        high_card = None
        for card in hand_in_value:
            if card > high_card:
                high_card = card
        return high_card

    def _detect_pair(self, hand):
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
        hand_in_value = self._convert_in_value(hand)
        hand_in_value = list(set(hand_in_value))
        hand_in_value.sort()
        if len(hand_in_value) == 5:
            if hand_in_value[4]-hand_in_value[0] == 4:
                return hand_in_value[4]
        return None

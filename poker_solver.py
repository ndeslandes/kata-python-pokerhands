class PokerSolver(object):
    def __init__(self):
        pass
        
    cards = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    sets = ['H', 'S', 'C', 'D']
    hands = {'high_card':1, 'pair':2, 'two_pairs':3, 'three_of_a_kind':4, 'straight':5, 'flush':6, 'full_house':7, 'four_of_a_kind':8, 'straight_flush':9}
    
    def solve(self, hands):
        hand = hands.split('  ');
        
        black_name = hand[0].split(':')[0]
        white_name = hand[1].split(':')[0]

        black_hand = hand[0].split(':')[1].split(' ')[1:6]
        white_hand = hand[1].split(':')[1].split(' ')[1:6]
        
        black_score = self._evaluate_hand(black_hand)
        white_score = self._evaluate_hand(white_hand)
        
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
        fifth_card_value = self.cards[hand[4][0]]
        fourth_card_value = self.cards[hand[3][0]]
        third_card_value = self.cards[hand[2][0]]
        second_card_value = self.cards[hand[1][0]]
        first_card_value = self.cards[hand[0][0]]
        if self._detect_straight_flush(hand):
            return (self.hands['straight_flush'], self._detect_straight_flush(hand))
        if self._detect_four_of_a_kind(hand):
            return (self.hands['four_of_a_kind'], [self._detect_four_of_a_kind(hand), fifth_card_value])
        if self._detect_full_house(hand):
            return (self.hands['full_house'], self._detect_full_house(hand))
        if self._detect_flush(hand):
            return (self.hands['flush'], self._detect_flush(hand))
        if self._detect_straight(hand):
            return (self.hands['straight'], self._detect_straight(hand))
        if self._detect_three_of_a_kind(hand):
            return (self.hands['three_of_a_kind'], [self._detect_three_of_a_kind(hand), fifth_card_value, fourth_card_value])
        if self._detect_two_pairs(hand):
            return (self.hands['two_pairs'], [self._detect_two_pairs(hand), fifth_card_value])
        if self._detect_pair(hand):
            return (self.hands['pair'], [self._detect_pair(hand), fifth_card_value, fourth_card_value, third_card_value])
        return (self.hands['high_card'], [fifth_card_value, fourth_card_value, third_card_value, second_card_value, first_card_value])
    
    def _convert_in_value(self, hand):
        hand_in_value = []
        for card in hand:
            hand_in_value.append(self.cards[card[0]])
        return hand_in_value
    
    def _sort_hand(self, hand):
        return sorted(hand, key=lambda card: self.cards[card[0]])

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
                return [hand_in_value[4]]
        return None

    def _detect_flush(self, hand):
        counter = dict([(a_set, 0) for a_set in self.sets])
        for card in hand:
            counter[card[1]] += 1
            if counter[card[1]] == 5:
                return [self.cards[card[0]]]
        return None
    
    def _detect_full_house(self, hand):
        pair = self._detect_pair(hand)
        three_of_a_kind = self._detect_three_of_a_kind(hand)
        if bool(pair) & bool(three_of_a_kind):
            return [three_of_a_kind, pair]
        return None

    def _detect_four_of_a_kind(self, hand):
        counter = dict([(card, 0) for card in self.cards.keys()]) 
        for card in hand:
            counter[card[0]] += 1
            if counter[card[0]] == 4:
                return self.cards[card[0]]
        return None

    def _detect_straight_flush(self, hand):
        straight = self._detect_straight(hand)
        flush = self._detect_flush(hand)
        if bool(straight) & bool(flush):
            return straight
        return None

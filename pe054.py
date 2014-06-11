# -*- coding: utf-8 -*-
# Answer 376


class PlayingCard(object):
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __repr__(self):
        return '{{ value: {0.value}, suit: "{0.suit}"}}'.format(self)
        
    def __eq__(self, card2):
        return self.value == card2.value
    
    def __ne__(self, card2):
        return self.value != card2.value
        
    def __gt__(self, card2):
        return self.value > card2.value

    def __ge__(self, card2):
        return self.value >= card2.value
    
    def __lt__(self, card2):
        return self.value < card2.value
        
    def __le__(self, card2):
        return self.value <= card2.value
        
        
class PokerHand(object):
            
    def __init__(self, cards):
        self.RANKS = [None, self.high_card, self.pair, self.two_pair,
                      self.three_oak, self.straight, self.flush, 
                      self.full_house, self.four_oak, self.straight_flush,
                      self.royal_flush]
        self.cards = cards
        self.rank = None
        self.score()

    def __repr__(self):
        return ('{{ cards: {0.cards}, ' +
                ' rank: {0.rank.__name__}}}').format(self)
        
    def royal_flush(self):
        if self.straight_flush() and sorted(self.cards)[4].value == 14:
            return sorted(self.cards)
        return None
    
    def straight_flush(self):
        if self.flush() and self.straight():
            return sorted(self.cards)
        return None
    
    def four_oak(self):
        return [x for x in sorted(self.cards) 
                    if len([y for y in self.cards if y == x]) == 4]
    
    def full_house(self):
        two = [x for x in sorted(self.cards) 
                    if len([y for y in self.cards if y == x]) == 2]
        three = [x for x in sorted(self.cards) 
                    if len([y for y in self.cards if y == x]) == 3]
        if two and three:
            return three + two
        return None
        
    def flush(self):
        suit = self.cards[0].suit
        cards_of_suit = [x for x in self.cards if x.suit == suit]
        if len(cards_of_suit) == 5:
            return sorted(self.cards)
        return None
    
    def straight(self):
        self.cards.sort()
        span = self.cards[4].value - self.cards[0].value
        if span == 4 and len(set(x.value for x in self.cards)) == 5:
            return self.cards
        return None
        
    def three_oak(self):
        return [x for x in sorted(self.cards) 
                    if len([y for y in self.cards if y == x]) == 3]
    
    def two_pair(self):
        pairs =  [x for x in sorted(self.cards) 
                    if len([y for y in self.cards if y == x]) == 2]
        return pairs if len(pairs) == 4 else None
                
    def pair(self):
        return [x for x in sorted(self.cards) 
                    if len([y for y in self.cards if y == x]) == 2]
    
    def high_card(self):
        return [sorted(self.cards)[-1]]
    
    def score(self):
        for each in [x for x in self.RANKS[::-1] if x]:
            if each():
                self.rank = each
                break
    
    def rank_level(self):
        return self.RANKS.index(self.rank)
    
    def __gt__(self, hand2):
        if self.rank_level() > hand2.rank_level():
            return True
        elif self.rank_level() == hand2.rank_level():
            cards1, cards2 = self.rank(), hand2.rank()
            while cards1 and cards2:
                c1, c2 = cards1.pop(-1), cards2.pop(-1)
                if c1 > c2: return True
                elif c1 < c2: return False
            cards1, cards2 = sorted(self.cards), sorted(hand2.cards)
            while cards1 and cards2:
                c1, c2 = cards1.pop(-1), cards2.pop(-1)
                if c1 > c2: return True
                elif c1 < c2: return False
            return False
        else:
            return False

def split_hands():        
    value = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    f = open('data\pe054_poker.txt')
    
    for line in f.readlines():
        rd = [(int(value.get(l[0],l[0])), l[1]) for l in line[:29].split(' ')]
        rd = [PlayingCard(*card) for card in rd]
        yield PokerHand(rd[:5]), PokerHand(rd[5:])

def answer():
    wins = 0    
    for p1, p2 in split_hands():
        if p1 > p2:
            wins += 1    
    return wins

if __name__ == '__main__':
    print(answer())
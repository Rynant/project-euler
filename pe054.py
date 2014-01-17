# -*- coding: utf-8 -*-
raise Exception('Not complete')

RANK_MULTIPLIER = 14


def card_values(cards):
    return list(x[0] for x in cards)
    
def royal_flush(cards):
    pass

def straight_flush(cards):
    pass

def four_oak(cards):
    pass

def full_house(cards):
    pass

def flush(cards):
    pass

def straight(cards):
    pass

def three_oak(cards):
    '''Takes list of card values.'''
    pairs = sorted([x for x in cards if cards.count(x) == 3])
    return (pairs[-1] if pairs else 0) * RANK_MULTIPLIER * 3

def two_pair(cards):
    '''Takes list of card values.'''
    pairs = sorted([x for x in cards if cards.count(x) == 2])
    return (pairs[-1] if len(pairs) == 4 else 0) * RANK_MULTIPLIER * 2

def pair(cards):
    '''Takes list of card values.'''
    pairs = sorted([x for x in cards if cards.count(x) == 2])
    return (pairs[-1] if pairs else 0) * RANK_MULTIPLIER * 1

def high_card(cards):
    return sorted(i[0] for i in cards)[-1]

def score(cards):
    pass

def split_hands():        
    value = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    f = open('pe054_poker.txt')
    
    for line in f.readlines():
        # Split each round into tuples of the hands ()
        rd = [(int(value.get(l[0],l[0])), l[1]) for l in line[:29].split(' ')]
        yield rd[:5], rd[5:]


wins = 0

for hand in split_hands():
    print(hand)
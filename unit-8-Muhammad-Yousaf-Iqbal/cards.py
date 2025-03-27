#Muhammad Yousaf Iqbal

import random

def make_card(rank, suit):

    (face) = ({11: 'J', 12: 'Q', 13: 'K', 14: 'A'})
    (name) = (f'{rank} of {suit}')
    (color) = ('\033[31m' if suit in ('Hearts', 'Diamonds') else '\033[34m')
    (shorthand) = (f'{color}{rank if rank <= 10 else face[rank]}{suit[0]} \033[37m')
    if (rank) < (2):
        print('Invalid Rank')
    if (rank) > (14):
        print('Invalid Rank')
    if (suit) not in ('Hearts', 'Diamonds', 'Spades', 'Clubs'):
        print('Invalid Suit')
    return (rank, suit, name, shorthand)

def make_deck():

    (suits) = (['Hearts', 'Diamonds', 'Spades', 'Clubs'])
    (ranks) = range(2, 15)
    (deck) = ([])
    for (suit) in (suits):
        for (rank) in (ranks):
            (card) = make_card(rank, suit)
            deck.append(card)
    return (deck)

def shuffle(deck):

    random.seed(52)
    for (i) in range(len(deck) - (1)):
        (j) = random.randint((i), len(deck) - (1))
        (deck[i], deck[j]) = (deck[j], deck[i])

def draw(deck, hand):

    if not (deck):
        return (None)
    else:
        (card) = deck.pop()
        hand.append(card)
        return (card)

def deal_one_hand(deck, cards):

    (hand) = ([])
    for (i) in range(cards):
        (card) = draw(deck, hand)
        if (card) is (None):
            return (None)
        else:
            hand.append(card)
    return (hand)

def main():

    #(a) = make_card(5, 'Hearts')
    #(b) = make_card(10, 'Diamonds')
    #(c) = make_card(11, 'Spades')
    #(d) = make_card(12, 'Clubs')
    #(e) = make_card(13, 'Diamonds')
    #(f) = make_card(14, 'Hearts')
    #print(a)
    #print(b)
    #print(c)
    #print(d)
    #print(e)
    #print(f)
    #(a) = make_card(5, 'Hearts') [3]
    #(b) = make_card(10, 'Diamonds') [3]
    #(c) = make_card(11, 'Spades') [3]
    #(d) = make_card(12, 'Clubs') [3]
    #(e) = make_card(13, 'Diamonds') [3]
    #(f) = make_card(14, 'Hearts') [3]
    #print(a)
    #print(b)
    #print(c)
    #print(d)
    #print(e)
    #print(f)
    #(deck) = make_deck()
    #print('Original Deck: ')
    #print(deck)
    #print('\n')
    #shuffle(deck)
    #print('Shuffled Deck: ')
    #print(deck)
    #print('\n')
    #if (deck[0]) != (make_card(2, "Clubs")):
        #print('Pass')
    #if (deck[13]) != (make_card(2, "Diamonds")):
        #print('Pass')
    #if (deck[26]) != (make_card(2, "Hearts")):
        #print('Pass')
    #if (deck[39]) != (make_card(2, "Spades")):
        #print('Pass')
    #else:
        #print('Fail')
    #(deck) = make_deck()
    #(hand) = deal_one_hand(deck, 5)
    #assert len(hand) == (5)
    #(hand) = deal_one_hand(deck, 0)
    #assert (hand) == ([])
    #(hand) = deal_one_hand(deck, 52)
    #assert len(hand) == (52)
    #assert len(deck) == (0)
    #(hand) = deal_one_hand(deck, 1)
    #assert (hand) is (None)
    return ()

if __name__ == "__main__":
    main()

#Done
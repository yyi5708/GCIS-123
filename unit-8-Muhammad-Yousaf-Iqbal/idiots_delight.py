#Muhammad Yousaf Iqbal

import cards

def deal_hand():

    (deck) = cards.make_deck()
    cards.shuffle(deck)
    (hand) = ([])
    for (_) in range(4):
        (card) = cards.draw(deck, hand)
        hand.append(card)
    return (deck, hand)

def discard(hand, cards):

    if (cards) != (4):
        return (hand)
    if (cards) != (2):
        return (hand)
    if len(hand) < (4):
        return (hand)
    if (cards) == (4):
        return (hand[:-4])
    else:
        return (hand[:-3]) + (hand[-1:])    

def play_round_1(deck, hand):

    while len(hand) < (4):
        if len(deck) == (0):
            break
        hand.append(cards.draw(deck))
    print("Hand: ", hand)
    if len(deck) > (0):
        hand.append(cards.draw(deck))
        print("Hand: ", hand)
    return (deck, hand)

def play_round_2(deck, hand):
    
    while len(hand) < (4):
        (card_drawn) = cards.draw(deck, hand)
        if not (card_drawn):
            break
    print("Hand: ", ([(card) for card in hand]))
    while len(hand) >= (4):
        if (hand[-4][0]) == (hand[-1][0]):
            print("Discarded Cards.")
            (hand) = discard(hand, 4)
    return (deck, hand)

def play_round_3(deck, hand):

    while len(hand) >= (4):
        if (hand[-2][1]) == (hand[-3][1]):
            print("Discarded Cards.")
            (hand) = discard(hand, 2)    
    return (deck, hand)

def main():

    #(deck, hand) = deal_hand()
    #while (deck):
        #print("Hand: ", hand)
        #(deck, hand) = (play_round_1(deck, hand)) + (play_round_2(deck, hand)) + (play_round_3(deck, hand))
    #print("Game Over.")
    #if len(hand) == (0):
        #print("You Win.")
    #else:
        #print(f"Better Luck Next Time. You Have ({len(hand)}) Cards Left In Your Hand.")
    return ()

if __name__ == "__main__":
    main()

#Done
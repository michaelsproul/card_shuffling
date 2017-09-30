import random

CLUB = 0
SPADE = 1
DIAMOND = 2
HEART = 3

def flatten(l):
    result = []
    for sublist in l:
        result.extend(sublist)
    return result

def starting_deck():
    remainder = [CLUB, CLUB, SPADE, SPADE, DIAMOND, DIAMOND, HEART, HEART]
    random.shuffle(remainder)

    deck = 2 * [([CLUB] * 4)] + 2 * [([SPADE] * 4)] + 2 * [([DIAMOND] * 4)] + 2 * [([HEART] * 4)] + [remainder[:4], remainder[4:]]
    random.shuffle(deck)
    return flatten(deck)

def dad_shuffle(deck, period=7):
    piles = [deck[i::period] for i in range(0, period)]
    random.shuffle(piles)
    return flatten(piles)

def random_shuffle(deck):
    result = deck.copy()
    random.shuffle(result)
    return result

def deal(deck):
    start1 = 4 * 3
    start2 = 4 * 7
    player_cards = [deck[3 * i:3 * i + 3] + deck[start1 + 4 * i:start1 + 4 * i + 4] + deck[start2 + 3 * i:start2 + 3 * i + 3] for i in range(0, 4)]
    return player_cards

def is_exceptional(hand, k=5):
    m = {suit: 0 for suit in range(CLUB, HEART + 1)}
    for suit in hand:
        m[suit] += 1

    for suit in range(CLUB, HEART + 1):
        if m[suit] >= k:
            return True
    return False

def compare(k=5, period=7, iterations=10000):
    dad_exceptional = 0
    rand_exceptional = 0

    for i in range(0, iterations):
        s = starting_deck()

        dad = dad_shuffle(s, period)
        rand = random_shuffle(s)

        dad_exceptional += sum(is_exceptional(hand, k) for hand in deal(dad))
        rand_exceptional += sum(is_exceptional(hand, k) for hand in deal(rand))

    total_hands = 4 * iterations
    print("dad_exceptional: {1}/{0}, rand_exceptional: {2}/{0}".format(total_hands, dad_exceptional, rand_exceptional))

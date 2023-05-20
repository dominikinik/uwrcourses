import random
wartosc_kart = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

wszystkie_kolory = [
    'SCZ',
    'SCZER',
    'ZAL',
    'DZW'
]

Figurant = [
    'A1', 'A2', 'A3', 'A4',
    'K1', 'K2', 'K3', 'K4',
    'Q1', 'Q2', 'Q3', 'Q4',
    'J1', 'J2', 'J3', 'J4'
]

Blotkarz = [
    21, 22, 23, 24,
    31, 32, 33, 34,
    41, 42, 43, 44,
    51, 52, 53, 54,
    61, 62, 63, 64,
    71, 72, 73, 74,
    81, 82, 83, 84,
    91, 92, 93, 94,
    101, 102, 103, 104
]


def straight_flush(reka):
    suits = reka[1]
    cards = [wartosc_kart[card] for card in reka[0]]
    cards.sort()

    for i in range(1, len(cards)):
        if cards[i] != cards[i - 1] + 1:
            return False

        if suits[i] != suits[i - 1]:
            return False

    return sum(cards)


def four_of_a_kind(reka):
    cards = [wartosc_kart[card] for card in reka[0]]
    cards.sort()

    first_4 = cards[0] == cards[1] == cards[2] == cards[3]
    last_4 = cards[1] == cards[2] == cards[3] == cards[4]
    if first_4 or last_4:
        return True

    return False


def full_house(reka):
    cards = [wartosc_kart[card] for card in reka[0]]
    cards.sort()

    first_3 = cards[0] == cards[1] == cards[2]
    last_2 = cards[3] == cards[4]

    first_2 = cards[0] == cards[1]
    last_3 = cards[2] == cards[3] == cards[4]

    if first_3 and last_2 or first_2 and last_3:
        return True

    return False


def flush(reka):
    suits = reka[1]
    cards = [wartosc_kart[card] for card in reka[0]]
    cards.sort(reverse=True)

    for i in range(1, len(cards)):
        if suits[i] != suits[i - 1]:
            return False

    return True


def straight(reka):
    cards = [wartosc_kart[card] for card in reka[0]]
    cards.sort()

    for i in range(1, len(cards)):
        if cards[i] != cards[i - 1] + 1:
            return False

    return True


def three_of_a_kind(reka):
    cards = [wartosc_kart[card] for card in reka[0]]
    cards.sort()

    first_3 = cards[0] == cards[1] == cards[2]
    middle_3 = cards[1] == cards[2] == cards[3]
    last_3 = cards[2] == cards[3] == cards[4]

    if first_3 or middle_3 or last_3:
        return True

    return False


def two_pairs(reka):
    cards = [wartosc_kart[card] for card in reka[0]]
    cards.sort()

    pair_first = cards[0] == cards[1]
    pair_mid_l = cards[1] == cards[2]
    pair_mid_r = cards[2] == cards[3]
    pair_last = cards[3] == cards[4]

    if pair_first and pair_mid_r or pair_first and pair_last or pair_mid_l and pair_last:
        return True

    return False


def one_pair(reka):
    cards = [wartosc_kart[card] for card in reka[0]]
    cards.sort()

    pair_1 = cards[0] == cards[1]
    pair_2 = cards[1] == cards[2]
    pair_3 = cards[2] == cards[3]
    pair_4 = cards[3] == cards[4]

    if pair_1 or pair_2 or pair_3 or pair_4:
        return True

    return False


def reka_fig(n):
    cards = []
    suits = []

    cards = random.sample(Figurant, n)
    suits = [wszystkie_kolory[int(card[-1]) - 1] for card in cards]
    cards = [card[:-1] for card in cards]

    return (cards, suits)


def reka_blo(n, rodzaj):
    cards = []
    suits = []

    cards = random.sample(rodzaj, n)
    suits = [wszystkie_kolory[card % 10 - 1] for card in cards]
    cards = [card // 10 for card in cards]

    return (cards, suits)


def symulacja(hand_size):

    Figurant_hand = reka_fig(hand_size)
    Blotkarz_hand = reka_blo(hand_size, Blotkarz_1)  # zmiana

    hand_rankings = [straight_flush, four_of_a_kind, full_house,
                     flush, straight, three_of_a_kind, two_pairs, one_pair]

    for ranking in hand_rankings:
        fig = ranking(Figurant_hand)
        blt = ranking(Blotkarz_hand)

        if fig is False and blt:
            return (0, 1)

        if fig and blt is False:
            return (1, 0)

        if fig and blt:
            return (1, 0)


proba = 26921
figur = 0
blotk = 0
reka = 5
# lepsze talie
Blotkarz_1 = [21, 31, 41, 51, 61, 71, 81, 91, 101]

Blotkarz_2 = [91, 92, 93, 94, 101, 102, 103, 104, 81, 82, 83, 84]

for i in range(proba):
    wyn = symulacja(reka)
    figur += wyn[0]
    blotk += wyn[1]

print(f'po {proba} grach szanse zwyciestwa blotkarza to: {blotk / proba * 100}% ')

import math
import re


test_result = 30


def main(input_file):
    winning_regex = r"(\d+)(?=.*[\|^])(?!.*:)"

    with open(input_file, "r") as f:
        lines = f.readlines()
    
    cards = [re.split("[\|:]", x.strip()) for x in lines]
    card_values = 0

    original_length = len(cards)
    i = 0
    while i < len(cards):
        winning_cards = set(cards[i][1].strip().split())
        owned_cards = set(cards[i][2].strip().split())

        matching_cards = len(owned_cards & winning_cards)

        card_values += math.floor(2**(matching_cards-1))


        # Append copied cards to end of cards
        cards.extend(cards[(i+1):(i+1+matching_cards)])

        i += 1

    print(cards)
        
    
    return card_values
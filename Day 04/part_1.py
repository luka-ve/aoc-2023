import math
import re


test_result = 13


def main(input_file):
    winning_regex = r"(\d+)(?=.*[\|^])(?!.*:)"

    with open(input_file, "r") as f:
        lines = f.readlines()
    
    cards = [re.split("[\|:]", x.strip()) for x in lines]
    card_values = 0
    
    for card in cards:
        winning_cards = set(card[1].strip().split())
        owned_cards = set(card[2].strip().split())
        card_values += math.floor(2**(len(owned_cards & winning_cards)-1))
    
    return card_values
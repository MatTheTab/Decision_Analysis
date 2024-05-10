import numpy as np
from player import Player
import random

class MyRandom_Default(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = random.choice(self.cards)    
        if declared_card is not None and declared_card[0] > called_card[0]:
            called_card = declared_card
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return np.random.choice([False, True])
    
class MyRandom_All_Cards(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        all_cards = [(number, color) for color in range(4) for number in range(9, 15)]
        possible_cards = []
        for card in all_cards:
            if declared_card is None or card[0] >= declared_card[0]:
                possible_cards.append(card)
        called_card = random.choice(possible_cards)
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return np.random.choice([False, True])
    
class MyRandom_Real_Cards(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        possible_cards = []
        for card in self.cards:
            if declared_card is None or card[0] >= declared_card[0]:
                possible_cards.append(card)
        if len(possible_cards) > 0:
            called_card = random.choice(possible_cards)
        else:
            all_cards = [(number, color) for color in range(4) for number in range(9, 15)]
            possible_cards = []
            for card in all_cards:
                if declared_card is None or card[0] >= declared_card[0]:
                    possible_cards.append(card)
            called_card = random.choice(possible_cards)
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return np.random.choice([False, True])
    
class Random_Never_Accuse(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = random.choice(self.cards)    
        if declared_card is not None and declared_card[0] > called_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return False
    
class Random_Always_Accuse(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = random.choice(self.cards)    
        if declared_card is not None and declared_card[0] > called_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return True
    
class Mimic(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        if declared_card is not None:
            called_card = declared_card
        else:
            called_card = true_card 
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return False
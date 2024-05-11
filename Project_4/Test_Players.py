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
    
class Saint_Believer(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        available_cards = []
        for card in self.cards:
            if declared_card is None or card[0] >= declared_card[0]:
                available_cards.append(card)
        available_cards = sorted(available_cards, key=lambda x: x[0])
        if len(available_cards) > 0:
            true_card = available_cards[0]
            called_card = available_cards[0]
        else:
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
            if declared_card[0] == 14:
                called_card = (14, np.random.randint(0, 3))
            else:
                called_card = (np.random.randint(declared_card[0], 14), np.random.randint(0, 3))
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return False
    
class Saint_Once_in_a_While(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        available_cards = []
        for card in self.cards:
            if declared_card is None or card[0] >= declared_card[0]:
                available_cards.append(card)
        available_cards = sorted(available_cards, key=lambda x: x[0])
        if len(available_cards) > 0:
            true_card = available_cards[0]
            called_card = available_cards[0]
        else:
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
            if declared_card[0] == 14:
                called_card = (14, np.random.randint(0, 4))
            else:
                called_card = (np.random.randint(declared_card[0], 15), np.random.randint(0, 4))
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        number = np.random.randint(0, 10)
        if number == 0:
            return True
        return False
    
class Saint_Two_Face(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        available_cards = []
        for card in self.cards:
            if declared_card is None or card[0] >= declared_card[0]:
                available_cards.append(card)
        available_cards = sorted(available_cards, key=lambda x: x[0])
        if len(available_cards) > 0:
            true_card = available_cards[0]
            called_card = available_cards[0]
        else:
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
            if declared_card[0] == 14:
                called_card = (14, np.random.randint(0, 4))
            else:
                called_card = (np.random.randint(declared_card[0], 15), np.random.randint(0, 4))
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return np.random.choice([False, True])
    
class Saint_Accountant(Player):
    def __init__(self, name):
        super().__init__(name)
        self.prob_call = 0.5
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        available_cards = []
        for card in self.cards:
            if declared_card is None or card[0] >= declared_card[0]:
                available_cards.append(card)
        available_cards = sorted(available_cards, key=lambda x: x[0])
        if len(available_cards) > 0:
            true_card = available_cards[0]
            called_card = available_cards[0]
        else:
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
            if declared_card[0] == 14:
                called_card = (14, np.random.randint(0, 4))
            else:
                called_card = (np.random.randint(declared_card[0], 15), np.random.randint(0, 4))
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        random_float = np.random.rand()
        if random_float <= self.prob_call:
            return True
        return False
    
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log = True):
        if iChecked and iDrewCards:
            self.prob_call /= 2
        elif iChecked and not iDrewCards:
            self.prob_call *= 2
            if self.prob_call > 1.0:
                self.prob_call = 1.0

class Saint_Nervous(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        available_cards = []
        for card in self.cards:
            if declared_card is None or card[0] >= declared_card[0]:
                available_cards.append(card)
        available_cards = sorted(available_cards, key=lambda x: x[0])
        if len(available_cards) > 0:
            true_card = available_cards[0]
            called_card = available_cards[0]
        else:
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
            if declared_card[0] == 14:
                called_card = (14, np.random.randint(0, 4))
            else:
                called_card = (np.random.randint(declared_card[0], 15), np.random.randint(0, 4))
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        available_cards = sorted(self.cards, key=lambda x: x[0])
        if available_cards[-1][0] < opponent_declaration[0]:
            return True
        return False
    
class Saint_Collector(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        available_cards = []
        for card in self.cards:
            if declared_card is None or card[0] >= declared_card[0]:
                available_cards.append(card)
        available_cards = sorted(available_cards, key=lambda x: x[0])
        if len(available_cards) > 0:
            true_card = available_cards[0]
            called_card = available_cards[0]
        else:
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
            if declared_card[0] == 14:
                called_card = (14, np.random.randint(0, 4))
            else:
                called_card = (np.random.randint(declared_card[0], 15), np.random.randint(0, 4))
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        num_cards = 1
        for card in self.cards:
            if card[0] == opponent_declaration[0]:
                num_cards += 1
        if num_cards == 4:
            return True
        return False
    
class Dabbler_Believer(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        random_int = np.random.randint(0, 10)
        if random_int == 0:
            cheat = True
        else:
            cheat = False
        if cheat:
            called_card = random.choice(self.cards)             
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return False
    
class Dabbler_Once_in_a_While(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        random_int = np.random.randint(0, 10)
        if random_int == 0:
            cheat = True
        else:
            cheat = False
        if cheat:
            called_card = random.choice(self.cards)             
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        number = np.random.randint(0, 10)
        if number == 0:
            return True
        return False
    
class Dabbler_Two_Face(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        random_int = np.random.randint(0, 10)
        if random_int == 0:
            cheat = True
        else:
            cheat = False
        if cheat:
            called_card = random.choice(self.cards)             
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return np.random.choice([False, True])
    
class Dabbler_Accountant(Player):
    def __init__(self, name):
        super().__init__(name)
        self.prob_call = 0.5
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        random_int = np.random.randint(0, 10)
        if random_int == 0:
            cheat = True
        else:
            cheat = False
        if cheat:
            called_card = random.choice(self.cards)             
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        random_float = np.random.rand()
        if random_float <= self.prob_call:
            return True
        return False
    
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log = True):
        if iChecked and iDrewCards:
            self.prob_call /= 2
        elif iChecked and not iDrewCards:
            self.prob_call *= 2
            if self.prob_call > 1.0:
                self.prob_call = 1.0

class Dabbler_Nervous(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        random_int = np.random.randint(0, 10)
        if random_int == 0:
            cheat = True
        else:
            cheat = False
        if cheat:
            called_card = random.choice(self.cards)             
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        available_cards = sorted(self.cards, key=lambda x: x[0])
        if available_cards[-1][0] < opponent_declaration[0]:
            return True
        return False
    
class Dabbler_Collector(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        random_int = np.random.randint(0, 10)
        if random_int == 0:
            cheat = True
        else:
            cheat = False
        if cheat:
            called_card = random.choice(self.cards)             
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        num_cards = 1
        for card in self.cards:
            if card[0] == opponent_declaration[0]:
                num_cards += 1
        if num_cards == 4:
            return True
        return False
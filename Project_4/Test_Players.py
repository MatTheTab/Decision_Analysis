import numpy as np
from player import Player
import random
from collections import deque

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

class Coin_Flipper_Believer(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = np.random.choice([False, True])
        if cheat:
            called_card = random.choice(self.cards)             
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return False
    
class Coin_Flipper_Once_in_a_While(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = np.random.choice([False, True])
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
    
class Coin_Flipper_Two_Face(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = np.random.choice([False, True])
        if cheat:
            called_card = random.choice(self.cards)             
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return np.random.choice([False, True])
    
class Coin_Flipper_Accountant(Player):
    def __init__(self, name):
        super().__init__(name)
        self.prob_call = 0.5
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = np.random.choice([False, True])
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

class Coin_Flipper_Nervous(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = np.random.choice([False, True])
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
    
class Coin_Flipper_Collector(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = np.random.choice([False, True])
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

class Pathological_Believer(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = True
        if cheat:
            called_card = random.choice(self.cards)             
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return False
    
class Pathological_Once_in_a_While(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = True
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
    
class Pathological_Two_Face(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = True
        if cheat:
            called_card = random.choice(self.cards)             
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return np.random.choice([False, True])
    
class Pathological_Accountant(Player):
    def __init__(self, name):
        super().__init__(name)
        self.prob_call = 0.5
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = True
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

class Pathological_Nervous(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = True
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
    
class Pathological_Collector(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        true_card = random.choice(self.cards)
        called_card = true_card
        cheat = True
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
    
class Pusher_Believer(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        card_counts = {item[0]: sum(1 for tup in self.cards if tup[0] == item[0]) for item in self.cards}
        cheat = False
        for key in card_counts:
            if card_counts[key] == 1:
                cheat = True
                break
        if cheat:
            called_card = random.choice(self.cards)
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
        else:
            available_cards = []
            for card in self.cards:
                if declared_card is None or card[0]>=declared_card[0]:
                    available_cards.append(card)
            available_cards = sorted(available_cards, key=lambda x: x[0])    
            if len(available_cards) == 0:
                called_card = random.choice(self.cards)
                available_cards = self.cards
                available_cards = sorted(available_cards, key=lambda x: x[0])
                true_card = available_cards[0]
            else:
                true_card = available_cards[0]
                called_card = true_card       
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return False
    
class Pusher_Once_in_a_While(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        card_counts = {item[0]: sum(1 for tup in self.cards if tup[0] == item[0]) for item in self.cards}
        cheat = False
        for key in card_counts:
            if card_counts[key] == 1:
                cheat = True
                break
        if cheat:
            called_card = random.choice(self.cards)
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
        else:
            available_cards = []
            for card in self.cards:
                if declared_card is None or card[0]>=declared_card[0]:
                    available_cards.append(card)
            available_cards = sorted(available_cards, key=lambda x: x[0])    
            if len(available_cards) == 0:
                called_card = random.choice(self.cards)
                available_cards = self.cards
                available_cards = sorted(available_cards, key=lambda x: x[0])
                true_card = available_cards[0]
            else:
                true_card = available_cards[0]
                called_card = true_card       
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        number = np.random.randint(0, 10)
        if number == 0:
            return True
        return False
    
class Pusher_Two_Face(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        card_counts = {item[0]: sum(1 for tup in self.cards if tup[0] == item[0]) for item in self.cards}
        cheat = False
        for key in card_counts:
            if card_counts[key] == 1:
                cheat = True
                break
        if cheat:
            called_card = random.choice(self.cards)
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
        else:
            available_cards = []
            for card in self.cards:
                if declared_card is None or card[0]>=declared_card[0]:
                    available_cards.append(card)
            available_cards = sorted(available_cards, key=lambda x: x[0])    
            if len(available_cards) == 0:
                called_card = random.choice(self.cards)
                available_cards = self.cards
                available_cards = sorted(available_cards, key=lambda x: x[0])
                true_card = available_cards[0]
            else:
                true_card = available_cards[0]
                called_card = true_card       
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        return np.random.choice([False, True])
    
class Pusher_Accountant(Player):
    def __init__(self, name):
        super().__init__(name)
        self.prob_call = 0.5
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        card_counts = {item[0]: sum(1 for tup in self.cards if tup[0] == item[0]) for item in self.cards}
        cheat = False
        for key in card_counts:
            if card_counts[key] == 1:
                cheat = True
                break
        if cheat:
            called_card = random.choice(self.cards)
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
        else:
            available_cards = []
            for card in self.cards:
                if declared_card is None or card[0]>=declared_card[0]:
                    available_cards.append(card)
            available_cards = sorted(available_cards, key=lambda x: x[0])    
            if len(available_cards) == 0:
                called_card = random.choice(self.cards)
                available_cards = self.cards
                available_cards = sorted(available_cards, key=lambda x: x[0])
                true_card = available_cards[0]
            else:
                true_card = available_cards[0]
                called_card = true_card       
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

class Pusher_Nervous(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        card_counts = {item[0]: sum(1 for tup in self.cards if tup[0] == item[0]) for item in self.cards}
        cheat = False
        for key in card_counts:
            if card_counts[key] == 1:
                cheat = True
                break
        if cheat:
            called_card = random.choice(self.cards)
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
        else:
            available_cards = []
            for card in self.cards:
                if declared_card is None or card[0]>=declared_card[0]:
                    available_cards.append(card)
            available_cards = sorted(available_cards, key=lambda x: x[0])    
            if len(available_cards) == 0:
                called_card = random.choice(self.cards)
                available_cards = self.cards
                available_cards = sorted(available_cards, key=lambda x: x[0])
                true_card = available_cards[0]
            else:
                true_card = available_cards[0]
                called_card = true_card       
        if declared_card is not None and called_card[0] < declared_card[0]:
            called_card = (min(declared_card[0]+1,14), called_card[1])
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        available_cards = sorted(self.cards, key=lambda x: x[0])
        if available_cards[-1][0] < opponent_declaration[0]:
            return True
        return False
    
class Pusher_Collector(Player):
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        card_counts = {item[0]: sum(1 for tup in self.cards if tup[0] == item[0]) for item in self.cards}
        cheat = False
        for key in card_counts:
            if card_counts[key] == 1:
                cheat = True
                break
        if cheat:
            called_card = random.choice(self.cards)
            available_cards = self.cards
            available_cards = sorted(available_cards, key=lambda x: x[0])
            true_card = available_cards[0]
        else:
            available_cards = []
            for card in self.cards:
                if declared_card is None or card[0]>=declared_card[0]:
                    available_cards.append(card)
            available_cards = sorted(available_cards, key=lambda x: x[0])    
            if len(available_cards) == 0:
                called_card = random.choice(self.cards)
                available_cards = self.cards
                available_cards = sorted(available_cards, key=lambda x: x[0])
                true_card = available_cards[0]
            else:
                true_card = available_cards[0]
                called_card = true_card       
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
    
class Saint_Sceptic_Adaptable_Naive(Player):
    def __init__(self, name):
        super().__init__(name)
        self.prob_threshold = 0.75
        self.game_started = True
        self.opponents_cards = None
        self.heap = None
        self.last_played = None
        self.I_played_first = None
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            self.last_played = None
            return "draw"
        
        if self.game_started:
            self.game_started = False
            num_repeats = len(self.cards)
            if declared_card is not None:
                num_repeats -= 1
                self.I_played_first = False
            else:
                self.I_played_first = True 
            self.opponents_cards = ["Uknown" for i in range(num_repeats)]
            self.heap = ["Uknown" for i in range(24 - num_repeats - len(self.cards))]

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
        self.last_played = true_card
        return true_card, called_card
    
    def get_probs(self, opponent_declaration):
        if opponent_declaration in self.cards:
            return 1.0
        else:
            all_cards = [(number, color) for color in range(4) for number in range(9, 15)]
            fullfilled_condition_cards = []
            not_fullfilled = []
            for card in all_cards:
                if card not in self.cards:
                    if card[0]>= opponent_declaration[0]:
                        fullfilled_condition_cards.append(card)
                    else:
                        not_fullfilled.append(card)
            predicted_prob = 1.0
            for i in range(len(self.cards)):
                predicted_prob *= len(not_fullfilled)/(len(not_fullfilled) + len(fullfilled_condition_cards))
            return 1.0 - predicted_prob
        
    def checkCard(self, opponent_declaration):
        probability_cheating = self.get_probs(opponent_declaration)
        if probability_cheating > self.prob_threshold:
            return True
        return False
        
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log = True):
        if iChecked and iDrewCards:
            self.prob_threshold *= 2
            if self.prob_threshold>1:
                self.prob_threshold = 1.0
        elif iChecked and not iDrewCards:
            self.prob_threshold /= 2

class Saint_Sceptic_75_Naive(Player):
    def __init__(self, name):
        super().__init__(name)
        self.prob_threshold = 0.75
        self.game_started = True
        self.opponents_cards = None
        self.heap = None
        self.last_played = None
        self.I_played_first = None
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            self.last_played = None
            return "draw"
        
        if self.game_started:
            self.game_started = False
            num_repeats = len(self.cards)
            if declared_card is not None:
                num_repeats -= 1
                self.I_played_first = False
            else:
                self.I_played_first = True 
            self.opponents_cards = ["Uknown" for i in range(num_repeats)]
            self.heap = ["Uknown" for i in range(24 - num_repeats - len(self.cards))]

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
        self.last_played = true_card
        return true_card, called_card
    
    def get_probs(self, opponent_declaration):
        if opponent_declaration in self.cards:
            return 1.0
        else:
            all_cards = [(number, color) for color in range(4) for number in range(9, 15)]
            fullfilled_condition_cards = []
            not_fullfilled = []
            for card in all_cards:
                if card not in self.cards:
                    if card[0]>= opponent_declaration[0]:
                        fullfilled_condition_cards.append(card)
                    else:
                        not_fullfilled.append(card)
            predicted_prob = 1.0
            for i in range(len(self.cards)):
                predicted_prob *= len(not_fullfilled)/(len(not_fullfilled) + len(fullfilled_condition_cards))
            return 1.0 - predicted_prob
        
    def checkCard(self, opponent_declaration):
        probability_cheating = self.get_probs(opponent_declaration)
        if probability_cheating > self.prob_threshold:
            return True
        return False
        
class Saint_Sceptic_50_Naive(Player):
    def __init__(self, name):
        super().__init__(name)
        self.prob_threshold = 0.5
        self.game_started = True
        self.opponents_cards = None
        self.heap = None
        self.last_played = None
        self.I_played_first = None
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            self.last_played = None
            return "draw"
        
        if self.game_started:
            self.game_started = False
            num_repeats = len(self.cards)
            if declared_card is not None:
                num_repeats -= 1
                self.I_played_first = False
            else:
                self.I_played_first = True 
            self.opponents_cards = ["Uknown" for i in range(num_repeats)]
            self.heap = ["Uknown" for i in range(24 - num_repeats - len(self.cards))]

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
        self.last_played = true_card
        return true_card, called_card
    
    def get_probs(self, opponent_declaration):
        if opponent_declaration in self.cards:
            return 1.0
        else:
            all_cards = [(number, color) for color in range(4) for number in range(9, 15)]
            fullfilled_condition_cards = []
            not_fullfilled = []
            for card in all_cards:
                if card not in self.cards:
                    if card[0]>= opponent_declaration[0]:
                        fullfilled_condition_cards.append(card)
                    else:
                        not_fullfilled.append(card)
            predicted_prob = 1.0
            for i in range(len(self.cards)):
                predicted_prob *= len(not_fullfilled)/(len(not_fullfilled) + len(fullfilled_condition_cards))
            return 1.0 - predicted_prob
        
    def checkCard(self, opponent_declaration):
        probability_cheating = self.get_probs(opponent_declaration)
        if probability_cheating > self.prob_threshold:
            return True
        return False
        
class Saint_Sceptic_25_Naive(Player):
    def __init__(self, name):
        super().__init__(name)
        self.prob_threshold = 0.25
        self.game_started = True
        self.opponents_cards = None
        self.heap = None
        self.last_played = None
        self.I_played_first = None
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            self.last_played = None
            return "draw"
        
        if self.game_started:
            self.game_started = False
            num_repeats = len(self.cards)
            if declared_card is not None:
                num_repeats -= 1
                self.I_played_first = False
            else:
                self.I_played_first = True 
            self.opponents_cards = ["Uknown" for i in range(num_repeats)]
            self.heap = ["Uknown" for i in range(24 - num_repeats - len(self.cards))]

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
        self.last_played = true_card
        return true_card, called_card
    
    def get_probs(self, opponent_declaration):
        if opponent_declaration in self.cards:
            return 1.0
        else:
            all_cards = [(number, color) for color in range(4) for number in range(9, 15)]
            fullfilled_condition_cards = []
            not_fullfilled = []
            for card in all_cards:
                if card not in self.cards:
                    if card[0]>= opponent_declaration[0]:
                        fullfilled_condition_cards.append(card)
                    else:
                        not_fullfilled.append(card)
            predicted_prob = 1.0
            for i in range(len(self.cards)):
                predicted_prob *= len(not_fullfilled)/(len(not_fullfilled) + len(fullfilled_condition_cards))
            return 1.0 - predicted_prob
        
    def checkCard(self, opponent_declaration):
        probability_cheating = self.get_probs(opponent_declaration)
        if probability_cheating > self.prob_threshold:
            return True
        return False
        
class Saint_Nervous_ver_2(Player):
    
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
        if (available_cards[-1][0] < opponent_declaration[0]) or (opponent_declaration in self.cards):
            return True
        return False
    
class Saint_Nervous_ver_3(Player):
    def __init__(self, name):
        super().__init__(name)
        self.played_cards = []
    
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
            cards_to_call = self.played_cards
            cards_to_call = sorted(cards_to_call, key=lambda x: x[0])
            called_card = None
            for card in cards_to_call:
                if card[0] >= declared_card[0]:
                    called_card = card
                    break
            if called_card is None:
                called_card = (14, np.random.randint(0, 4))
        self.played_cards.append(true_card)
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        available_cards = sorted(self.cards, key=lambda x: x[0])
        if (available_cards[-1][0] < opponent_declaration[0]) or (opponent_declaration in self.cards):
            return True
        return False
    
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log = True):
        if revealedCard is not None:
            self.played_cards.append(revealedCard)

class Saint_Nervous_Memory(Player):
    def __init__(self, name):
        super().__init__(name)
        self.memory = deque(maxlen=3)
        self.played_cards = []
    
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
            cards_to_call = self.played_cards
            cards_to_call = sorted(cards_to_call, key=lambda x: x[0])
            called_card = None
            for card in cards_to_call:
                if card[0] >= declared_card[0]:
                    called_card = card
                    break
            if called_card is None:
                called_card = (14, np.random.randint(0, 4))
        self.played_cards.append(true_card)
        self.memory.append(true_card)
        return true_card, called_card
    
    def checkCard(self, opponent_declaration):
        available_cards = sorted(self.cards, key=lambda x: x[0])
        if (available_cards[-1][0] < opponent_declaration[0]) or (opponent_declaration in self.cards) or (opponent_declaration in self.memory):
            return True
        return False
    
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log = True):
        if revealedCard is not None:
            self.played_cards.append(revealedCard)
            self.memory.append(revealedCard)
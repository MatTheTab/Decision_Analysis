import numpy as np
from player import Player
import random

class Krzysztof_Player(Player):
    def __init__(self, name):
        super().__init__(name)
        self.check_probabilities = [1, 0]
        self.cheat_probabilities = [0, 1]
        
    
    ### player's random strategy
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"

        #decide whether to cheat
        if_cheat = np.random.choice([True, False], p=self.cheat_probabilities)

        possible_cards = [x for x in self.cards if x[0] >= declared_card[0]] if declared_card is not None else self.cards

        #don't cheat when no card on the table
        if declared_card is None:
            if_cheat = False

        #if no possible cards we must cheat
        if len(possible_cards) == 0:
            if_cheat = True

        ind = np.argmin(self.cards, axis=0)[0]
        if if_cheat:
            self.pile_model.append(self.cards[ind])
            
            return (self.cards[ind], (declared_card[0], (declared_card[1]+1)%4))
        
        #if not cheating choose the smallest possible card
        ind = np.argmin(possible_cards, axis=0)[0]
        chosen_card = possible_cards[ind]

        self.pile_model.append(chosen_card)
        return chosen_card, chosen_card
    
    ### randomly decides whether to check or not
    def checkCard(self, opponent_declaration):
        #action invoked after the opponent added a card to a pile
        self.pile_model.append('unknown')
        self.opponents_card_no -= 1

        self.opponents_possible_cards = self.opponents_possible_cards - set(self.cards)
        if opponent_declaration not in self.opponents_possible_cards:
            return True
        
        return np.random.choice([True, False], p=self.check_probabilities)
    
    def startGame(self, cards):
        super().startGame(cards)
        self.opponents_possible_cards = {(number, color) for color in range(4) for number in range(9, 15)} - set(self.cards)
        self.cards_in_game = set(self.cards)
        self.pile_model = []
        self.opponents_card_no = 8


    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):
        super().getCheckFeedback(checked, iChecked, iDrewCards, revealedCard, noTakenCards, log)
        if checked:
            if iChecked and iDrewCards:
                self.pile_model = self.pile_model[:-noTakenCards]
                
            if not iChecked and iDrewCards:
                self.pile_model = self.pile_model[:-noTakenCards]

            if not iDrewCards:
                #opponent drew 3 cards
                self.opponents_card_no += 3

                #gets to know the card from the top
                if iChecked:
                    self.pile_model[-1] = revealedCard
                    self.cards_in_game.add(revealedCard)
                
                #if all cards are known exclude the rest from the consideration 
                if len(self.cards_in_game) == 16:
                    self.opponents_possible_cards = self.opponents_possible_cards & self.cards_in_game
                
                #adds 3 cards from the top to the opponents possible cards
                for _ in range(noTakenCards):
                    card = self.pile_model.pop()
                    if card != 'unknown':
                        self.opponents_possible_cards.add(card)
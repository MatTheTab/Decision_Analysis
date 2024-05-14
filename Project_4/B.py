from player import Player
import numpy as np
import random

# Blayer 1 ------------------------------------------------------------------------------------------:
'''
- Never cheats
- Calls cheat if:
    = enemy is playing a card that is certainly in their hand (not always correct)
    = enemy is playing a card that is a certain card possibly in the pile (not always correct)
    = enemy is playing a card that is a certainly in our hand
- Plays the worst possible card always
- Draws if no acceptable card
'''
class Blayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.cards = None
        
        self.opponent_declarations = []

        self.num_opponent_cards = None
        
        self.pile_cards = []
        self.certain_pile_cards = set([])
        self.certain_opponent_cards = set([])
        self.certain_game_cards = set([])

        self.count_our_cheat_detected = 0
        self.count_our_cheat_not_detected = 0

        self.count_opponent_cheated = 0
        self.count_opponent_told_truth = 0
        self.count_game_moves = 0

        self.game_turn = None # 0 if ours, 1 if theirs
        self.lied = False
       
    def select_fake_card(self, declared_card):
        card = None

        for value in range(declared_card[0], 15):
            for color in range(4):
                card = (value, color)
                if (card is not None) and (card not in self.certain_pile_cards) and (card not in self.certain_opponent_cards) and (card != declared_card):
                    return card

        return (declared_card[0], random.randint(0, 3))

    def putCard(self, declared_card):       
        if self.game_turn is None:
            self.game_turn = 0

        lie = False
        our_true_card = None
        our_declared_card = None

        # No declared card, play worst true card
        if declared_card is None:
            our_true_card = min(self.cards, key=lambda x: x[0])
            our_declared_card = our_true_card

            self.pile_cards.append(our_true_card)
            self.certain_pile_cards.add(our_true_card)
            return our_true_card, our_declared_card
        
        # On last card draw - cannot cheat
        if len(self.cards) == 1 and (self.cards[0][0] < declared_card[0]):
            return "draw"

        # If lie, always play worst card, declare a sensible card
        if lie:
            our_true_card = min(self.cards, key=lambda x: x[0])
            our_declared_card = self.select_fake_card(declared_card)
            self.lied = True
        else:
            # Play worst possible acceptable card 
            # TODO: unless we know opponent has no better card then take the worst best card and call cheat if they dont draw?
            acceptable_cards = [card for card in self.cards if card[0] >= declared_card[0]]
            if len(acceptable_cards) > 0:
                our_true_card = min(acceptable_cards, key=lambda x: x[0])
                our_declared_card = our_true_card
                self.lied = False

            # No acceptable card - draw
            else:
                return "draw"

        self.pile_cards.append(our_true_card)
        self.certain_pile_cards.add(our_true_card)
        return our_true_card, our_declared_card
    
    def checkCard(self, opponent_declaration):
        cheat = False
        # Call cheat if we possess declared card or card is certainly in pile
        if (opponent_declaration in self.cards) or (opponent_declaration in self.certain_pile_cards):
            # if (opponent_declaration in self.cards):
                # print("Call, in our cards")
            # if (opponent_declaration in self.certain_pile_cards):
                # print("Call, in pile")
                
            cheat = True
        
        # Call cheat with probability increasing with the value of declared card, increasing with the cheating consistency of opponent (anti always cheat strategy), decreasing with no cheats

        self.pile_cards.append(opponent_declaration)
        if opponent_declaration in self.certain_opponent_cards:
            self.certain_opponent_cards.remove(opponent_declaration)
            self.certain_pile_cards.add(opponent_declaration)
        
        return cheat

    
    ### -- checked = TRUE -> someone checked. If FALSE, the remaining inputs do not play any role
    ### -- iChecked = TRUE -> I decided to check my opponent (so it was my turn); 
    ###               FALSE -> my opponent checked and it was his turn
    ### -- iDrewCards = TRUE -> I drew cards (so I checked but was wrong or my opponent checked and was right); 
    ###                 FALSE -> otherwise
    ### -- revealedCard - some card (X, Y). Only if I checked.
    ### -- noTakenCards - number of taken cards
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):
        self.count_game_moves += 1

        if self.game_turn is None:
            self.game_turn = 1

        if log: print("Feedback = " + self.name + " : checked this turn = " + str(checked) +
              "; I checked = " + str(iChecked) + "; I drew cards = " + 
                      str(iDrewCards) + "; revealed card = " + 
                      str(revealedCard) + "; number of taken cards = " + str(noTakenCards))
        
        # Opponent cheat detected
        if (checked and iChecked and not iDrewCards):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
                    self.certain_opponent_cards.add(c)
            
            self.certain_opponent_cards.add(revealedCard)

            # print("ADD", noTakenCards)
            self.num_opponent_cards += noTakenCards -1
            self.count_opponent_cheated += 1

        # Opponent didnt cheat, we called
        if (checked and iChecked and iDrewCards):
            self.count_opponent_told_truth = 1
            # print("Remove", 1)
            self.num_opponent_cards -= 1

            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
                
        # We didn't cheat, opponent called
        if (checked and not iChecked and not iDrewCards):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
                    self.certain_opponent_cards.add(c)
            
            self.certain_opponent_cards.add(revealedCard)

            # print("ADD", noTakenCards)
            self.num_opponent_cards += noTakenCards
            self.count_opponent_cheated += 1

        # Our cheat detected
        if (checked and not iChecked and iDrewCards):
            self.count_our_cheat_detected += 1
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)

        # Our cheat not caught
        if (self.lied and self.game_turn == 0 and not checked):
            self.count_our_cheat_not_detected += 1

        # We drew cards
        if (iDrewCards and not checked):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
            
        # Opponent drew cards
        if (not checked and not iDrewCards and noTakenCards is not None):
            self.num_opponent_cards += noTakenCards
            # print("ADD", noTakenCards)
            
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
                    self.certain_opponent_cards.add(c)

        # print("OPP HAND SIZE", self.num_opponent_cards)

        # No call, opponent played
        if (not checked and noTakenCards is None and self.game_turn == 1):
            # print("Remove", 1)
            self.num_opponent_cards -= 1

        self.game_turn = 1 - self.game_turn

    
    ### -------------------------------------------------------------
    
    ### Init player's hand
    def startGame(self, cards):
        self.cards = cards
        self.num_opponent_cards = len(cards)
        for card in cards: self.certain_game_cards.add(card)
    
    ### Add some cards to player's hand (if (s)he checked opponent's move, but (s)he was wrong)
    def takeCards(self, cards_to_take):
        self.cards = self.cards + cards_to_take

# PLAYER 2 - Never certain of enemy version -----------------------------------------------------------------------------------------
'''
- Never cheats
- Calls cheat if:
    = enemy is playing a card that is a certain card in the pile (played by us)
    = enemy is playing a card that is a certainly in our hand
- Plays the worst possible card always
- Draws if no acceptable card
'''
class Blayer2(Blayer):    
    def checkCard(self, opponent_declaration):
        cheat = False
        # Call cheat if we possess declared card or card is certainly in pile
        if (opponent_declaration in self.cards) or (opponent_declaration in self.certain_pile_cards):
            # if (opponent_declaration in self.cards):
                # print("Call, in our cards")
            # if (opponent_declaration in self.certain_pile_cards):
                # print("Call, in pile")
                
            cheat = True
        
        # Call cheat with probability increasing with the value of declared card, increasing with the cheating consistency of opponent (anti always cheat strategy), decreasing with no cheats

        self.pile_cards.append(opponent_declaration)        
        return cheat
    
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):
        self.count_game_moves += 1

        if self.game_turn is None:
            self.game_turn = 1

        if log: print("Feedback = " + self.name + " : checked this turn = " + str(checked) +
              "; I checked = " + str(iChecked) + "; I drew cards = " + 
                      str(iDrewCards) + "; revealed card = " + 
                      str(revealedCard) + "; number of taken cards = " + str(noTakenCards))
        
        # Opponent cheat detected
        if (checked and iChecked and not iDrewCards):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)

            # print("ADD", noTakenCards)
            self.num_opponent_cards += noTakenCards -1
            self.count_opponent_cheated += 1

        # Opponent didnt cheat, we called
        if (checked and iChecked and iDrewCards):
            self.count_opponent_told_truth = 1
            # print("Remove", 1)
            self.num_opponent_cards -= 1

            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
                
        # We didn't cheat, opponent called
        if (checked and not iChecked and not iDrewCards):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
            
            # print("ADD", noTakenCards)
            self.num_opponent_cards += noTakenCards
            self.count_opponent_cheated += 1

        # Our cheat detected
        if (checked and not iChecked and iDrewCards):
            self.count_our_cheat_detected += 1
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)

        # Our cheat not caught
        if (self.lied and self.game_turn == 0 and not checked):
            self.count_our_cheat_not_detected += 1

        # We drew cards
        if (iDrewCards and not checked):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
            
        # Opponent drew cards
        if (not checked and not iDrewCards and noTakenCards is not None):
            self.num_opponent_cards += noTakenCards
            # print("ADD", noTakenCards)
            
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)

        # print("OPP HAND SIZE", self.num_opponent_cards)

        # No call, opponent played
        if (not checked and noTakenCards is None and self.game_turn == 1):
            # print("Remove", 1)
            self.num_opponent_cards -= 1

        self.game_turn = 1 - self.game_turn

# Blayer 3 ------------------------------------------------------------------------------------------:
'''
- Never cheats
- Calls cheat if:
    = enemy is playing a card that is certainly in their hand (not always correct)
    = enemy is playing a card that is a certain card possibly in the pile (not always correct)
    = enemy is playing a card that is a certainly in our hand
- Plays the card that is better the less cards the opponent has, doesnt play aces until the end
- Draws if no acceptable card
'''
class Blayer3(Blayer):
    def putCard(self, declared_card):       
        if self.game_turn is None:
            self.game_turn = 0

        lie = False
        our_true_card = None
        our_declared_card = None

        # No declared card, play worst true card
        if declared_card is None:
            our_true_card = min(self.cards, key=lambda x: x[0])
            our_declared_card = our_true_card

            self.pile_cards.append(our_true_card)
            self.certain_pile_cards.add(our_true_card)
            return our_true_card, our_declared_card
        
        # On last card draw - cannot cheat
        if len(self.cards) == 1 and (self.cards[0][0] < declared_card[0]):
            return "draw"

        # Play worst possible acceptable card that is not our best card, unless we can win with the cards
        acceptable_cards = [card for card in self.cards if card[0] >= declared_card[0]]
        if len(acceptable_cards) > 0:
            best_card = max(acceptable_cards, key=lambda x: x[0])
            all_best_cards = [card for card in acceptable_cards if card[0] == best_card[0]]
            non_best_cards = [card for card in acceptable_cards if card[0] != best_card[0]]

            if len(all_best_cards) == len(self.cards):
                our_true_card = best_card
                our_declared_card = our_true_card
                self.lied = False

            elif len(non_best_cards) > 0:
                our_true_card = min(non_best_cards, key=lambda x: x[0])
                our_declared_card = our_true_card
                self.lied = False

            else:
                lie=True

        # No acceptable card - lie
        else:
            lie = True
            self.lied = True
            
        # If lie, always play worst card, declare a sensible card
        if lie:
            our_true_card = min(self.cards, key=lambda x: x[0])
            our_declared_card = self.select_fake_card(declared_card)
            self.lied = True

        self.pile_cards.append(our_true_card)
        self.certain_pile_cards.add(our_true_card)
        return our_true_card, our_declared_card
    

# Saint_Nervous_ver_B ------------------------------------------------------------------------------------------:
class Saint_Nervous_ver_B(Player):
    def __init__(self, name):
        super().__init__(name)
        self.cards = None
        
        self.opponent_declarations = []

        self.num_opponent_cards = None
        
        self.pile_cards = []
        self.certain_pile_cards = set([])
        self.certain_opponent_cards = set([])
        self.certain_game_cards = set([])

        self.count_our_cheat_detected = 0
        self.count_our_cheat_not_detected = 0

        self.count_opponent_cheated = 0
        self.count_opponent_told_truth = 0
        self.count_game_moves = 0

        self.game_turn = None # 0 if ours, 1 if theirs
        self.lied = False
       
    def select_fake_card(self, declared_card):
        card = None

        for value in range(declared_card[0], 15):
            for color in range(4):
                card = (value, color)
                if (card is not None) and (card not in self.certain_pile_cards) and (card not in self.certain_opponent_cards) and (card != declared_card):
                    return card

        return (declared_card[0], random.randint(0, 3))

    def putCard(self, declared_card):       
        if self.game_turn is None:
            self.game_turn = 0

        lie = False
        our_true_card = None
        our_declared_card = None

        # No declared card, play worst true card
        if declared_card is None:
            our_true_card = min(self.cards, key=lambda x: x[0])
            our_declared_card = our_true_card

            self.pile_cards.append(our_true_card)
            self.certain_pile_cards.add(our_true_card)
            return our_true_card, our_declared_card
        
        # On last card draw - cannot cheat
        if len(self.cards) == 1 and (self.cards[0][0] < declared_card[0]):
            return "draw"

        # Play worst possible acceptable card
        acceptable_cards = [card for card in self.cards if card[0] >= declared_card[0]]
        if len(acceptable_cards) > 0:
            our_true_card = min(acceptable_cards, key=lambda x: x[0])
            our_declared_card = our_true_card
            self.lied = False

        # No acceptable card - lie
        else:
            lie = True
            
        # If lie, always play worst card, declare a sensible card
        if lie:
            our_true_card = min(self.cards, key=lambda x: x[0])
            our_declared_card = self.select_fake_card(declared_card)
            self.lied = True

        self.pile_cards.append(our_true_card)
        self.certain_pile_cards.add(our_true_card)
        return our_true_card, our_declared_card
    
    
    def checkCard(self, opponent_declaration):
        cheat = False
        # Call cheat if we possess declared card or card is certainly in pile
        if (max(self.cards, key=lambda x: x[0])[0] < opponent_declaration[0]) or (opponent_declaration in self.cards) or (opponent_declaration in self.certain_pile_cards):                
            cheat = True
        
        self.pile_cards.append(opponent_declaration)
        if opponent_declaration in self.certain_opponent_cards:
            self.certain_opponent_cards.remove(opponent_declaration)
            self.certain_pile_cards.add(opponent_declaration)
        
        return cheat

    
    ### -- checked = TRUE -> someone checked. If FALSE, the remaining inputs do not play any role
    ### -- iChecked = TRUE -> I decided to check my opponent (so it was my turn); 
    ###               FALSE -> my opponent checked and it was his turn
    ### -- iDrewCards = TRUE -> I drew cards (so I checked but was wrong or my opponent checked and was right); 
    ###                 FALSE -> otherwise
    ### -- revealedCard - some card (X, Y). Only if I checked.
    ### -- noTakenCards - number of taken cards
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):
        self.count_game_moves += 1

        if self.game_turn is None:
            self.game_turn = 1

        if log: print("Feedback = " + self.name + " : checked this turn = " + str(checked) +
              "; I checked = " + str(iChecked) + "; I drew cards = " + 
                      str(iDrewCards) + "; revealed card = " + 
                      str(revealedCard) + "; number of taken cards = " + str(noTakenCards))
        
        # Opponent cheat detected
        if (checked and iChecked and not iDrewCards):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
                    self.certain_opponent_cards.add(c)
            
            self.certain_opponent_cards.add(revealedCard)

            # print("ADD", noTakenCards)
            self.num_opponent_cards += noTakenCards -1
            self.count_opponent_cheated += 1

        # Opponent didnt cheat, we called
        if (checked and iChecked and iDrewCards):
            self.count_opponent_told_truth = 1
            # print("Remove", 1)
            self.num_opponent_cards -= 1

            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
                
        # We didn't cheat, opponent called
        if (checked and not iChecked and not iDrewCards):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
                    self.certain_opponent_cards.add(c)
            
            self.certain_opponent_cards.add(revealedCard)

            # print("ADD", noTakenCards)
            self.num_opponent_cards += noTakenCards
            self.count_opponent_cheated += 1

        # Our cheat detected
        if (checked and not iChecked and iDrewCards):
            self.count_our_cheat_detected += 1
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)

        # Our cheat not caught
        if (self.lied and self.game_turn == 0 and not checked):
            self.count_our_cheat_not_detected += 1

        # We drew cards
        if (iDrewCards and not checked):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
            
        # Opponent drew cards
        if (not checked and not iDrewCards and noTakenCards is not None):
            self.num_opponent_cards += noTakenCards
            # print("ADD", noTakenCards)
            
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
                    self.certain_opponent_cards.add(c)

        # print("OPP HAND SIZE", self.num_opponent_cards)

        # No call, opponent played
        if (not checked and noTakenCards is None and self.game_turn == 1):
            # print("Remove", 1)
            self.num_opponent_cards -= 1

        self.game_turn = 1 - self.game_turn

    
    ### -------------------------------------------------------------
    
    ### Init player's hand
    def startGame(self, cards):
        self.cards = cards
        self.num_opponent_cards = len(cards)
        for card in cards: self.certain_game_cards.add(card)
    
    ### Add some cards to player's hand (if (s)he checked opponent's move, but (s)he was wrong)
    def takeCards(self, cards_to_take):
        self.cards = self.cards + cards_to_take

# Saint_Nervous_ver_B2 ------------------------------------------------------------------------------------------:
class Saint_Nervous_ver_B2(Saint_Nervous_ver_B):
    def checkCard(self, opponent_declaration):
        cheat = False
        # Call cheat if we possess declared card or card is certainly in pile
        if (max(self.cards, key=lambda x: x[0])[0] < opponent_declaration[0]) or (opponent_declaration in self.cards) or (opponent_declaration in self.certain_pile_cards):                
            cheat = True
        
        self.pile_cards.append(opponent_declaration)
        
        return cheat

    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):
        self.count_game_moves += 1

        if self.game_turn is None:
            self.game_turn = 1

        if log: print("Feedback = " + self.name + " : checked this turn = " + str(checked) +
              "; I checked = " + str(iChecked) + "; I drew cards = " + 
                      str(iDrewCards) + "; revealed card = " + 
                      str(revealedCard) + "; number of taken cards = " + str(noTakenCards))
        
        # Opponent cheat detected
        if (checked and iChecked and not iDrewCards):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)

            # print("ADD", noTakenCards)
            self.num_opponent_cards += noTakenCards -1
            self.count_opponent_cheated += 1

        # Opponent didnt cheat, we called
        if (checked and iChecked and iDrewCards):
            self.count_opponent_told_truth = 1
            # print("Remove", 1)
            self.num_opponent_cards -= 1

            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
                
        # We didn't cheat, opponent called
        if (checked and not iChecked and not iDrewCards):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
            
            # print("ADD", noTakenCards)
            self.num_opponent_cards += noTakenCards
            self.count_opponent_cheated += 1

        # Our cheat detected
        if (checked and not iChecked and iDrewCards):
            self.count_our_cheat_detected += 1
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)

        # Our cheat not caught
        if (self.lied and self.game_turn == 0 and not checked):
            self.count_our_cheat_not_detected += 1

        # We drew cards
        if (iDrewCards and not checked):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
            
        # Opponent drew cards
        if (not checked and not iDrewCards and noTakenCards is not None):
            self.num_opponent_cards += noTakenCards
            # print("ADD", noTakenCards)
            
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)

        # print("OPP HAND SIZE", self.num_opponent_cards)

        # No call, opponent played
        if (not checked and noTakenCards is None and self.game_turn == 1):
            # print("Remove", 1)
            self.num_opponent_cards -= 1

        self.game_turn = 1 - self.game_turn
    


# Saint_Nervous_ver_B2 ------------------------------------------------------------------------------------------:
class Saint_Nervous_ver_B3(Saint_Nervous_ver_B):
    def putCard(self, declared_card):       
        if self.game_turn is None:
            self.game_turn = 0

        lie = False
        our_true_card = None
        our_declared_card = None

        # No declared card, play worst true card
        if declared_card is None:
            our_true_card = min(self.cards, key=lambda x: x[0])
            our_declared_card = our_true_card

            self.pile_cards.append(our_true_card)
            self.certain_pile_cards.add(our_true_card)
            return our_true_card, our_declared_card
        
        # On last card draw - cannot cheat
        if len(self.cards) == 1 and (self.cards[0][0] < declared_card[0]):
            return "draw"

        # Play worst possible acceptable card that is not our best card, unless we can win with the cards
        acceptable_cards = [card for card in self.cards if card[0] >= declared_card[0]]
        if len(acceptable_cards) > 0:
            best_card = max(acceptable_cards, key=lambda x: x[0])
            all_best_cards = [card for card in acceptable_cards if card[0] == best_card[0]]
            non_best_cards = [card for card in acceptable_cards if card[0] != best_card[0]]

            if len(all_best_cards) == len(self.cards):
                our_true_card = best_card
                our_declared_card = our_true_card
                self.lied = False

            elif len(non_best_cards) > 0:
                our_true_card = min(non_best_cards, key=lambda x: x[0])
                our_declared_card = our_true_card
                self.lied = False

            else:
                lie=True

        # No acceptable card - lie
        else:
            lie = True
            self.lied = True
            
        # If lie, always play worst card, declare a sensible card
        if lie:
            our_true_card = min(self.cards, key=lambda x: x[0])
            our_declared_card = self.select_fake_card(declared_card)
            self.lied = True

        self.pile_cards.append(our_true_card)
        self.certain_pile_cards.add(our_true_card)
        return our_true_card, our_declared_card
    
    
# Saint_Nervous_ver_B2 ------------------------------------------------------------------------------------------:
class Saint_Nervous_ver_B4(Saint_Nervous_ver_B3): 
    def putCard(self, declared_card):       
        if self.game_turn is None:
            self.game_turn = 0

        lie = False
        our_true_card = None
        our_declared_card = None

        # No declared card, play worst true card
        if declared_card is None:
            our_true_card = min(self.cards, key=lambda x: x[0])
            our_declared_card = our_true_card

            self.pile_cards.append(our_true_card)
            self.certain_pile_cards.add(our_true_card)
            return our_true_card, our_declared_card
        
        # On last card draw - cannot cheat
        if len(self.cards) == 1 and (self.cards[0][0] < declared_card[0]):
            return "draw"

        # Play worst possible acceptable card that is not our best card, unless we can win with the cards
        acceptable_cards = [card for card in self.cards if card[0] >= declared_card[0]]
        if len(acceptable_cards) > 0:
            best_card = max(acceptable_cards, key=lambda x: x[0])
            all_best_cards = [card for card in acceptable_cards if card[0] == best_card[0]]
            non_best_cards = [card for card in acceptable_cards if card[0] != best_card[0]]

            if len(all_best_cards) == len(self.cards):
                our_true_card = best_card
                our_declared_card = our_true_card
                self.lied = False

            elif len(non_best_cards) > 0:
                our_true_card = min(non_best_cards, key=lambda x: x[0])
                our_declared_card = our_true_card
                self.lied = False

            else:
                lie=True

        # No acceptable card - lie
        else:
            lie = True
            self.lied = True
            
        # If lie, always play worst card, declare a sensible card
        if lie:
            our_true_card = min(self.cards, key=lambda x: x[0])
            our_declared_card = self.select_fake_card(declared_card)
            self.lied = True

        self.pile_cards.append(our_true_card)
        self.certain_pile_cards.add(our_true_card)
        return our_true_card, our_declared_card

    def checkCard(self, opponent_declaration):
        cheat = False
        # Call cheat if we possess declared card or card is certainly in pile
        if (max(self.cards, key=lambda x: x[0])[0] < opponent_declaration[0]) or (opponent_declaration in self.cards) or (opponent_declaration in self.certain_pile_cards):                
            cheat = True
        
        self.pile_cards.append(opponent_declaration)
        
        return cheat

    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):
        self.count_game_moves += 1

        if self.game_turn is None:
            self.game_turn = 1

        if log: print("Feedback = " + self.name + " : checked this turn = " + str(checked) +
              "; I checked = " + str(iChecked) + "; I drew cards = " + 
                      str(iDrewCards) + "; revealed card = " + 
                      str(revealedCard) + "; number of taken cards = " + str(noTakenCards))
        
        # Opponent cheat detected
        if (checked and iChecked and not iDrewCards):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)

            # print("ADD", noTakenCards)
            self.num_opponent_cards += noTakenCards -1
            self.count_opponent_cheated += 1

        # Opponent didnt cheat, we called
        if (checked and iChecked and iDrewCards):
            self.count_opponent_told_truth = 1
            # print("Remove", 1)
            self.num_opponent_cards -= 1

            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
                
        # We didn't cheat, opponent called
        if (checked and not iChecked and not iDrewCards):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
            
            # print("ADD", noTakenCards)
            self.num_opponent_cards += noTakenCards
            self.count_opponent_cheated += 1

        # Our cheat detected
        if (checked and not iChecked and iDrewCards):
            self.count_our_cheat_detected += 1
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)

        # Our cheat not caught
        if (self.lied and self.game_turn == 0 and not checked):
            self.count_our_cheat_not_detected += 1

        # We drew cards
        if (iDrewCards and not checked):
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)
            
        # Opponent drew cards
        if (not checked and not iDrewCards and noTakenCards is not None):
            self.num_opponent_cards += noTakenCards
            # print("ADD", noTakenCards)
            
            toTake = self.pile_cards[-noTakenCards:]
            for c in toTake: 
                self.pile_cards.remove(c)
                if c in self.certain_pile_cards:
                    self.certain_pile_cards.remove(c)

        # print("OPP HAND SIZE", self.num_opponent_cards)

        # No call, opponent played
        if (not checked and noTakenCards is None and self.game_turn == 1):
            # print("Remove", 1)
            self.num_opponent_cards -= 1

        self.game_turn = 1 - self.game_turn
    

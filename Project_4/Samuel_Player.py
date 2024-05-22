import numpy as np
from player import Player

class Amalgamat(Player):

    def __init__(self, name):
        super().__init__(name)
        # self.opponent_cards = []
        self.declared_heap = []
        self.known_heap = []


        self.possibly_in_opponents_hand = []
        self.opponent_hand_len = 8

        self.play_if_possible = None
        self.deck = [(number, color) for color in range(4) for number in range(9, 15)]
        self.last_strat = None

        self.times_cheated = 0
        self.times_caught = 0
        self.no_of_opponents_checks = 0
        self.no_of_opponents_moves = 0

    
    ### player's random strategy
    def putCard(self, declared_card):
        # shuffle so lowest card is first
        self.shuffle()

        # Last played card has to be valid
        if len(self.cards) == 1 and not self.can_play(self.cards[0], declared_card):
            return "draw"

        ### Prevent wining ###
        # if opponent has 1 card left play highset card
        if self.opponent_hand_len == 1 and self.can_play(self.cards[-1], declared_card):
            played_card = self.cards[-1]
            self.update_known_cards(played_card, played_card)
            self.last_strat = 0
            return played_card, played_card

        ### Baiting strategy ###
        # Play the card you declared when cheating earlier
        # possibly baiting the opponent to check
        if self.play_if_possible and self.can_play(self.play_if_possible, declared_card) and self.play_if_possible in self.cards:
            played_card = self.play_if_possible
            self.update_known_cards(played_card, played_card)
            self.play_if_possible = None
            self.last_strat = 2
            return played_card, played_card

        should_cheat = np.random.choice([0, 1], p=self.determine_cheating_probability())
        if should_cheat:
            ### Cheating strategy ###
            # cheat with the lowest card that is not known
            for card in self.cards:
                if card not in self.declared_heap and self.can_play(card, declared_card):
                    self.play_if_possible = card
                    played_card = self.cards[0]
                    self.update_known_cards(played_card, card)
                    self.last_strat = 3
                    self.times_cheated += 1
                    return played_card, card
        
        ### Fair play ###
        # if you don't have to cheat with your lowest card, don't cheat
        if self.can_play(self.cards[0], declared_card):
            played_card = self.cards[0]
            self.update_known_cards(played_card, played_card)
            self.last_strat = 1
            return played_card, played_card
        
        ### Cheating strategy ###
        # I know I shouldn't but maybe....
        for card in self.cards:
            if card not in self.declared_heap and self.can_play(card, declared_card):
                self.play_if_possible = card
                played_card = self.cards[0]
                self.update_known_cards(played_card, card)
                self.last_strat = 3
                self.times_cheated += 1
                return played_card, card


        ### Fair but less optimal play ### 
        # if above fails, play any card that you can legally play:
        for card in self.cards:
            if self.can_play(card, declared_card):
                self.update_known_cards(card, card)
                self.last_strat = 4
                return card, card
        
        ### Worst case scenario play ###
        # if no card can be legally played, cheat with any card that is not known.
        # if all cards are known, cheat with the allowed
        for card in self.deck:
            if self.can_play(card, declared_card) and card not in self.declared_heap:
                self.update_known_cards(self.cards[0], card)
                self.last_strat = 5
                self.times_cheated += 1
                return self.cards[0], card
            
        # if all cards are known, cheat with the allowed card that is reapeated least often
        for card in self.deck:
            if self.can_play(card, declared_card):
                self.update_known_cards(self.cards[0], card)
                self.last_strat = 6
                self.times_cheated += 1
                return self.cards[0], card
                    
    # This happens after the opponent has played a card
    def checkCard(self, opponent_declaration):

        self.no_of_opponents_moves += 1

        # if no card to check return False
        if opponent_declaration is None:
            return False

        self.opponent_hand_len -= 1
        # update known and declared heap
        self.known_heap.append("?")
        self.declared_heap.append(opponent_declaration)
        
        # check if declared card is in your hand
        if opponent_declaration in self.cards:
            return True
        # check if declared card is in known heap
        if opponent_declaration in self.known_heap:
            return True

        if len(self.known_heap)<= 3 and opponent_declaration[0] > 12 and self.opponent_hand_len > 1:
            return True
        
        ### zachachmyncony check
        if len(self.known_heap) > 1:
            last_card_i_played = self.known_heap[-2]
            if not last_card_i_played == "?":    
                # Check if there is card that is in opponents hand that is lower than the declared card
                # and it could have been played. If so, check.
                for card in self.possibly_in_opponents_hand:
                    if card[0] < opponent_declaration[0] and self.can_play(card, last_card_i_played):
                        return True
                
        if opponent_declaration in self.possibly_in_opponents_hand:
            # remove card from possibly_in_opponents_hand
            self.possibly_in_opponents_hand.remove(opponent_declaration)
            return False
        
        return False
        
    
    ### Notification sent at the end of a round
    ### One may implement this method, capture data, and use it to get extra info
    ### -- checked = TRUE -> someone checked. If FALSE, the remaining inputs do not play any role
    ### -- iChecked = TRUE -> I decided to check my opponent (so it was my turn); 
    ### FALSE -> my opponent checked and it was his turn
    ### -- iDrewCards = TRUE -> I drew cards (so I checked but was wrong or my opponent checked and was right); 
    ### FALSE -> otherwise
    ### -- revealedCard - some card (X, Y). Only if I checked.
    ### -- noTakenCards - number of taken cards
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):

        if checked and not iChecked:
            self.no_of_opponents_checks += 1
            if iDrewCards:
                self.times_caught += 1
            
        
        # Update number of cards in opponents hand 
        if not iDrewCards and noTakenCards is not None:
            self.opponent_hand_len += noTakenCards

        # # opponent drew cards
        # if noTakenCards is not None and not checked:
        # print("Someone drew cards")
        # self.known_heap = self.known_heap[:-noTakenCards]
        # self.declared_heap = self.declared_heap[:-noTakenCards]

        # Track heap and cards that could be in opponent's hand
        if checked and noTakenCards is not None:

            # track cards that are about to be removed from the heap
            removed_cards = self.known_heap[-noTakenCards:]
            removed_cards = [card for card in removed_cards if card != "?"]
            

            self.known_heap = self.known_heap[:-noTakenCards]
            self.declared_heap = self.declared_heap[:-noTakenCards]

            if revealedCard not in removed_cards and revealedCard is not None:
                removed_cards.append(revealedCard)

            if not iDrewCards:
                self.possibly_in_opponents_hand += removed_cards
        
                        
    def shuffle(self):
        # shuffle from smallest to largest
        self.cards = sorted(self.cards, key=lambda x: x[0])
            
    def can_play(self, card, declared_card):
        if declared_card is None:
            return True
        if card[0] >= declared_card[0]:
            return True
        return False
    
    def update_known_cards(self, played_card, declared_card):
        ## TODO: This is not correct for now.
        # Update known cards based on the played card and declared card
        self.known_heap.append(played_card)
        self.declared_heap.append(declared_card)

    # Debugging function
    def last_strategy(self):
        return self.last_strat 
    
    def determine_cheating_probability(self):
        # self.times_cheated
        # self.times_caught
        # self.no_of_opponents_checks
        # self.no_of_opponents_moves
        if self.times_cheated + self.times_caught + self.no_of_opponents_checks + self.no_of_opponents_moves == 0:
            # base scenario
            return [0.7, 0.3]
        
        if self.no_of_opponents_checks == self.no_of_opponents_moves:
            # opponent checks every time, don't cheat
            return [1, 0]
        
        if self.times_cheated != 0:
            success_rate = self.times_caught / self.times_cheated
            
            # if you are successful more than 80% of the time, cheat more
            if success_rate > 0.75:
                return [0.3, 0.7]

            if success_rate <= 0.5:
                return [0.9, 0.1]

        return [1, 0]
import numpy as np
from player import Player

class Adam_player(Player):
    def __init__(self, name):
        super().__init__(name)
        self.enemy_cards=set()
        self.pile=[]
        self.game_cards=set()
        self.played=set()
    
    def putCard(self, declared_card):
    
        if declared_card is not None:
            self.pile.append(declared_card)
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            c=min(3, len(self.pile))
            self.pile=self.pile[:-c]
            return "draw"
        if declared_card is None:
            smallest_card=min(self.cards, key=lambda x:x[0])
            self.pile.append(smallest_card)
            self.played.add(smallest_card)
            return smallest_card,smallest_card 
    
        if declared_card[0]>max(self.cards, key=lambda x:x[0])[0]:
            cheat=self.get_possible(declared_card)
            smallest_card=min(self.cards, key=lambda x:x[0])
            self.pile.append(smallest_card)
            self.played.add(cheat)
            return (smallest_card, cheat)
        possible=[x for x in self.cards if x[0]>=declared_card[0]]
        smallest=min(possible, key=lambda x:x[0])
        self.pile.append(smallest)
        return smallest, smallest
        

        ### Init player's hand
    def startGame(self, cards):
        self.cards = cards
        self.game_cards=self.game_cards.union(cards)
    
    def get_possible(self, declared):
        possible=set((number, color) for color in range(4) for number in range(declared[0], 15))-self.enemy_cards-self.played
        possible.discard(declared)
        if len(possible)==0:
            possible=set((number, color) for color in range(4) for number in range(declared[0], 15))
            possible.discard(declared)
        return list(possible)[np.random.choice(len(possible))]

            
    ### randomly decides whether to check or not
    def checkCard(self, opponent_declaration):
        if opponent_declaration in self.pile:
            return True
      
        if opponent_declaration in self.cards: 
            return True
        if len(self.game_cards)==16 and opponent_declaration not in self.game_cards:
            return True
        
        
        return np.random.choice([True, False])
    
    def takeCards(self, cards_to_take):
        self.cards = self.cards + cards_to_take
        self.game_cards=self.game_cards.union(self.cards)
        self.pile=self.pile[:-len(cards_to_take)]
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):
   
        if log: print("Feedback = " + self.name + " : checked this turn = " + str(checked) +
              "; I checked = " + str(iChecked) + "; I drew cards = " + 
                      str(iDrewCards) + "; revealed card = " + 
                      str(revealedCard) + "; number of taken cards = " + str(noTakenCards))
        if revealedCard is not None:
        
            self.game_cards=self.game_cards.union([revealedCard])

        if checked and not iDrewCards:
            for x in self.pile[-noTakenCards:]:
                self.enemy_cards.add(x)
import numpy as np
from player import Player
import random
from collections import deque
from Test_Players import *
from collections import Counter
from B import *

class ensamble_player(Player):
    def __init__(self, name):
        super().__init__(name)
        self.player1 = Saint_Nervous_ver_B("player1")
        self.player2 = Saint_Nervous_ver_B2("player2")
        self.player3 = Saint_Nervous_ver_3("player3")
        self.player4 = Saint_Nervous_ver_2("player4")
    
    def startGame(self, cards):
        self.cards = cards
        self.player1.startGame(cards)
        self.player2.startGame(cards)
        self.player3.startGame(cards)
        self.player4.startGame(cards)

    def takeCards(self, cards_to_take):
        self.cards = self.cards + cards_to_take
        self.player1.takeCards(cards_to_take)
        self.player2.takeCards(cards_to_take)
        self.player3.takeCards(cards_to_take)
        self.player4.takeCards(cards_to_take)
    
    def putCard(self, declared_card):
        if len(self.cards) == 1 and declared_card is not None and self.cards[0][0] < declared_card[0]:
            return "draw"
        self.player1.cards = self.cards
        self.player2.cards = self.cards
        self.player3.cards = self.cards
        self.player4.cards = self.cards
        move1 = self.player1.putCard(declared_card)
        move2 = self.player2.putCard(declared_card)
        move3 = self.player3.putCard(declared_card)
        move4 = self.player4.putCard(declared_card)
        moves = [move1, move2, move3, move4]
        real_moves_counts = {}
        declared_moves_counts = {}
        for move in moves:
            if move[0] in real_moves_counts:
                real_moves_counts[move[0]] += 1
            else:
                real_moves_counts[move[0]] = 1
            if move[1] in declared_moves_counts:
                declared_moves_counts[move[1]] += 1
            else:
                declared_moves_counts[move[1]] = 1

        num_apperances = -1
        real_move = "draw"
        for key in real_moves_counts:
            if real_moves_counts[key] > num_apperances:
                num_apperances = real_moves_counts[key]
                real_move = key

        num_apperances = -1
        called_move = "draw"
        for key in declared_moves_counts:
            if declared_moves_counts[key] > num_apperances:
                num_apperances = declared_moves_counts[key]
                called_move = key

        return real_move, called_move


    def checkCard(self, opponent_declaration):
        check1 = self.player1.checkCard(opponent_declaration)
        check2 = self.player2.checkCard(opponent_declaration)
        check3 = self.player3.checkCard(opponent_declaration)
        check4 = self.player4.checkCard(opponent_declaration)
        checks = [check1, check2, check3, check4]
        count = Counter(checks)
        if count[True] >= count[False]:
            return True
        else:
            return False

    
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log = True):
        self.player1.getCheckFeedback(checked, iChecked, iDrewCards, revealedCard, noTakenCards, log = False)
        self.player2.getCheckFeedback(checked, iChecked, iDrewCards, revealedCard, noTakenCards, log = False)
        self.player3.getCheckFeedback(checked, iChecked, iDrewCards, revealedCard, noTakenCards, log = False)
        self.player4.getCheckFeedback(checked, iChecked, iDrewCards, revealedCard, noTakenCards, log = False)


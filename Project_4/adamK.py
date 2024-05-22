import numpy as np
from player import Player
import random


class AdamK(Player):
    """Player tries to count cards in his hand and some of cards in the pile, then it makes decision accordingly"""

    def __init__(self, name):  # only run once
        super().__init__(name)
        self._just_played = False    # auxilary variable for counting cards in pile
        self._reset_counts()

    def putCard(self, declared_card):
        self._just_played = True
        assert self.cards is not None

        legal_cards = self.cards
        if declared_card is not None:
            legal_cards = list(
                filter(lambda c: c >= declared_card, legal_cards))

        if legal_cards:
            play = min(legal_cards, key=lambda c: c[0])
            self.pile.append(play)
            return play, play

        if len(self.cards) == 1:
            return "draw"

        # cheat
        play = min(self.cards, key=lambda c: c[0])

        # declare = declared_card
        # if not self.min_cheat:
        #     frompile = None
        #     for card in self.pile:
        #         if card is not None and card[0] >= declared_card[0]:
        #             frompile = card
        #             break
        #     if frompile is not None:
        #         declare = frompile
        #     else:
        #         declare = (14, random.randint(0, 3))

        frompile = None
        for card in self.pile:
            if card is not None and card[0] >= declared_card[0]:
                frompile = card
                break
        if frompile is not None:
            declare = frompile
        else:
            declare = (14, random.randint(0, 3))

        self.pile.append(play)
        return play, declare

    def checkCard(self, opponent_declaration):
        assert self.cards is not None
        if opponent_declaration in self.cards or opponent_declaration in self.pile:
            return True

        n_his_cards = 16 - len(self.cards) - len(self.pile)

        known = filter(lambda a: a is not None, self.cards + self.pile)
        unknown = self._getDeck() - set(known)
        legal = list(
            filter(lambda c: c[0] >= opponent_declaration[0], unknown))
        nunknown = len(unknown)
        nlegal = len(legal)
        nillegal = nunknown - nlegal

        # calculate chance that opponent doesn't have the required card
        # if has more cards than illegal
        if n_his_cards > nillegal:
            return False

        prob_doesnt_have = 1
        for i in range(n_his_cards):
            x = (nillegal - i) / (nunknown - i)
            prob_doesnt_have *= x
        return random.random() < prob_doesnt_have

    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):
        assert self.cards is not None
        self.playing_set = self.playing_set | set(self.cards)

        if not checked:
            if noTakenCards is None:  # normal move
                if not self._just_played:
                    self.pile.append(None)
            else:  # drawn
                self.pile = self.pile[:-noTakenCards]
        else:  # someone checked
            if iChecked:
                if iDrewCards:
                    self.pile = self.pile[:-noTakenCards]
                else:
                    self.pile = self.pile[:-noTakenCards+1]
            else:
                if iDrewCards:
                    self.pile = self.pile[:-noTakenCards]
                else:
                    self.pile = self.pile[:-noTakenCards]

        if self._just_played:
            self.i_moved += 1
        else:
            self.he_moved += 1

        if self._just_played:
            self._just_played = False

        if self.i_moved > 100 or self.he_moved > 100:
            self._reset_counts()

        assert self.cards is not None
        if len(self.cards) == 0:
            self._reset_counts()

        his_cards = 16 - len(self.cards) - len(self.pile)
        if his_cards == 0:
            self._reset_counts()

    def _reset_counts(self):
        self.pile = []
        self.i_moved = 0
        self.he_moved = 0
        self.playing_set = set()

    def _getDeck(self):
        return set([(number, color) for color in range(4) for number in range(9, 15)])


class AdamK2(Player):
    def __init__(self, name):  # only run once
        super().__init__(name)
        self._just_played = False    # auxilary variable for counting cards in pile
        self._reset_counts()

    def putCard(self, declared_card):
        self._just_played = True
        assert self.cards is not None

        legal_cards = self.cards
        if declared_card is not None:
            legal_cards = list(
                filter(lambda c: c >= declared_card, legal_cards))

        if legal_cards:
            play = min(legal_cards, key=lambda c: c[0])
            self.pile.append(play)
            return play, play

        if len(self.cards) == 1:
            return "draw"

        # cheat
        play = min(self.cards, key=lambda c: c[0])

        declare = declared_card
        self.pile.append(play)
        return play, declare

    def checkCard(self, opponent_declaration):
        assert self.cards is not None
        if opponent_declaration in self.cards or opponent_declaration in self.pile:
            return True

        n_his_cards = 16 - len(self.cards) - len(self.pile)

        known = filter(lambda a: a is not None, self.cards + self.pile)
        unknown = self._getDeck() - set(known)
        legal = list(
            filter(lambda c: c[0] >= opponent_declaration[0], unknown))
        nunknown = len(unknown)
        nlegal = len(legal)
        nillegal = nunknown - nlegal

        # calculate chance that opponent doesn't have the required card
        # if has more cards than illegal
        if n_his_cards > nillegal:
            return False

        prob_doesnt_have = 1
        for i in range(n_his_cards):
            x = (nillegal - i) / (nunknown - i)
            prob_doesnt_have *= x
        return random.random() < prob_doesnt_have

    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):
        assert self.cards is not None
        self.playing_set = self.playing_set | set(self.cards)
        if not checked:
            if noTakenCards is None:  # normal move
                if not self._just_played:
                    self.pile.append(None)
            else:  # drawn
                self.pile = self.pile[:-noTakenCards]
        else:  # someone checked
            if iChecked:
                if iDrewCards:
                    self.pile = self.pile[:-noTakenCards]
                else:
                    self.pile = self.pile[:-noTakenCards+1]
            else:
                if iDrewCards:
                    self.pile = self.pile[:-noTakenCards]
                else:
                    self.pile = self.pile[:-noTakenCards]


        if self._just_played:
            self.i_moved += 1
        else:
            self.he_moved += 1

        if self._just_played:
            self._just_played = False

        if self.i_moved > 100 or self.he_moved > 100:
            self._reset_counts()

        assert self.cards is not None
        if len(self.cards) == 0:
            self._reset_counts()

        his_cards = 16 - len(self.cards) - len(self.pile)
        if his_cards == 0:
            self._reset_counts()

    def _reset_counts(self):
        self.pile = []
        self.i_moved = 0
        self.he_moved = 0
        self.playing_set = set()

    def _getDeck(self):
        return set([(number, color) for color in range(4) for number in range(9, 15)])
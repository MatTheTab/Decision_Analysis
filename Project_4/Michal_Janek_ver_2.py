import random
from typing import Optional

import numpy as np
from player import Player


class Card:
    def __init__(self, number, color, certain=None):
        self.number = number
        self.color = color
        self.certain = certain

    def __eq__(self, other):
        if isinstance(other, Card):
            if self.certain is None or other.certain is None:
                return self.color == other.color and self.number == other.number
            else:
                return self.color == other.color and self.number == other.number and self.certain == other.certain

        elif isinstance(other, tuple):
            if len(other) != 2:
                return False

            return self.color == other[1] and self.number == other[0]

        return False

    def __str__(self):
        return "Card: {} of {}".format(self.number, self.color)

    __repr__ = __str__


class KaminskiIndrzejczak_ver_2(Player):
    def __init__(self, name):
        super().__init__(name)
        self.pile_cards: list[Card] = []
        self.opponents_cards: list[Card] = []
        self.opponents_cards_count = 0
        self.game_cards: list[Card] = []
        self.game_cards_count = 16

    def startGame(self, cards):
        super().startGame(cards)

        self.game_cards_count = len(cards) * 2
        self.opponents_cards_count = len(cards)

        for card in cards:
            self.game_cards.append(Card(card[0], card[1], True))

    def takeCards(self, cards_to_take):
        super().takeCards(cards_to_take)

        for card in cards_to_take:
            if card not in self.game_cards:
                self.game_cards.append(Card(*card, True))

            if card in self.opponents_cards:
                self.opponents_cards.remove(card)

            if card in self.pile_cards:
                self.pile_cards.remove(card)

    ### player's random strategy
    def choose_card(self, declared_card):
        if declared_card is None:
            smallest_card = sorted(self.cards)[0]

            return smallest_card, smallest_card

        legal_cards = list(filter(lambda x: x[0] >= declared_card[0], self.cards))

        illegal_cards = list(filter(lambda x: x[0] < declared_card[0], self.cards))

        if len(legal_cards) == 0:
            if len(self.cards) == 1:
                return "draw"

            real_card = sorted(self.cards)[0]

            free_game_cards = list(
                filter(lambda x: x.number > declared_card[0] and x not in self.opponents_cards, self.game_cards))

            if len(free_game_cards) > 0:
                fake_card = random.choice(free_game_cards)
                return real_card, (fake_card.number, fake_card.color)

            colors = [0, 1, 2, 3]
            random.shuffle(colors)
            almost_safe_card = None

            for n in range(declared_card[0], 15):
                for c in colors:
                    fake_card = (n, c)

                    if almost_safe_card is not None and Card(*fake_card, True) not in self.opponents_cards and fake_card != declared_card:
                        almost_safe_card = fake_card

                    if fake_card not in self.opponents_cards and fake_card != declared_card:
                        break
                else:
                    continue

                break

            else:
                fake_card = (
                    declared_card[0],
                    list(filter(lambda x: x != declared_card[1], colors))[0]) if almost_safe_card is None \
                    else almost_safe_card

            return real_card, fake_card
            # Let's do some checking init mate?

        legal_cards = sorted(legal_cards)

        chosen_card = legal_cards[0]

        if len(illegal_cards) > 0:
            return random.choice(illegal_cards), chosen_card

        return chosen_card, chosen_card

    def putCard(self, declared_card):
        chosen_card = self.choose_card(declared_card)

        if chosen_card == 'draw':
            return chosen_card

        real_card, new_declared_card = chosen_card

        self.pile_cards.append(Card(*real_card, True))

        return real_card, new_declared_card

    ### randomly decides whether to check or not
    def checkCard(self, opponent_declaration):
        self.pile_cards.append(Card(*opponent_declaration, False))

        if opponent_declaration in self.cards:
            return True

        if Card(*opponent_declaration, True) in self.pile_cards:
            return True

        if Card(*opponent_declaration) in self.opponents_cards:
            return False



        # if len(self.game_cards) >= self.game_cards_count and Card(*opponent_declaration, True) not in self.game_cards:
        # return True
        #
        # estimated_cheating_chance = 1 - (len(self.opponents_cards) / self.opponents_cards_count)
        # if estimated_cheating_chance > 0.5:
        # return True

        return False

    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):
        super().getCheckFeedback(checked, iChecked, iDrewCards, revealedCard, noTakenCards, log)

        if revealedCard is not None and revealedCard not in self.game_cards:
            self.game_cards.append(Card(*revealedCard, True))

        if noTakenCards is None:
            return

        if (checked and not iDrewCards) or (not iDrewCards):
            self.opponents_cards_count += noTakenCards

            for _ in range(min(len(self.pile_cards), noTakenCards)):
                taken_card = self.pile_cards.pop()

                if revealedCard is not None and taken_card == revealedCard:
                    taken_card.certain = True

                if not taken_card.certain and taken_card not in self.opponents_cards:
                    self.opponents_cards.append(taken_card)
                elif taken_card.certain:
                    taken_card.certain = None

                    for opponents_card in self.opponents_cards:
                        if opponents_card.__eq__(taken_card):
                            opponents_card.certain = True
                            break
                    else:
                        taken_card.certain = True
                        self.opponents_cards.append(taken_card)
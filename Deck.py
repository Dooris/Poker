#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author Katja Karsikas

import random

from Card import Card


class Deck:
    """A representation of a deck of cards in a card game."""
    def __init__(self):
        self._suits = ["hearts", "clubs", "diamonds", "spades"]
        self._ranks = ["2", "3", "4", "5", "6", "7", "8",
                       "9", "10", "J", "Q", "K", "A"]
        self._cards = [Card(s, n) for s in self._suits for n in self._ranks]

    def deck(self):
        return self._cards

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self._cards)

    def deal(self, players, number_of_cards):
        """Deal the cards to the players.
        Add a specific number of cards to the player's hand.

        :param players: A list of players.
        :param number_of_cards: An int, the number of cards to be dealt per player.
        """
        number_of_players = len(players)
        for number in range(number_of_players*number_of_cards):
            mod = number % number_of_players
            players[mod].add_card(self._cards.pop(0))

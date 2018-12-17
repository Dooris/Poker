#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author Katja Karsikas


class Card:
    """
    A representation of a card.

    :param suit: A string, the cards's suit.
    :param rank: A string, the card's rank.
    """
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __repr__(self):
        return self.rank + " of " + self.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank_as_number() < other.rank_as_number()

    def rank_as_number(self):
        """Transform rank to integer."""
        if self._rank == "A":
            number = 14
        elif self._rank == "K":
            number = 13
        elif self._rank == "Q":
            number = 12
        elif self._rank == "J":
            number = 11
        else:
            number = self._rank
        return int(number)

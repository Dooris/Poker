#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author Katja Karsikas


class Player:
    """
    A representation of a player in a card game.

    :param name: A string, the person's name.
    """
    def __init__(self, name):
        self._name = name
        self._hand = list()

    @property
    def name(self):
        return self._name

    @property
    def hand(self):
        return self._hand

    def add_card(self, card):
        """Add a card to player's hand."""
        self._hand.append(card)

    def show_hand(self):
        """Print player's hand."""
        self.hand.sort()
        print("{}: {}".format(self.name, self.hand))

    def empty_hand(self):
        """Empty player's hand."""
        self._hand.clear()

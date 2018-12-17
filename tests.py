#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author Katja Karsikas

import unittest

import Game
from Card import Card


class TestAnalyze(unittest.TestCase):
    """
    Test cases for analyze_hand function to assert
    that it analyzes the hand of cards correctly.
    """

    def test_analysing_straight_flush(self):
        """
        Test that the analyze_hand returns "Straight flush".
        """
        hand = [Card("diamonds", "7"), Card("diamonds", "9"),
                Card("diamonds", "10"), Card("diamonds", "6"),
                Card("diamonds", "8")]
        result = Game.analyze_hand(hand)
        self.assertEqual(result, "Straight flush")

    def test_analysing_four_of_kind(self):
        """
        Test that the analyze_hand returns "Four of a kind".
        """
        hand = [Card("diamonds", "5"), Card("clubs", "5"),
                Card("hearts", "5"), Card("spades", "6"),
                Card("clubs", "5")]
        result = Game.analyze_hand(hand)
        self.assertEqual(result, "Four of a kind")

    def test_analysing_full_house(self):
        """
        Test that the analyze_hand returns "Full house".
        """
        hand = [Card("diamonds", "K"), Card("clubs", "8"),
                Card("hearts", "8"), Card("spades", "8"),
                Card("clubs", "K")]
        result = Game.analyze_hand(hand)
        self.assertEqual(result, "Full house")

    def test_analysing_royal_straight(self):
        """
        Test that the analyze_hand returns "Straight".
        """
        hand = [Card("hearts", "K"), Card("diamonds", "J"),
                Card("spades", "10"), Card("spades", "Q"),
                Card("clubs", "A")]
        result = Game.analyze_hand(hand)
        self.assertEqual(result, "Straight")

    def test_analysing_small_straight(self):
        """
        Test that the analyze_hand returns "Straight" also when ace is 1.
        """
        hand = [Card("clubs", "5"), Card("diamonds", "2"),
                Card("hearts", "4"), Card("spades", "3"),
                Card("clubs", "A")]
        result = Game.analyze_hand(hand)
        self.assertEqual(result, "Straight")

    def test_analysing_flush(self):
        """
        Test that the analyze_hand returns "Flush" if all cards has the same suit.
        """
        hand = [Card("clubs", "4"), Card("clubs", "5"),
                Card("clubs", "9"), Card("clubs", "J"),
                Card("clubs", "K")]
        result = Game.analyze_hand(hand)
        self.assertEqual(result, "Flush")

    def test_analysing_three_of_kind(self):
        """
        Test that the analyze_hand returns "Three of a kind"
        if three of the ranks has the same value.
        """
        hand = [Card("diamonds", "5"), Card("clubs", "J"),
                Card("hearts", "J"), Card("spades", "6"),
                Card("clubs", "J")]
        result = Game.analyze_hand(hand)
        self.assertEqual(result, "Three of a kind")

    def test_analysing_two_pairs(self):
        """
        Test that the analyze_hand returns "Two pairs".
        """
        hand = [Card("clubs", "7"), Card("spades", "J"),
                Card("hearts", "K"), Card("spades", "7"),
                Card("diamonds", "K")]
        result = Game.analyze_hand(hand)
        self.assertEqual(result, "Two pairs")

    def test_analysing_pair(self):
        """
        Test that the analyze_hand returns a "Pair".
        """
        hand = [Card("clubs", "Q"), Card("hearts", "J"),
                Card("diamonds", "2"), Card("spades", "Q"),
                Card("diamonds", "4")]
        result = Game.analyze_hand(hand)
        self.assertEqual(result, "Pair")

    def test_analysing_empty_hand(self):
        """
        Test that the analyze_hand returns "Nothing".
        """
        hand = [Card("clubs", "1"), Card("diamonds", "5"),
                Card("spades", "9"), Card("clubs", "10"),
                Card("clubs", "A")]
        result = Game.analyze_hand(hand)
        self.assertEqual(result, "Nothing")


if __name__ == '__main__':
    unittest.main()

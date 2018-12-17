#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author Katja Karsikas

from collections import defaultdict

from Deck import Deck
from Player import Player


def is_straight_flush(hand):
    """
    Returns true if the hand of cards contains a straight flush.

    :param hand: A list of cards.
    :return Boolean.
    """
    if is_flush(hand) and is_straight(hand):
        return True
    else:
        return False


def is_straight(hand):
    """
    Returns true if the hand of cards contains a straight.

    :param hand: A list of cards.
    :return Boolean.
    """
    values = [card.rank_as_number() for card in hand]
    value_range = max(values) - min(values)
    if len(set(item_frequency(values))) == 1 and value_range == 4:
        return True
    else:
        # Check straight with low Ace
        if set(values) == {14, 2, 3, 4, 5}:
            return True
        return False


def is_flush(hand):
    """
    Returns true if all cards in the hand has the same suit.

    :param hand: A list of cards.
    :return Boolean.
    """
    suits = [card.suit for card in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False


def is_full_house(hand):
    """
    Returns true if the hand of cards contains three of a kind and a pair.

    :param hand: A list of cards.
    :return Boolean.
    """
    values = [card.rank for card in hand]
    if item_frequency(values) == [2, 3]:
        return True
    else:
        return False


def is_four_of_kind(hand):
    """
    Returns true if the hand of cards contains four of a kind.

    :param hand: A list of cards.
    :return Boolean.
    """
    values = [card.rank for card in hand]
    if item_frequency(values) == [1, 4]:
        return True
    else:
        return False


def is_three_of_kind(hand):
    """
    Returns true if the hand of cards contains three of a kind.

    :param hand: A list of cards.
    :return Boolean.
    """
    values = [card.rank for card in hand]
    if item_frequency(values) == [1, 1, 3]:
        return True
    else:
        return False


def is_two_pairs(hand):
    """
    Returns true if the hand of cards contains two pairs.

    :param hand: A list of cards.
    :return Boolean.
    """
    values = [card.rank for card in hand]
    if item_frequency(values) == [1, 2, 2]:
        return True
    else:
        return False


def is_pair(hand):
    """
    Returns true if the hand of cards contains a pair.

    :param hand: A list of cards.
    :return Boolean.
    """
    values = [card.rank for card in hand]
    if item_frequency(values) == [1, 1, 1, 2]:
        return True
    else:
        return False


def item_frequency(values):
    """
    Get the frequency of items in a list.
    Returns a list of items' frequencies in a list in sorted order.

    :param values: A list of cards.
    :return A list of integers.
    """
    value_counts = defaultdict(lambda: 0)
    for item in values:
        value_counts[item] += 1
    return sorted(value_counts.values())


def analyze_hand(hand):
    """
    Analyze and return the content of the hand.

    :param hand: Player's hand of cards.
    :return: A string, content of the hand.
    """
    if is_straight_flush(hand):
        return "Straight flush"
    elif is_four_of_kind(hand):
        return "Four of a kind"
    elif is_full_house(hand):
        return "Full house"
    elif is_straight(hand):
        return "Straight"
    elif is_flush(hand):
        return "Flush"
    elif is_three_of_kind(hand):
        return "Three of a kind"
    elif is_two_pairs(hand):
        return "Two pairs"
    elif is_pair(hand):
        return "Pair"
    else:
        return "Nothing"


def main():
    print("Game started.")

    number_of_players = 3
    number_of_cards = 5

    # Create players.
    players = list()
    # Ask the name for each player from the user.
    for number in range(1, number_of_players + 1):
        # Create a player and add it to the list.
        player = Player("Player" + str(number))
        players.append(player)

    # Play a new game until the user wants to quit.
    while True:
        # Create and shuffle the deck.
        deck = Deck()
        deck.shuffle()

        # Deal hands to the players.
        deck.deal(players, number_of_cards)

        # Go through players' hands
        for player in players:
            # Print a player's hand.
            player.show_hand()
            # Print the hand's result.
            print(" -> ", end="")
            print(analyze_hand(player.hand))
            # Empty the player's hand.
            player.empty_hand()

        # Ask if the user wants to play again.
        answer = input("Do you want play again? (Y/N)\n")
        answer = answer.lower()
        if answer == "y" or answer == "yes" or answer == "":
            print("New game:")
            continue
        else:
            break


if __name__ == "__main__":
    main()

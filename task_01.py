#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides player pairs for the game using enumerate."""


def get_matches(players):
    """game and players.

    Args:
        players [list]: names

    return:
        list: list of tuples with two player names

    examples:
        >>>get_matches(['James', 'Jesse', 'Jennifer'])
        >>>[('James', 'Jesse'), ('James', 'Jennifer'), ('Jesse', 'Jennifer')]
    """
    newlist = []
    for index1, player1 in enumerate(players):
        for index2, player2 in enumerate(players):
            if index1 < index2:
                newlist.append((player1, player2))
    return newlist

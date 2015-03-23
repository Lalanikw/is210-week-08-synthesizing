#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides player pairs for the game using enumerate."""


def get_matches(players):
    """game.

    Args:
        players [list]: names

    return:
        list: names of the player pairs

    examples:
        >>>get_matches(['James', 'Jesse', 'Jennifer'])
        >>>(0, 'James')
            (1, 'Jesse')
            (2, 'Jennifer')

    """
    newlist = []
    list_len = len(playerlist)
    for idx, players in enumerate(players):
        innerlist = []
        st_idx = idx+1
        for i in range(st_idx, list_len):
            innerlist.append([players, playerlist[i]])
        if len(innerlist) > 0:
            newlist.append(innerlist)
    return newlist

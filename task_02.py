#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""passwards, usernames and authentication."""

import authentication
import getpass


def login(username, maxattempts=3):
    """correct password needed.

    Args:
        username (str): valid names
        maxattempts (int): optional 3

    return:
        list: pair of tuples

    examples:
        >>>login ('Mike', 3)
        >>>Please enter your password: desk
        >>>Incorrect username or password. You have 2 attempts left.
        >>>Please enter your password: chair
        >>>Incorrect username or password. You have 1 attempts left.
        >>>Please enter your password: television
        >>>Incorrect username or password. You have 0 attempts left.
        >>>False
    """
    authenticated = False
    passstr = 'Please enter your password: '
    failedstr = 'Incorrect username or password. You have {} attempts left.'
    counter = 0
    while not authenticated and counter < maxattempts:
        password = getpass.getpass(passstr)
        authenticated = authentication.authenticate(username, password)
        counter += 1
        if not authenticated:
            print failedstr.format(maxattempts - counter, maxattempts)
    return authenticated

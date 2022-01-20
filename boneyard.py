"""Models a boneyard -- a pile of dominoes"""

import random
from domino import *

def create_boneyard():
    """
    returns a pile of dominoes containing
    one copy of every possible domino
    """
    boneyard = list()
    for l in range(0,7):
        for r in range(l,7):
            bone = create_domino(l, r)
            boneyard.append(bone)
    return boneyard


def draw_from_boneyard(boneyard):
    """
    removes a random domino from the boneyard and returns it
    :return: random domino from boneyard
    """
    index = random.randint(0,len(boneyard) - 1)
    bone = boneyard.pop(index)
    return bone


def tiles_remaining(boneyard):
    """returns the number of tiles left in the yard"""
    return len(boneyard)


def boneyard_is_empty(boneyard):
    """return True if boneyard empty, False if not"""
    return len(boneyard) == 0

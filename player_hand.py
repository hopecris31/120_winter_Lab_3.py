"""Models a hand of dominoes"""
from domino import *

def create_player():
    """create an empty hand for player"""
    return []

def get_bone(player, i):
    """
    return the ith domino of the player's hand

    :param player: hand of the player
    :param i: index of card to get (0 is first card)
    :return: domino if i is valid index
    """
    return player[i]


def remove_bone_from_hand(player, i):
    """
    remove the ith domino of the player's hand and return it.

    :param player: hand of the player
    :param i: index of card to remove (0 is first card)
    :return: ith domino in player's hand if i is valid index
    """
    return player.pop(i)


def show_player(player):
    """print the given player's hand"""
    print("PLAYER HAND")
    print("-----------")
    for i in range(len(player)):
        print("%d: %s" % (i, as_str(get_bone(player, i))))


def add_bone_to_hand(player, bone):
    """
    adds the given domino to the player's hand

    :param player: the player's hand (list)
    :param bone: domino to add
    :return: None
    """
    print ("adding %s to hand" % (as_str(bone)))
    player.append(bone)

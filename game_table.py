"""models the table upon which dominoes can be played"""
from domino import *


def create_table(initial_bone):
    """
    creates a new domino table with a single starting domino

    :param initial_bone:  the starting domino
    :return new table as a list
    """
    table = []
    table.append(initial_bone)
    return table


def show_dominoes_on_table(table):
    """print the current table of dominoes"""
    print ("TABLE")
    print ("-----")
    to_show = ""
    for bone in table:
        to_show += as_str(bone) + " "
    print(to_show)


def get_left_domino(table):
    """return the domino on the left end that can be added to"""
    return table[0]


def get_right_domino(table):
    """return the domino on the right end that can be added to"""
    return table[len(table)-1]

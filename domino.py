"""Models a domino"""

def create_domino(left_pips, right_pips):
    """
    create a domino from the given integers

    :param left_pips: the left number
    :param right_pips: the right number
    :return: domino as a two-character string
    """
    return str(left_pips) + str(right_pips)


def as_str(bone):
    """return given domino as a printable string"""
    return "[%s | %s]" % (get_left(bone), get_right(bone))


def get_left(bone):
    """given a domino, return left number"""
    return bone[0]


def get_right(bone):
    """given a domino, return right number"""
    return bone[1]

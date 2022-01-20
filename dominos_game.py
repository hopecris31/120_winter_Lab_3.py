"""plays a simplified version of dominoes"""
from game_table import *
from boneyard import *
from player_hand import *


def get_play_kind():
    """asks player for move she wants to make"""
    valid = ['l', 'r', 'd']
    #ask for input
    #while user typed in something invalid
    #ask again
    #input is valid
    while move not in valid:
        move = input('move not valid, type L, R, or D')
        #move is valid
    return move


def get_bone_to_play(player):
    """
    ask user for domino she wishes to play from given hand
    :param player: hand to play from
    :return: domino to play
    """
    index = input("enter the number of the bone to play")
    return remove_bone_from_hand(player, int(index))

def display_error():
    """display error message"""
    print("ERROR, try again")


def main():
    boneyard = create_boneyard()
    player = create_player()

    initial_bone = draw_from_boneyard(boneyard)
    table = create_table(initial_bone)

    while len(boneyard)>0:
        show_dominoes_on_table(table)
        show_player(player)

        play_kind = get_play_kind()

        if play_kind == 'l':
            bone = get_bone_to_play(player)
            bone_left = bone[0]
            bone_right = bone[1]
            if bone_left == table[0][0]:
                new_domino = bone_right + bone_left
                table.insert(0,new_domino)
            elif bone_right == table[0][0]:
                table.insert(0, bone)
            else:
                display_error()
                add_bone_to_hand(player,bone)
        elif play_kind == 'r':
            bone = get_bone_to_play(player)
            bone_left = bone[0]
            bone_right = bone[1]
            if bone_left == table[len(table)-1][1]:
                table.append(bone)
            elif bone_right == table[len(table)-1][1]:
                new_domino = bone_right + bone_left
                table.append(new_domino)
            else:
                display_error()
                add_bone_to_hand(player, bone)
        elif play_kind == 'd':
            bone = draw_from_boneyard(boneyard)
            add_bone_to_hand(player, bone)

if __name__ == "__main__":
    main()

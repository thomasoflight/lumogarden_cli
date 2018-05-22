# ---IMPORTS--- #
import sys
sys.dont_write_bytecode = True

import os

# ---LISTS/DATA--- #
outlist_filename = "outlist.txt"
outlist_folder = os.path.dirname(os.path.curdir)
outlist_file = os.path.join(outlist_folder, outlist_filename)
outlist_obj = open(outlist_file, "r")
outlist_pool = [l.strip() for l in outlist_obj.readlines()]

room_out_filename = "room_out.txt"
room_out_folder = os.path.dirname(os.path.curdir)
room_out_file = os.path.join(room_out_folder, room_out_filename)
room_out = open(room_out_file, "r")
room_out_pool = [l.strip() for l in room_out.readlines()]


def main():
    review(room_out_pool)
    print()
    review(file_to_list(outlist_file))


def review(list_input):

    for item in list_input:
        print(item + "?")
        proceed = input("> ")


main()




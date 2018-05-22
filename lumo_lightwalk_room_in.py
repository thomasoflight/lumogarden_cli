#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

import lumo_filehandler as l_files

# ---LISTS/DATA--- #
entering_room_pool = [
    "CHANGE MY CLOTHES",
    "PUT AWAY STUFF FROM BAG"
    ]

def review(list_input):
    for item in list_input:
        print(item + "?")
        proceed = input("> ")

def wants_and_multipliers():
	print("\nWhat do I want to do versus what is a life-multiplier?")

def get_wants():
	wants = []
	fish_want = input("Tell me your spontaneous fish, my friend: ")

    if fish_want:
        l_files.Wrtrs().basic_wrtr(ascii_fish, destination_file)
        l_files.Wrtrs().basic_wrtr("\n ", destination_file)
        l_files.Wrtrs().basic_wrtr(l_files.today_frmttd, destination_file)
        l_files.Wrtrs().basic_wrtr("\n ", destination_file)

    while "done" not in fish_want:
        l_files.Wrtrs().basic_wrtr(fish_want, destination_file)
        l_files.Wrtrs().basic_wrtr("\n", destination_file)
        fish_want = input("Tell me another fish: ")


def select_hard_multipliers():
    review(entering_room_pool)
    wants_and_multipliers()


if __name__ == '__main__':
    spontaneous_fish()





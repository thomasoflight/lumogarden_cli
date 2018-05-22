#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

import os

# ---LISTS/DATA--- #
room_busking_filename = "room_busking.txt"
room_busking_folder = os.path.dirname(os.path.curdir)
room_busking_file = os.path.join(room_busking_folder, room_busking_filename)
room_busking_obj = open(room_busking_file, "r")
room_busking_pool = [l.strip() for l in room_busking_obj.readlines()]

def main():
    review(room_busking_pool)
    print()
    print("Have a good time busking Aprille :-) ")

def review(list_input):

    for item in list_input:
        print(item + "?")
        proceed = input("> ")

main()




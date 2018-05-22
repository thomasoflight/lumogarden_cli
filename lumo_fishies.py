#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode=True

import os
from os import path
from os.path import exists

import lumo_filehandler as l_files

fishies_filename = "fishies.txt"
fishies_file     = os.path.join(l_files.rootpath, fishies_filename)
ascii_fish       = "\n/o \\/\n\\  /\\"


def set_destination_file():

    # set_destination = input("All fishies or today? ")


    # if "all" in set_destination or "fishies" in set_destination:
    #     destination_file = fishies_file

    # elif set_destination == "today" and not exists(l_files.lightwalk_file):
    #     l_files.Wrtrs().mk_lightwalk()
    #     destination_file = l_files.lightwalk_file
    #     print("Lightwalk file created.")

        
    # elif set_destination == "today" and exists(l_files.lightwalk_file):
    #     destination_file = l_files.lightwalk_file
    
    # else:
    #     print("Hmm...not sure")

    return fishies_file


def spontaneous_fish():

    destination_file = set_destination_file()

    fish_task = input("Your spontaneous fish: ")

    if fish_task:
        l_files.Wrtrs().basic_wrtr(ascii_fish, destination_file)
        l_files.Wrtrs().basic_wrtr("", destination_file)

    while fish_task not in ["done", "no"]:
        l_files.Wrtrs().basic_wrtr(fish_task, destination_file)
        fish_task = input("Tell me another fish: ")

    l_files.Wrtrs().basic_wrtr("", destination_file)


if __name__ == '__main__':
    spontaneous_fish()








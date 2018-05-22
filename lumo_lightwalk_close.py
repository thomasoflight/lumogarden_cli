#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A file to collect feathers from the end of the day
and to express some end of the day thoughts."""

# ---IMPORTS--- #
import sys
sys.dont_write_bytecode = True

import datetime
import os
import subprocess

import lumo_filehandler as l_files
import lumo_feathers


# ---TIME--- #
today = datetime.date.today()
today_format = today.strftime("%d %b %Y")

# ---FILES--- #
lightwalk_filename = ("%s - Lightwalk.odf") % today_format
desktop_folder = "/Users/thomasoflight/Desktop"
close_file = os.path.join(desktop_folder, "close.txt")

lightwalk_file_desktop = os.path.abspath(
    os.path.join(desktop_folder, lightwalk_filename))

today_jrnl_entry_filename = ("%s ( ).txt") % today_format
today_jrnl_entry = os.path.abspath(
    os.path.join(desktop_folder, today_jrnl_entry_filename))


# ---LISTS/DATA--- #
restoration_pool = [
    "KITCHEN-->COUNTER/TRASH",
    "KITCHEN-->WATER REFILL",
    "PREP ZOLOFT",
    "NOISE MACHINE ON",
    "MOUTH GAURD OUT"
    "CARIES",
    "CLOKITS",
    "CAL QUICKCHECK",
    "NAILIES", 
    "ARTIES",
    "READZORS"
    ]
    
entering_room_pool = [
    "CHANGE MY CLOTHES",
    "PUT AWAY STUFF FROM BAG"
    ]

ascii_fish = "\n/o \\/\n\\  /\\"

# ---FUCNTIONS--- #


def review(list_input):

    list_output = []

    print("\n")
    for item in list_input:
        print(item + "?")
        to_append = input("> ")

        if to_append:
            item = "{} - {}".format(item, to_append.upper())
            list_output.append(item)

    l_files.Wrtrs().basic_wrtr_list(list_output, os.path.join(desktop_folder, "close.txt"))

def fisher(context, list_name=ascii_fish):

    fish_task = input(context)

    if fish_task:
        l_files.Wrtrs().basic_wrtr(list_name, close_file)

    while fish_task not in ["done", "no"]:
        l_files.Wrtrs().basic_wrtr(fish_task, close_file)
        fish_task = input("Another? ")

    l_files.Wrtrs().basic_wrtr("", close_file)


def wants_and_multipliers():

    print("\nWhat do I want to do versus what is a life-multiplier?\n")
    fisher("So what do I want to do? ", "Wants:")
    print("\n-vs-\n")
    fisher("What are some multipliers? ", "Multipliers:")


if __name__ == '__main__':
    
    # review(entering_room_pool)
    # wants_and_multipliers()
    review(restoration_pool)
    









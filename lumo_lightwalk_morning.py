#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath("../LUMO_UTILITIES"))

import datetime
import lumo_filehandler as l_files


# ---LISTS/DATA--- #
starbucks_pool = [
    "PUT ON CLOTHES",
    "PACK --> ART SUPPLIES",
    "PACK --> COMPUTER/CHARGER",
    "PACK --> CUP",
    ]

morning_pool = [
    "..music..",
    "..drawing..",
    "..breathies..",
]

room_io_out_pool = [
    "CELL PHONE", 
    "WALLET with CASH"
]


def wake_count():

    print()
    usr_rspnse = input("Let's hear about this morning. 1 or 0 and a description if you'd like: ")
    rspnse_w_date = "{} - {}".format(usr_rspnse, l_files.today_frmttd_spaces)
    l_files.Wrtrs().basic_wrtr(rspnse_w_date, l_files.wake_counter_file)

def sleep_count():

    print()
    usr_rspnse = input("Let's hear about last night, like how's the bedtime stuff? ")
    rspnse_w_date = "{} - {}".format(usr_rspnse, l_files.today_frmttd_spaces)
    l_files.Wrtrs().basic_wrtr(rspnse_w_date, l_files.sleep_counter_file)

def arte_count():
    print("....a....")

def code_count():
    print("....a....")

def review(list_input):

    for item in list_input:
        print(item + "?")
        proceed = input("> ")

if __name__ == '__main__':
    review(morning_pool)
    wake_count()
    sleep_count()
    arte_count()
    code_count()



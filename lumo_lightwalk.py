#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
sys.dont_write_bytecode = True

sys.path.append(os.path.abspath("../LUMO_UTILITIES"))
import lumo_journal

import time
import subprocess
from random import choice

import lumo_filehandler as l_files
import lumo_poolgen as poolgen
import lumo_poolgen_m as poolgen_m
import lumo_pools_m as pools_m
import lumo_lightwalk_close as lightwalk_close


def garden_awake():

    print('Hello awoken-ones...')
    print()
    my_feels = input(choice(pools_m.journal_questions))
    

    my_feels = "From lightwalk: {}".format(my_feels)

    if not lumo_journal.exists_entry_fortoday():
        l_files.Wrtrs().mk_jrnl()
    
    l_files.Wrtrs().basic_wrtr(l_files.cur_time_hr, l_files.tdy_jrnl_file)
    l_files.Wrtrs().basic_wrtr(my_feels, l_files.tdy_jrnl_file)

    l_files.Wrtrs().mk_lightwalk()

    more_journaling = input("Continue? ").lower()

    if more_journaling and more_journaling != 'no':
    	subprocess.run(['nano {}'.format(l_files.tdy_jrnl_file)], shell=True, executable='/bin/bash')

def morning_pool():

	curr_hour = l_files.today.strftime('%H')
	curr_hour_int = int(curr_hour)
	print()
	
	if curr_hour_int < 14:
		subprocess.call(['python3', 'lumo_lightwalk_morning.py'])
		

def select_pools():

	poolgen.BERNARD.generate()
	poolgen.BERNARD_SUNDAY.generate()
	poolgen.MARIE.generate()
	poolgen.THOMAS_OF_LIGHT.generate()
	poolgen.APRILL.generate()
	poolgen.UNICORN.generate()
	poolgen.GLITTER_KINDESS.generate()
	poolgen.WEEK.generate()

def alt_pools():

	poolgen.FISHIES.generate_fish()
	poolgen_m.MEDITATIONS.generate_meditations()

def restoration_pool():
	l_files.Wrtrs().pool_wrtr(
		"restoration",
		lightwalk_close.restoration_pool,
		l_files.lightwalk_file)

def garden_bless():
	print()
	print("Have a great day beautiful")
	time.sleep(4)

def lightwalk():
	garden_awake()
	morning_pool()
	select_pools()
	alt_pools()
	restoration_pool()
	garden_bless()

if __name__ == '__main__':
	lightwalk()




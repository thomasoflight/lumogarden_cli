#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

from random import choice

import lumo_filehandler as l_files
import lumo_poolgen as poolgen
import lumo_poolgen_m as poolgen_m
import lumo_pools_m as pools_m


def garden_awake():

    l_files.Wrtrs().mk_lightwalk_next()

def select_pools():

	poolgen.BERNARD.generate(False)
	poolgen.APRILL.generate(False)
	poolgen.MARIE.generate(False)
	poolgen.THOMAS_OF_LIGHT.generate(False)
	poolgen.ADA.generate(False)
	poolgen.WEEK.generate(False)
	poolgen.MONTH.generate(False)
	# poolgen.JULIAN.generate(False)

def alt_pools():

	poolgen.FISHIES.generate_fish(False)


# ---RUN--- #	
garden_awake()
select_pools()
alt_pools()


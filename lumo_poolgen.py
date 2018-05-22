
# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

import random

import lumo_pools as pools
import lumo_poolgen_cycle as cycleitems
import lumo_filehandler as l_files

class LightwalkPool(object):

    def __init__(self, pool_name, pool_items=["Default"], cycle_items=["Default"], is_ascii_art=False):
        self.pool_name = pool_name
        self.pool_items = pool_items
        self.cycle_items = cycle_items
        self.pool_output = []
        self.is_ascii_art = is_ascii_art


    def generate(self, today_lightwalk=True):

        print("\n")


        if len(self.cycle_items) >= 1 and self.cycle_items[0] != "Default":
            self.pool_items += self.cycle_items


        for i, pool_item in enumerate(self.pool_items):
            print(("%s ?") % pool_item)

            to_append = input("> ")


            if to_append and to_append.lower() != 'remove' :
                goal = "%s @ %s" % (pool_item, to_append)
                self.pool_output.append(goal)
            elif to_append.lower() == 'remove':
                print(i)


        if len(self.pool_output) >= 1 and today_lightwalk:
            l_files.Wrtrs().pool_wrtr(self.pool_name, self.pool_output,
                                     l_files.lightwalk_file, self.is_ascii_art)

        elif len(self.pool_output) >= 1 and not today_lightwalk:
            l_files.Wrtrs().pool_wrtr(self.pool_name, self.pool_output,
                                     l_files.lightwalk_file_next, self.is_ascii_art)

    def print_to_screen(self):


        if len(self.pool_items) >= 1 and self.pool_items[0] != "Default":
            print(self.pool_name.upper())
            print()

            for pool_item in self.pool_items:
                print(pool_item)
        

class FishiesPool(object):

    def __init__(self, pool_name, is_ascii_art):
        self.pool_name = pool_name
        self.pool_output_fish = []
        self.ascii_fish = "/o \\/\n\\  /\\"
        self.is_ascii_art = is_ascii_art


    def generate_fish(self, today_lightwalk=True):
        
        print("\n")
        print(self.ascii_fish)

        fish_task = input("Any wandering fishies today? ")

    
        while fish_task not in ["done", "no"]:
            self.pool_output_fish.append(fish_task)
            fish_task = input("Any more fishies? ")

        if len(self.pool_output_fish) >= 1 and today_lightwalk:
            l_files.Wrtrs().pool_wrtr(
                    self.ascii_fish, self.pool_output_fish, 
                    l_files.lightwalk_file, self.is_ascii_art)

        elif len(self.pool_output_fish) >= 1 and not today_lightwalk:
            l_files.Wrtrs().pool_wrtr(self.pool_name, self.pool_output_fish,
                                     l_files.lightwalk_file_next, self.is_ascii_art)
        


BERNARD = LightwalkPool("Bernard", pools.bernard_pool, cycleitems.bernard_cycle_items)
BERNARD_SUNDAY = LightwalkPool("Sunday", pools.sunday_pool)
GLITTER_KINDESS = LightwalkPool("Glitter Kindness", pools.glitter_kindness, cycleitems.glitter_kindness_items) 
APRILL = LightwalkPool("Aprill", pools.aprill_pool) #cycleitems.aprill_cycle_items
MARIE = LightwalkPool("Marie", pools.marie_pool)
THOMAS_OF_LIGHT = LightwalkPool("Thomas Of Light", 
                                pools.thomasoflight_pool, cycleitems.thomas_cycle_items)
JULIAN = LightwalkPool("Julian", pools.julian_pool)
ADA = LightwalkPool("Ada", pools.ada_pool)

UNICORN = LightwalkPool("Unicorn", pools.utfh_pool, cycleitems.utfh_cycle_items)
WEEK = LightwalkPool("Shimmering Stars", random.sample(pools.shimmering_stars, len(pools.shimmering_stars)))

FISHIES = FishiesPool("Fishies", True)



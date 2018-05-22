# lumo_poolgen_m.py

import sys
sys.dont_write_bytecode = True

import os
import time
from random import choice

import lumo_pools_m as pools_m
import lumo_filehandler as l_files

class MeditatorPool(object):

    def __init__(self, pool_m_name, is_ascii_art,
                 pool_m_a=[""], pool_m_b=[""],
                 pool_m_c=[""], pool_m_d=[""]
                 ):

        self.pool_m_name = pool_m_name
        self.is_ascii_art = is_ascii_art

        self.pool_m_a = pool_m_a
        self.pool_m_b = pool_m_b
        self.pool_m_c = pool_m_c
        self.pool_m_d = pool_m_d

        self.pool_m_output = []

    def generate_mini(self):
        
        self.pool_m_output.append(
                            choice(self.pool_m_a))

        self.pool_m_output.append(
                            choice(self.pool_m_b))

        self.pool_m_output.append(
                            choice(self.pool_m_c))

        self.pool_m_output.append(
                            choice(self.pool_m_d))

    def generate_meditations(self):
    
        self.generate_mini()

        print("\n")
        time.sleep(.4)
        print(".-.-.-.--.-.-.-.")

        for meditation in self.pool_m_output:
                if meditation:
                    print(meditation)
                    time.sleep(.6)
                for dot in '...-':
                    if dot == '-':
                        break
                    print(dot)
                    time.sleep(.3)

        l_files.Wrtrs().pool_wrtr(self.pool_m_name, self.pool_m_output, 
                                  l_files.lightwalk_file, self.is_ascii_art)


MEDITATIONS = MeditatorPool(".-.-.-.--.-.-.-.", True, 
                            pools_m.risks, pools_m.minds,
                            pools_m.identities, pools_m.needs)





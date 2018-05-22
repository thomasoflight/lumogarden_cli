# lumo_poolgen_cycles.py{}

import sys
sys.dont_write_bytecode=True

import os
from os import path

import lumo_filehandler as l_files
import lumo_pools_cycle as cyclepools


class CyclePool(object):
        
    def unpack_cylce_tuple(self, tuple):
        
        task, cycle_days, log_filename = tuple
            
        log_file = os.path.join(l_files.logging_folder, log_filename)
            
        return task, cycle_days, log_file

    def read_log(self, cycle_file):
        with open(cycle_file, "r") as fin:
            last_cycle = fin.readline()

        return last_cycle


    def calculate_days_elpsd(self, last_cycle):

        d, m, y = last_cycle.split()
        log_frmtd = l_files.datetime.datetime(int(y), int(m), int(d))
        days_elpsd = l_files.today - log_frmtd

        return days_elpsd


    def generate(self, cycle_tuples):

        self.cycle_output = []

        for item in cycle_tuples:
            task, cycle_days, log_file = self.unpack_cylce_tuple(item)
            recent_cycle = self.read_log(log_file)
            days_elpsd = self.calculate_days_elpsd(recent_cycle)

            threshold_date = l_files.datetime.timedelta(days=cycle_days)

            if days_elpsd >= threshold_date:
                task = ("Cycle Pools: %s") % task
                self.cycle_output.append(task)
                l_files.Wrtrs().over_wrtr(l_files.today_frmttd_log, log_file)
            else:
                continue

        return self.cycle_output


bernard_cycle_items     = CyclePool().generate(cyclepools.bernard)
thomas_cycle_items      = CyclePool().generate(cyclepools.thomasoflight)
utfh_cycle_items        = CyclePool().generate(cyclepools.utfh)
glitter_kindness_items  = CyclePool().generate(cyclepools.glitter_kindness)



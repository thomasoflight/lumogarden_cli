#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

import datetime
import os
import sys 
sys.path.append(os.path.abspath("../LUMO_GARDEN_MAC/"))
import subprocess

import lumo_filehandler as l_files 


def exists_entry_fortoday():
	return os.path.exists(l_files.tdy_jrnl_file)


def write_journal():
	if exists_entry_fortoday():
		l_files.Wrtrs().basic_wrtr("", l_files.tdy_jrnl_file)
		l_files.Wrtrs().basic_wrtr("", l_files.tdy_jrnl_file)
		l_files.Wrtrs().basic_wrtr("{}".format(l_files.cur_time_hr), l_files.tdy_jrnl_file)

		subprocess.call(['open {}'.format(l_files.tdy_jrnl_file)], shell=True, executable='/bin/zsh')

	else:
		l_files.Wrtrs().basic_wrtr(l_files.today_frmttd, l_files.tdy_jrnl_file)
		l_files.Wrtrs().basic_wrtr("", l_files.tdy_jrnl_file)
		l_files.Wrtrs().basic_wrtr("{}".format(l_files.cur_time_hr), l_files.tdy_jrnl_file)


		subprocess.call(['open {}'.format(l_files.tdy_jrnl_file)], shell=True, executable='/bin/zsh')

if __name__ == '__main__':
	write_journal()

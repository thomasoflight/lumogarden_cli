import os, sys, subprocess
import re
from itertools import count

sys.path.append(os.path.abspath("../LUMO_GARDEN_MAC/"))

import lumo_filehandler as l_files 

sys.dont_write_bytecode = True

# ----------------------------------------------------- #

def get_int(today_ethos_notes):
	most_recent_note = today_ethos_notes[-1]
	curr_note_int = re.findall('\d+(?=\.)', most_recent_note)
	next_note_int = int(curr_note_int[0]) + 1
	return next_note_int

def get_next_note(int):
	ethos_filename = ("{}_%02i.txt".format(l_files.ethos_filename) 
								% i for i in count(int))
	ethos_filename = next(ethos_filename)
	return ethos_filename

def today_has_ethos():
	target_date = re.compile((l_files.today_frmttd).upper())

	all_notes = os.listdir(l_files.ethos_folder)
	print(all_notes)
	today_ethos_notes = [note for note in all_notes if target_date.search(note)]
	return today_ethos_notes


def write_ethosnote():
	today_ethos_notes = today_has_ethos()
	if today_ethos_notes:
		next_note_int = get_int(today_ethos_notes)
	else:
		next_note_int = 1

	ethos_filename = get_next_note(next_note_int)
	ethos_file = os.path.join(l_files.ethos_folder, ethos_filename)

	l_files.Wrtrs().basic_wrtr(l_files.cur_time_hr,
							   ethos_file)
	subprocess.call(['open', '-a' 'Sublime Text.app', ethos_file])


if __name__ == '__main__':
	write_ethosnote()


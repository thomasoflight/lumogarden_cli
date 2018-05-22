import sys
sys.dont_write_bytecode = True


import datetime
import os
import subprocess
sys.path.append(os.path.abspath("../LUMO_GARDEN_MAC/"))
import lumo_filehandler as l_files

def write_dreams():
	today = datetime.date.today()
	dream_filename = today.strftime("Dream_%d_%b_%Y.txt")

	desktop_folder = "/Users/thomasoflight/Desktop"
	dream = os.path.join(desktop_folder, dream_filename)

	subprocess.run(['touch ~/Desktop/"{}"'.format(dream_filename)], shell=True, executable='/bin/bash')
	subprocess.run(['open ~/Desktop/"{}"'.format(dream_filename)], shell=True, executable='/bin/bash')

if __name__ == '__main__':
	write_dreams()

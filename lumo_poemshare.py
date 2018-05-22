import sys
sys.dont_write_bytecode = True


import datetime
import os
import subprocess
import lumo_filehandler as l_files

def write_poem():
	today = datetime.date.today()
	poem_filename = today.strftime("Poemseed_%d_%b_%Y.txt")

	desktop_folder = "/Users/thomasoflight/Desktop"
	poem = os.path.join(desktop_folder, poem_filename)

	subprocess.run(['touch ~/Desktop/"{}"'.format(poem_filename)], shell=True, executable='/bin/bash')
	subprocess.run(['open ~/Desktop/"{}"'.format(poem_filename)], shell=True, executable='/bin/bash')

if __name__ == '__main__':
	write_poem()

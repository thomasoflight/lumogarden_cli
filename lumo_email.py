import sys
sys.dont_write_bytecode = True


import datetime
import os
import subprocess
sys.path.append(os.path.abspath("../LUMO_GARDEN_MAC/"))
import lumo_filehandler as l_files

def write_email():
	recipient = input("Hey babe, who you writing to? ").capitalize()
	
	today = datetime.date.today()
	today_frmttd = today.strftime("%d_%b_%Y")
	email_filename = "email_{}_{}.txt".format(recipient, today_frmttd)

	desktop_folder = "/Users/thomasoflight/Desktop"
	email = os.path.join(desktop_folder, email_filename)

	print(email)

	l_files.Wrtrs().basic_wrtr("Hi {} - ".format(recipient), email)
	l_files.Wrtrs().basic_wrtr("".format(recipient), email)
	l_files.Wrtrs().basic_wrtr("".format(recipient), email)


	subprocess.call(['nano {}'.format(email)], shell=True, executable='/bin/bash')

if __name__ == '__main__':
	write_email()

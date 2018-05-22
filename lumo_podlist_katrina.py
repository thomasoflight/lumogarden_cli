import os
import argparse
import lumo_filehandler as l_files

suitcase = argparse.ArgumentParser()

suitcase.add_argument(
		# 'pod_title',
		 action='store',
		 dest='pod_title',
		 nargs="+",
		 help="So, what is the name of the book(s) you are adding?")

# suitcase.add_argument(
# 		'BOOK CATEGORIES --->',
# 		nargs='?',
# 		help="ARTE; SOFT; LGHT; FIC; NONFIC; RECOVERY")

options = suitcase.parse_args()

def main():
   pods_txt_file = "/Users/thomasoflight/Sync/LUMO_UTILITIES/podlist_katrina.txt"

   pods = "".join((options.pod_title))
   pods = pods.split(";; ")
   pods = [pod.title() for pod in pods]

   l_files.Wrtrs().basic_wrtr_list(pods, pods_txt_file) 

if __name__ == '__main__':
	main()

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
		'no. of rounds', 
		 metavar='num_rounds',
		 help="How many rounds of timers do you want?")

# parser.add_argument(
# 		# 'book_title',
# 		 action='store',
# 		 dest='book_title',
# 		 nargs="+",
# 		 help="So, what is the name of the book(s) you are adding?")

# parser.add_argument(
# 		'BOOK CATEGORIES --->',
# 		nargs='?',
# 		help="ARTE; SOFT; LGHT; FIC; NONFIC; RECOVERY")


options = parser.parse_args()


def main():
   print(options.num_rounds)

if __name__ == '__main__':
	main()

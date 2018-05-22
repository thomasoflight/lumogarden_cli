import os
import argparse
import lumo_filehandler as l_files

suitcase = argparse.ArgumentParser()


suitcase.add_argument(
		'book_category', 
		 metavar='book_category',
		 help="Which category is this? E.G. 'erth', 'lght', 'soft'")

suitcase.add_argument(
		# 'book_title',
		 action='store',
		 dest='book_title',
		 nargs="+",
		 help="So, what is the name of the book(s) you are adding?")

suitcase.add_argument(
		'BOOK CATEGORIES --->',
		nargs='?',
		help="ARTE; SOFT; LGHT; FIC; NONFIC; RECOVERY")


options = suitcase.parse_args()


def main(folder):
   books_category_file = os.path.join(folder, l_files.bookstr_to_filename[(options.book_category).lower()])

   books = "".join((options.book_title))
   books = books.split(";; ")
   books = [book.title() for book in books]

   l_files.Wrtrs().basic_wrtr_list(books, books_category_file) 

if __name__ == '__main__':
	main(l_files.booklist_folder)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import lumo_filehandler as l_files

suitcase = argparse.ArgumentParser()

suitcase.add_argument(
		'film_category', 
		 metavar='film_category',
		 help="Which category is this? E.G. 'film', 'show'")

suitcase.add_argument(
		 action='store',
		 dest='film_title',
		 nargs="+",
		 help="So, what is the name of the film/show(s) you are adding?")

suitcase.add_argument(
		'FILM CATEGORIES --->',
		nargs='?',
		help="FILM; SHOW")


options = suitcase.parse_args()


def main(folder):
   film_category_file = os.path.join(folder, l_files.filmstr_to_filename[(options.film_category).lower()])

   films = "".join((options.film_title))
   films = films.split(";; ")
   films = [film.title() for film in films]

   l_files.Wrtrs().basic_wrtr_list(films, film_category_file) 

if __name__ == '__main__':
	main(l_files.filmlist_folder)

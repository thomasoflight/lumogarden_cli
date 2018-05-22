#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lumo_filehandler import lightwalk_file

def sugar_maple_dance(doc):
	with open(doc) as fin:
		for line in fin.readlines():
			print(line, end='')

if __name__ == '__main__':
	sugar_maple_dance(lightwalk_file)

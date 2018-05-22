#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True
import os
import re
import itertools


import lumo_filehandler as l_files

def main():

	feathers_list, f_count = load_feathers(l_files.feathers_file)
	feather_data = strip_descriptions(feathers_list)
	fth_sngl, fth_multi = separate_two_groups(feather_data)
	fth_sngl_b = multi_fth_to_single(fth_multi)
	intgrs_a = feather_to_int(fth_sngl + fth_sngl_b)
	intgrs_b = int(sum(intgrs_a))

	print('\nFeathers totaled in this list: {}'.format(intgrs_b))
	return intgrs_b, f_count

# @staticmethod
# main():
# 	feathers_list, f_count = load_feathers(l_files.feathers_file)



def load_feathers(file):
	print('Collecting feathers...')

	feathers_list = [ l.strip() for l in open(file, "r")]
	f_count = len(feathers_list)
	print(f"{f_count} feathers found.")

	return feathers_list, f_count


def strip_descriptions(list):
	feathers_updated = []
	
	for line in list:
		if line.split():
			line = line.split()
			line = line[0].strip('+')
			feathers_updated.append(line)

	return feathers_updated


def separate_two_groups(list):

	single_feathers = []
	multi_feathers = []

	for item in list:
		if item[0].isdigit():
			multi_feathers.append(item)
		else:
			single_feathers.append(item)

	return single_feathers, multi_feathers


def multi_fth_to_single(fth_list):
	converted_feathers = []

	for item in fth_list:
		multiplier, feather, ign = re.split('(\D+)', item)
		feathers = list(itertools.repeat(feather, int(multiplier)))
		converted_feathers += feathers

	return converted_feathers


def feather_to_int(feather_keys):
	marias = {
	'SP'   :.33,	# seed plume
	'IC'   :.66,	# interpreter cookies
	'CK'   :.66,	# interpreter cookies
	'SPR'    :1,	# spring timers
	'APL'    :1,	# spring timers
	'FF'     :1,	# fire feather
	'UF'     :3,	# unicorn feather
	'MB'    :12,	# moon bloom
	'WB'    :24,	# wind bloom
	'TC'    :72,	# trillogie coinb
	'TS'    :144	# trillogie spark
	}

	fth_ints = [marias[f] for f in feather_keys if marias.get(f)]

	return fth_ints



if __name__ == '__main__':
	main()

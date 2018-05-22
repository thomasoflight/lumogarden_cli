import sys
sys.dont_write_bytecode = True

import os
import re
import itertools
import time
import random

import lumo_feathers_sum

marias = {
'SP'     :.33,    # seed plume
'SPR'    :1.0,    # spring timers
'APL'    :1.0,    # spring timers
'FF'     :1.0,    # fire feather
'UF'     :3.0,    # unicorn feather
'MB'    :12.0,    # moon bloom
'WB'    :24.0,    # wind bloom
'TC'    :72.0,    # trillogie coinb
'TS'   :144.0     # trillogie spark
}

def spark():
    feathers_file = get_feathers_file()
    feathers_list = load_feathers(feathers_file)
    feathers      = strip_descriptions(feathers_list)

    (intgrs_mac, feathers_count) = lumo_feathers_sum.main()
    print(intgrs_mac)
    spklift_call = int(input('How many feathers do you spark to the wind? '))

    spklift_ratio_float = spklift_call / intgrs_mac
    spklift_percentage = ("{0:.02f}%".format((spklift_ratio_float) * 100))
    print(f'this would represent a reduction in feathers by ...{spklift_percentage}...')

    confirm = input("Confirm? ")
    print(confirm)

    # if not confirm:
        # sys.exit(0)

    idx              = 0
    total            = 0
    fth_count    = 0

    while feathers:
        f = feathers[idx]
        fth = feather_to_singl_int(f)

        if spklift_call - total < 2:
            break
        elif total + fth > spklift_call:
            idx += 1
            print('skipping {}'.format(f))
            continue
        else:
            print(fth, total); time.sleep(.02)
            total += fth
            idx += 1
            fth_count += 1

    print('{} feathers released for {}'.format(fth_count, total))

    


def feather_to_singl_int(fth):

    if fth[0].isdigit():
        separator, fth_multiplier, fth_base = re.split('(^\d*)', fth)

        fth_base = marias.get(fth_base, 0)
        fth_float = float(fth_multiplier)
        return fth_float * fth_base

    else:
        return marias.get(fth, 0)


def get_feathers_file():
    base_folder = os.path.dirname(__file__)
    feathers_fullpath = os.path.join(base_folder, "feathers.txt")

    return feathers_fullpath


def load_feathers(file):

    return [line for line in open(file, 'r')]


def strip_descriptions(loaded_feathers):
    feathers_updated = []
    
    for line in loaded_feathers:
        if line.split():
            line = line.split()
            line = line[0].strip('+')
            feathers_updated.append(line)

    return feathers_updated

if __name__ == '__main__':
    spark()

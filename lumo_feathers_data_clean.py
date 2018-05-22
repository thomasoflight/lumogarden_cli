import os
import re

marias = {
'SP'     :.33,    # seed plume
'SPR'    :1.0,    # spring timers
'APL'    :1.0,    # spring timers
'MAC'    :1.0,    # mac feather 
'FF'     :1.0,    # fire feather
'UF'     :3.0,    # unicorn feather
'MB'    :12.0,    # moon bloom
'WB'    :24.0,    # wind bloom
'TC'    :72.0,    # trillogie coinb
'TS'   :144.0     # trillogie spark
}

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


def feather_to_singl_int(fth):

    if fth[0].isdigit():
        separator, fth_multiplier, fth_base = re.split('(^\d*)', fth)

        fth_base = marias.get(fth_base, 0)
        fth_float = float(fth_multiplier)
        return fth_float * fth_base

    else:
        return marias.get(fth, 0)


def write_feathers(generator):
    with open('feathers.txt', 'w+') as fout:
        for line in generator:
            fout.write(line)

feathers_file   = get_feathers_file()
feathers_raw    = load_feathers(feathers_file)
feathers_units  = strip_descriptions(feathers_raw)
feathers        = [feather_to_singl_int(f) for f in feathers_units]

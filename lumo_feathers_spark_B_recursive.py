import sys
sys.dont_write_bytecode = True

import itertools
import time
import random

from lumo_feathers_data_clean import feathers_raw, feathers, write_feathers
import lumo_feathers_sum 



def main():
    fth_available_sum = lumo_feathers_sum.main()
    print(fth_available_sum)
    spk_call = int(input('How many feathers do you spark to the wind? '))
    
    spklift_ratio_float = spk_call / fth_available_sum
    spklift_percentage = "{0:.02f}%".format((spklift_ratio_float) * 100)

    print('this represents a reduction in feathers by ...{}...'.format(spklift_percentage) )

    do_stuff_b(spk_call)
    write_feathers((f for f in feathers_raw if f))
    # confirm = input('spark initiate? ')

    # if confirm.lower() == 'y':
        # write_feathers(feathers_raw)

def do_stuff(spk_call, feathers, fth_count=0, total=0, idx=0):

    if (spk_call - total < 2) or (idx == len(feathers)):
        print('{} feathers prepped for {}'.format(fth_count, total))
        return 

    fth = feathers[idx]
    updated_total = total + fth
    next_idx = idx + 1

    if updated_total > spk_call:
        do_stuff(spk_call, feathers, fth_count, total, next_idx)
    else:
        time.sleep(.02); print(updated_total)
        # feathers_raw[next_idx-1] = 
        fth_count += 1
        do_stuff(spk_call, feathers, fth_count, updated_total, next_idx)

def do_stuff_b(spk_call):
    idx = 0
    total = 0

    while idx < len(feathers):
        time.sleep(.1)
        if (spk_call - total < 2):
            break
        if total + feathers[idx] > spk_call:
            print("skipped")
            idx += 1
            continue

        total += feathers[idx]
        feathers_raw[idx] = ""
        print( f'added, total is {total}' )
        idx += 1

    return total

if __name__ == '__main__':
    main()


# ---IMPORTS--- #
import sys
sys.dont_write_bytecode = True

import os

# ---LISTS/DATA--- #
room_podcast_filename = "room_podcast.txt"
room_podcast_folder = os.path.dirname(os.path.curdir)
room_podcast_file = os.path.join(room_podcast_folder, room_podcast_filename)
room_podcast_obj = open(room_podcast_file, "r")
room_podcast_pool = [l.strip() for l in room_podcast_obj.readlines()]


def main():
    review(room_podcast_pool)
    print()
    print("Have a great time!!!")

def review(input_list):

    for item in input_list:
        print(item + "?")
        proceed = input("> ")


main()




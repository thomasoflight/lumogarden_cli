#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime

# ---TIME--- #
today = datetime.datetime.today()
today_frmttd = today.strftime("%d_%b_%Y")
today_frmttd_spaces = today.strftime("%d %b %Y")
today_frmttd_log = today.strftime("%d %m %Y")

is_Sunday = (datetime.date.weekday(today) == 6)
week_from_today = (today + datetime.timedelta(weeks=1)).strftime("%A, %B %d, %Y")

tomrrw = today + datetime.timedelta(days=1)
tomrrw_frmttd = tomrrw.strftime("%d%b %Y")

cur_time = today.strftime("%H:%M:%S")
cur_time_hr = "----------{}----------".format(cur_time)

# ---FILES--- #
rootpath = u"~/Desktop"

lightwalk_filename = ("%s_Lightwalk.odt") % today_frmttd.upper()
lightwalk_filename_next = ("%s - Lightwalk.odt") % tomrrw_frmttd.upper()
tdy_jrnl_filename = ("%s.txt") % today_frmttd
ethos_filename = ("ethos_%s") % today_frmttd.upper()


desktop_folder = u"~/Desktop/"
tresorit_folder = u"~/Desktop/"
lightwalk_folder = u"~/Desktop/"

journaling_folder = u"~/Desktop/"
logging_folder =  u"~/Desktop/"
ethos_folder = u"~/Desktop/"

outlist_filename = "outlist.txt"
outlist = os.path.join(rootpath, outlist_filename)



lightwalk_file = os.path.join(lightwalk_folder, lightwalk_filename)
lightwalk_file_next = os.path.join(desktop_folder, lightwalk_filename_next)

tdy_jrnl_file = os.path.join(journaling_folder, tdy_jrnl_filename)
close_file = os.path.join(desktop_folder, "close.txt")

wake_counter_file = os.path.join(desktop_folder, "wake_counter.txt")
sleep_counter_file = os.path.join(desktop_folder, "sleep_counter.txt")

ethos_file = os.path.join(ethos_folder, ethos_filename)
feathers_file = os.path.join(rootpath, "feathers.txt")


# ---FILES:BOOKLIST--- #
booklist_folder = "~/Desktop/"
filmlist_folder = "~/Desktop/"


bookstr_to_filename = {
    'lght':"booklist_lght.txt",
    'soft':"booklist_soft.txt",
    'nonfic':"booklist_nonfic.txt",
    'fic':"booklist_fic.txt",
    'arte':"booklist_arte.txt",
    'recovery':"booklist_recovery.txt"
    }

filmstr_to_filename = {
    'film':"filmlist_film.txt",
    'show':"filmlist_show.txt",
    }

# ---FUNCTIONS--- #
class Wrtrs(object):
    
    def pool_wrtr(self, pool_name, pool_output, file, ascii_art=None):
        
        with open(file, "a+") as fin:

                if ascii_art:                
                    fin.write("\n\n")
                    fin.write(pool_name)

                else:
                    pool_name_frmttd = ("\n\n-%s-") % pool_name.upper()
                    fin.write(pool_name_frmttd)


                for goal in pool_output:
                    fin.write("\n")
                    fin.write(goal)


    def basic_wrtr(self, content, file):

        with open(file, "a+") as fin:
            fin.write(content)
            fin.write("\n")


    def over_wrtr(self, content, file):

        with open(file, "w+") as fin:
            fin.write(content)
            fin.write("\n")

    def over_wrtr_list(self, list, file):

        with open(file, "w+") as fin:
            for item in list:
                fin.write(item)
                fin.write("\n")

    def basic_wrtr_list(self, list, file):

        with open(file, "a+") as fin:
            for item in list:
                fin.write(item)
                fin.write("\n")

    def mk_jrnl(self):
        self.basic_wrtr(today_frmttd.upper(), tdy_jrnl_file)
        self.basic_wrtr("", tdy_jrnl_file)


    def mk_lightwalk(self):
        self.basic_wrtr("LIGHTWALK: {}".format(today_frmttd_spaces.upper()), lightwalk_file)
        

    def mk_lightwalk_next(self):
        self.basic_wrtr(tomrrw_frmttd.upper(), lightwalk_file_next)
        self.basic_wrtr(" - LIGHTWALK", lightwalk_file_next)



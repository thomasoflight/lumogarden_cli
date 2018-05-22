import sys
sys.dont_write_bytecode = True

import lumo_filehandler as l_files

# ---FUNC--- #
def feathers_go():

    feather_input = input("> ")

    while feather_input.lower() != "done":
        string = str(feather_input)
        list = string.split()

        begn = list[0]
        end = ' '.join(list[1:])
        feather_frmttd = "+{0} ------ {2} --------- {1}".format(begn, end, l_files.today_frmttd)

        with open("feathers.txt", "a") as fin:
            fin.write(feather_frmttd.upper())
            fin.write("\n")

        feather_input = input("> ")

if __name__ == '__main__':
	feathers_go()



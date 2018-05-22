import lumo_filehandler as l_files

def querier():

	query_content = "..."

	while query_header not in ["done", "no"]:
		query_header = input("header: ")
		query_content = input(": ")
		query = "{} --> {}".format(query_header, query_content)
		l_files.Wrtrs().basic_wrtr(query, l_files.queries_file)
		

def explorer():

    print()
    l_files.Wrtrs().basic_wrtr(rspnse_w_date, sleep_counter_file)


# def spontaneous_fish():

#     destination_file = set_destination_file()

#     query = input("Tell me your spontaneous fish, my friend: ")

#     if fish_task:
#         l_files.Wrtrs().basic_wrtr(ascii_fish, destination_file)
#         l_files.Wrtrs().basic_wrtr("", destination_file)

#     while fish_task not in ["done", "no"]:
#         l_files.Wrtrs().basic_wrtr(fish_task, destination_file)
#         fish_task = input("Tell me another fish: ")

#     l_files.Wrtrs().basic_wrtr("", destination_file)


if __name__ == '__main__':
    querier()

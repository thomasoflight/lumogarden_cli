import collections


project_tasks = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print(project_tasks)

def display(list):
	for task in list:
		print(task, end=' ')


def main():
	cmd = None

	while cmd.lower() != 'x':
		cmd = input('[D]el or e[X]it')

		if cmd.lower() == 'd':
			delete_mode()
		else:
			break 

def delete_mode(tasks):
	cmd = None
	
	while cmd != 'x':
		cmd = input('> ')
		
		try:
			cmd = int(cmd)
			cmd -= 1

			display(tasks)
			print('deleting \'{}\' from list'.format(tasks[cmd]))
			tasks.__delitem__(cmd)
			# load(tasks)
			display(tasks)
		
		except:
			pass

		

delete_mode(project_tasks)

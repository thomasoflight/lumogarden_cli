import pickle
pickle_file='...'

def get_pickle_data(pickle_file):
	with open(pickle_file, 'rb') as p_fin:
		unpickled = pickle.load(p_fin)
	return unpickled

def wrt_pickle_data(pickle_file, data):
	with open(pickle_file, 'wb') as p_out:
		pickle.dump(data, p_out, pickle.HIGHEST_PROTOCOL)



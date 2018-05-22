import pickle
from lumo_filehandler import week_from_today


def get_existing_stars():
	with open('shimmering_stars.pickle', 'rb') as s_s:
	    shimmering_stars = pickle.load(s_s)

	return shimmering_stars
   

def retain_stars():
	existing_stars = get_existing_stars()
	retained_stars = []

	for star in existing_stars:
		retain = input(f"{star} > ")
		star_name = star.split()[0][:-1]

		if retain and retain.lower() != 'no':
			print('Shimmering Star: {} carries over to next week'.format(star_name))
			retained_stars.append(star)

	return retained_stars


def get_new_stars():
	print()
	new_stars = []
	new_star = input('New star >>> ') #  placeholder

	while new_star and new_star.lower() != 'done':
		new_star_w_date = (f"{new_star}:  {week_from_today}")
		new_stars.append(new_star_w_date)
		print(f'{new_star_w_date} added.')
		new_star = input('New star >>> ')

	return new_stars


def update_stars():
	retained_stars = retain_stars()
	new_stars = get_new_stars()
	updated_stars = retained_stars + new_stars

	return updated_stars


def write_stars():
	updated_stars = update_stars()

	with open('shimmering_stars.pickle', 'wb') as stars:
	    pickle.dump(updated_stars, stars, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
	write_stars()

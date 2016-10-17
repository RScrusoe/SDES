import csv
import os


global license_key_list, number_of_slots 
license_key_list = [i*100+1 for i in range(1,41)]
number_of_slots = 40

class User(object):
	def __init__(self, roll, password):
		"""User class

		:param roll: roll number of the users
		:param password: password of the user
		:returns: User object
		:rtype: Object

		"""
		self.roll = roll
		self.password = password


def generate_csv(date,month,year):
	# Assuming we have 40 icenses
	# Assuming 12 slots of 2 hours each in one day

	if str(year) not in os.listdir():
		os.mkdir(str(year))
	if str(month) not in os.listdir(str(year)):
		os.mkdir(str(year) + '/' + str(month))
	if (str(date) + '.csv') not in os.listdir(str(year) + '/' + str(month)):
		file = open(str(year) + '/' + str(month) + '/' + str(date) + '.csv' , 'w')
		writer = csv.writer(file,delimiter=",")
		for i in range(1,len(license_key_list) + 1):
			row = [license_key_list[i-1]] + [-1 for i in range(number_of_slots)]
			print(row)
			writer.writerow(row)
		file.close()

def show_available_slots(date,month,year):
	
	


def create_users(n):
	"""Creates n number of users with random roll number and random
password and stores them in users.csv file with 1st column being roll
number and 2nd being the passwrod

	:param n: number of users
	:returns: list of User instances and generates csv file.
	:rtype: list

	"""
	file = open('users.csv', 'w')
	writer = csv.writer(file, delimiter=",")
	users = []
	for i in range(1, n + 1):
		user = User(str(i), str(i) + 'a' )
		row = [user.roll , user.password]
		users.append(user)
		writer.writerow(row)
	file.close()
	return users
create_users(100)

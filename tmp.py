import os
import csv
global license_key_list, number_of_slots 
license_key_list = [i*100+1 for i in range(1,41)]
number_of_slots = 40

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

generate_csv(14,10,2016)
print(os.listdir('asd'))
print(license_key_list)


w = open('2016/10/14.csv','r')
reader = csv.reader(w)
for i in reader:
	print(i[7])
	if int(i[7]) == -1:
		print("####")
	break
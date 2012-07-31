#-------------------------------------------------------------------------------
# Name:        android_json2csv.py
# Purpose:     Convert json file of android app store into a csv file
#				with relevant information
#
# Author:      Mike Laderman
#
# Created:     July 2012
# Copyright:   (c) Mike Laderman 2012
# 
#-------------------------------------------------------------------------------

import csv
import json
from time import sleep

def main(input_file,output_file):
	'''Takes in json data, reads extracts key values from each line,
	and writes each line to a csv file for android app information'''


	#Open json data, read it in, and close the file
	print("Reading in JSON...")
	f = open(input_file,'r')

	#array of json lines
	reader = f.readlines()
	f.close()

	print("Creating CSV File...")
	sleep(1)
	#opens csv file to be written in
	f = open(output_file,'a')
	writer = csv.writer(f,dialect = 'excel',quoting=csv.QUOTE_NONNUMERIC)

	#writes title row
	writer.writerow(('Email','Category','Developer','Price','Min Installs','Number of Ratings','Rating'))

	#counter to keep track how many apps have been crawled.
	i = 0
	for line in reader:
		i+=1
		try:

			#loads json line into a variable
			d = json.loads(line)
			#extracts values from key pairs in JSON
			info = app_info(d)

			#writes app info line
			writer.writerow(info)
			print(i)
			print(info)
		except ValueError:
			print('Error')
			pass
	return

def app_info(JSON):
	'''Returns tuple of (title,emails, category, dev, prices, minimum_installs,rating_count,rating)'''
	try:
		title = name(JSON)
		emails = dev_emails(JSON)
		cat = category(JSON)
		dev = dev_name(JSON)
		prices = price(JSON)
		installs = installs_min(JSON)
		rating_count = num_ratings(JSON)
		rating = rating_value(JSON)
		return (title,emails, cat, dev, prices, installs,rating_count,rating)
	except:
		print('Error in the app_info function!')
		pass
		

def name(JSON):
	'''Returns category'''
	try:
		return JSON['name']
	except KeyError:
		return 'Title Not Found'


def dev_emails(JSON):
	'''Returns Email Address'''
	try:
		emails = JSON['dev_emails']
		if len(emails) > 1:
			return str(emails[0])
		elif len(emails) == 1:
			return str(emails[0])
		else:
			return ''
	except KeyError:
		return 'Emails Not Found'

def category(JSON):
	'''Returns category'''
	try:
		return JSON['category']
	except KeyError:
		return 'Category Not Found'

def dev_name(JSON):
	'''Returns dev'''
	try:
		return JSON['dev_name']
	except KeyError:
		return 'Name Not Found'

def price(JSON):
	'''Returns price'''
	try:
		return JSON['price']
	except KeyError:
		return 'Price Not Found'	

def installs_min(JSON):
	'''Returns minimum installation threshold'''
	try:
		return JSON['installs_min']
	except KeyError:
		return 'Installs Min Not Found'

def num_ratings(JSON):
	'''Returns number of ratings'''
	try:
		return JSON['rating_count']
	except KeyError:
		return 'Rating Count Not Found'

def rating_value(JSON):
	'''Returns average rating'''
	try:
		return JSON['rating_value']
	except KeyError:
		return 'Rating Not Found'	

if __name__ == "__main__":
	main('marketplace-database.json_lines','android_devs.csv')
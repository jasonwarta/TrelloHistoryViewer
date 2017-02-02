#!/usr/bin/env python

import json,sys

reload(sys)  
sys.setdefaultencoding('utf8')

def loadData():
	with open('activity.json') as data_file:
		parsed_data = json.load(data_file)
		return parsed_data

def main():
	data = loadData()
	for item in data['lists']:
		print(item['name'])
	for item in data['actions']:
		print(item['type'])

if __name__ == '__main__':
	main()
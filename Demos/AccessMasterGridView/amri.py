import time 
from time import sleep
import requests
import json
import pprint
import csv
from datetime import datetime




def writeDictToCSV( filename, data):

	f = open(filename, 'w')
	f.write('TimeStamp')
	f.write('\t')
	f.write('Value')
	f.write('\n')
	for row in data:
		timestamp = datetime.fromtimestamp(row)
		f.write(str(timestamp))
		f.write('\t')
		f.write(str(data[row]))
		f.write('\n')

def callKeepaApi ( asin ):
	KEEPA_KEY = "8fdnui1hbe9d62tc5npkmpgkdsaugfoui8ranves3sj5roe3tj1cfj5fggnbqtoo"
	url = 'https://api.keepa.com/product?key=' + KEEPA_KEY + '&domain=1&asin=' + asin
	response = requests.get(url)	
	data = response.json()

	if 'products' in data:
		return data['products'][0]


def convertToDict ( keepa_data_list ):	
	
	res_dict = {}

	isTime = 1
	timevalue = 0 
	for element in keepa_data_list:
		if isTime == 1:
			timevalue = element
			isTime = 0
		else:
			unixTime = (timevalue+21564000)*60
			res_dict[unixTime] = element
			isTime = 1

	return res_dict

pp = pprint.PrettyPrinter(indent=4)

asins = ['B01IWIBKGE', 'B0002IJXDA', 'B00E24BM2U', 'B002EJC990', 'B002LLVFK0']
for asin in asins:
	keepa_data = callKeepaApi(asin)

	csv_data = keepa_data['csv']
	del keepa_data['csv']

	csv_fail = {}

	cnt = 0
	for dataList in csv_data:
		if not dataList:
			csv_fail[cnt] = dataList
		else:
			filename = "./output/" + str(asin) + "_output_" + str(cnt) + ".csv"
			print(str(cnt) + ") " + str(len(dataList)) + "   -- " + filename)
			data = convertToDict(dataList)
			# pp.pprint(data)
			writeDictToCSV(filename, data)
		cnt += 1

	f = open("./output/" + str(asin) + 'output_details.txt', 'w')
	f.write(str(keepa_data))
	f.write("--------------------------")
	f.write("failed csv")
	f.write(str(csv_fail))


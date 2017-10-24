# # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

NUM_OF_CHANNELS = 16
#FILE_DIR = "/Users/Hanlin/Desktop/DLA/myproject/data/f.txt"
FILE_DIR = "/home/pi/myproject/data.txt"
CACHE = [] # List[str] of length 16, one string for each channel
DEBUG = True

#################################### WebApp functions ###################################

def visual(request):

	channels = toWaveDormData(readFile())
	context = {"channels": channels, "button_num": range(1,NUM_OF_CHANNELS + 1)}
	return render(request, "dlaApp/visual.html", context)

##################################### Backend Data Processing ############################

# convert data of format 111000110 to WaveDorm specific format 1..0..1.0 
def toWaveDormData(chanData):
	# type: List(List(str)) -> List(str)

	newData = []
	for i in range(len(chanData)):
		dataLst = chanData[i]

		prevStr = dataLst[0]
		newStr = dataLst[0]
		for index in range(1, len(dataLst)):
			thisBit = dataLst[index]
			if thisBit == prevStr:
				newStr += "."
			else:
				newStr += thisBit
				prevStr = thisBit

		newData.append(newStr)
	CACHE = newData
	return newData

# read most recent data from file and store in cache
def readFile():
	# type: () -> List(List(str))

	chanData = []
	with open(FILE_DIR, 'r') as f:
		timeData = f.read()
		f.close()

	for i in range(NUM_OF_CHANNELS):
		lst = []
		j = i
		while j < len(timeData):
			lst.append(timeData[j])
			j += NUM_OF_CHANNELS	
		chanData.append(lst)

		

	if DEBUG:
		if (len(timeData) % 16) != 0:
			print("data length is not divisible by 16")
	return chanData


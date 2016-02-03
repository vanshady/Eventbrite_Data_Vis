#############################################################################################

# Python script for the following tasks: 
# 1. Get the different format types from the Eventbrite JSON API
# 2. Create a dictionary to store the values of the formatIDs for all the events on Eventbrite
# 3. Generate a JSON file which will be the input to the bubble chart D3 rendering 

# Author: Ashwin Tumma <ashwin.tumma@stonybrook.edu>
# Date: March 20, 2015

# Modified by: Minwei Xu <faceswilliam@gmail.com>
# Date: Feb 2, 2016

# Central Idea: 
# -------------
# We have already obtained the data for the events' formatID using a separate python file, and 
# have the data available in data.csv file. We will be using the formatID value
# from this file. 

# Usage: 
# ----------
# $ python GetFormatStatistics.py 
# The output of this program will be a file named - format.json which will contain 
# all the data points encoded in the formatID value

#############################################################################################

import urllib2
import json

# The token mentioned in the URL is the token which I got generated from the Eventbrite API User Interface
# For security purposes I have masked the token with all Xs in the published version of this Python code, 
# but you can get yours generated similary from Eventbrite's Generate Token Page.

token = ""
response = urllib2.urlopen('https://www.eventbriteapi.com/v3/formats/?token='+token)
data = json.load(response)

formats = data['formats']


formatDict = {}
formatNamesDict = {}
formatLongNamesDict = {}

# Get the values from the JSON API
for k in formats:
	# Initialize the dictionary with the format ids as the key and ZERO as its value
	formatDict[k['id']] = 0;
	print k['short_name']
	formatNamesDict[k['id']] = k['short_name'].strip();
	formatLongNamesDict[k['id']] = k['name'].strip()
	

# Populate the dictionary from the values that we have fetched earlier
pointsFile = open('data.csv')
for line in pointsFile:
	formatID =  line.split(',')[3].strip()
	if formatID.strip() != "None":
		formatDict[formatID] = formatDict.get(formatID) + 1

pointsFile.close()

# Generate a new JSON file to be read by the FormatBubbleChart.html file
jsonOutputFile = open('../../public/json/format.json','wb')
jsonOutputFile.write('{\n "name": "format",\n "children": [\n')

formatDictLen = len(formatDict)
index = 0 
for formatID, size in formatDict.items():	
	jsonOutputFile.write('{"name": "'+formatNamesDict.get(formatID)+'", "longName":"' + formatLongNamesDict.get(formatID)+'", "size":'+str(size)+'}') 
	print index
	if index < formatDictLen -1:
		jsonOutputFile.write(',\n') 
	index+=1

jsonOutputFile.write('\n]}')
jsonOutputFile.close()


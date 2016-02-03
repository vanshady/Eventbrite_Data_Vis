#############################################################################################

# Python script for extracting the values of the start date of the events of Eventbrite

# Author: Ashwin Tumma <ashwin.tumma@stonybrook.edu>
# Date: March 20, 2015

# Central Idea: 
# -------------
# We have already obtained the data for the events' start date using a separate python file, and 
# have the data available in data.csv file. We will be using the start date values 
# from this file. 

# Usage: 
# ----------
# $ python GetDateValues.py 
# The output of this program will be a file named - dateTimeJSON.json which will contain 
# all the data points encoded in the epoch time value format 

#############################################################################################

import time

epochTimeDictionary = {}

pattern = '%Y-%m-%d %H:%M:%S'
pointsFile = open('/public/csv/data.csv')

# Extract the values of the start date from the input file
for line in pointsFile:
	try:
		dateTimeValue = line.split(',')[2]
		if dateTimeValue != "None".strip():

			# Convert the given date time value from its format to UNIX epoch time
			# We convert the timestamp value to epoch time, because cal-heatmap.js expects data 
			# in the UNIX epoch time value format.
			dateTimeValue = dateTimeValue.replace("T"," ")
			print dateTimeValue
			epoch = int(time.mktime(time.strptime(dateTimeValue.strip(), pattern)))
			
			if epoch in epochTimeDictionary: 
				epochTimeDictionary[epoch] = epochTimeDictionary.get(epoch) + 1
			else: 
				epochTimeDictionary[epoch] = 1
	except:
		continue


pointsFile.close()

# Start writing data to the output JSON file
jsonOutputFile = open('/public/json/dateTimeJSON.json','wb')
jsonOutputFile.write("{") 

for epochTime, value in epochTimeDictionary.items():
	jsonOutputFile.write('"'+str(epochTime)+'":'+str(value)+',')

jsonOutputFile.write('"0":0 }')
jsonOutputFile.close()


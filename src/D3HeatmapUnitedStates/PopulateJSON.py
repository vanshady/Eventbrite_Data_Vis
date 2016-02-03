#############################################################################################

# Python script for reading the data from the data points text file and populating the JSON
# file with the required data and its required format.

# Author: Ashwin Tumma <ashwin.tumma@stonybrook.edu>
# Date: March 18, 2015

# Modified by: Minwei Xu <faceswilliam@gmail.com>
# Date: Feb 2, 2016

#############################################################################################
import os

# Create a new us.json file for this session, and copy the SVG section from the template file
os.system('cp us.json.template us.json')

# Open the file containing the US states data
fp = open('state.csv')
jsonFile = open('../../public/json/us.json','a+')

index = 1 
for line in fp: 
	jsonFile.write('{"label": "'+line.split(":")[0].strip()+'","value" : '+ line.split(",")[1].strip() + '}' )
	if index <= 49: 
		jsonFile.write(' , \n')
	index+=1

fp.close()

# Write the terminating brackets
jsonFile.write("\n ] } ")
jsonFile.close()

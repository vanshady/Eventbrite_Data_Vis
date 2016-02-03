#############################################################################################

# Python script for fetching the "region" data from the Eventbrite JSON API and 
# counting the number of occurences for events in each state of the United States.
# 
# I have focused on the data from United States only for greater representational purpose.
# Similar exercise and codes can be written for analysis of data throughout the globe

# Author: Ashwin Tumma <ashwin.tumma@stonybrook.edu>
# Date: March 18, 2015

# Central Idea: 
# -------------
# The address of each event is encoded in the JSON string for the event. It is readily accessible 
# through [events].[venue] value. There are fine grained and coarse grained address values available
# for the events. But for our purposes we will be working with the coarse grained address values, 
# which is the state in which the event has/ will occur. 
# The value for the State is encoded in [events][address][region] value, but before accessing that, 
# as mentioned in the above comments, we will be using regions only from the United States, so for this 
# reason, we filter the values based on country as well [events][address][country] = "US" (for United States)

# Usage: 
# ----------
# $ python GetStatesCounters.py > DataPoints.txt
# The output of this program is redirected to the DataPoints.txt file

# Alternatives for usage: 
# ------------------
# I chose to redirect the output of this program to a text file from commmand line, to avoid 
# increasing lines of code in this file. But having said that, alternatively, we can also write the 
# data to a file mentioned by the user at command line. 

#############################################################################################

import urllib2
import json

# Create a dictionary for each state in the United States based on its code, and initialize
# the value of each one of them to ZERO.

statesDictionary = {
'AL':0,'AK':0,'AZ':0,'AR':0,'CA':0,'CO':0,'CT':0,'DE':0,'FL':0,'GA':0,'HI':0,'ID':0,'IL':0,'IN':0,'IA':0,'KS':0,'KY':0,'LA':0,'ME':0,'MD':0,'MA':0,'MI':0,'MN':0,'MS':0,'MO':0,'MT':0,'NE':0,'NV':0,'NH':0,'NJ':0,'NM':0,'NY':0,'NC':0,'ND':0,'OH':0,'OK':0,'OR':0,'PA':0,'RI':0,'SC':0,'SD':0,'TN':0,'TX':0,'UT':0,'VT':0,'VA':0,'WA':0,'WV':0,'WI':0,'WY':0
}

token = ""
# 500 was the page count (with each page having 50 entries) on the day this script was written
for page in range(1, 500):

	# The token mentioned in the URL is the token which I got generated from the Eventbrite API User Interface
	# For security purposes I hide the token in the published version of this Python code, 
	# but you can get yours generated similary from Eventbrite's Generate Token Page.
        response = requests.get(
            "https://www.eventbriteapi.com/v3/events/search/?token=" + token + "&page=" + str(page),
            headers = {
                "Authorization": "Bearer " + token,
            },
            verify = True,  # Verify SSL certificate
        ).json()
        events = response['events']

        for k in events:
		try:
			if k['venue_id'] is None:
				continue
			else:
                venue = requests.get(
                    "https://www.eventbriteapi.com/v3/venues/"+k['venue_id']+"/?token=" + token,
                    headers = {
                        "Authorization": "Bearer " + token,
                    },
                    verify = True,  # Verify SSL certificate
                ).json()
                
				if venue['address']['country'] == "US":
					# Increment the value of that particular state
					state = venue['address']['region']
					if venue['address']['region'] is not None and state is not None and state in statesDictionary: 
						statesDictionary[state] = statesDictionary.get(state) + 1
                
                time.sleep(3) # Wait 3 seconds to avoid blocking
        except KeyError:
            print "BLOCKED"                     

print "Printing the state and its values"
for state,value in statesDictionary.items():
	# Use foutput.write, if the output was supposed to be written to a file directly from the program code.
	print str(state)+","+str(value)

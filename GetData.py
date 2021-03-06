import requests
import json
import time

dataFile = open('./public/csv/data.csv', 'a')

token = ""

s = ""
for page in range(1, 500):
    print "Page ",page
    response = requests.get(
        "https://www.eventbriteapi.com/v3/events/search/?token=" + token + "&page=" + str(page),
        headers = {
            "Authorization": "Bearer " + token,
        },
        verify = True,  # Verify SSL certificate
    ).json()
    events = response['events']
    
    for k in events: 
        if k['venue_id'] is None:
            continue	
        else:
            try:
                venue = requests.get(
                    "https://www.eventbriteapi.com/v3/venues/"+k['venue_id']+"/?token=" + token,
                    headers = {
                        "Authorization": "Bearer " + token,
                    },
                    verify = True,  # Verify SSL certificate
                ).json()
                
                dataFile.write(venue['latitude'] + "," + venue['longitude'] + "\n" + "," + str(k['start']['local']) + "," + str(k['format_id']) + "\n")
                time.sleep(3) # Wait 3 seconds to avoid blocking
            except KeyError:
                print "BLOCKED:  Venue_id " + str(k[venue_id]) + " Page: "+ str(page) + "\n"                     
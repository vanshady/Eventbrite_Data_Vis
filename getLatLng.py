import requests
import json
import pprint
import string
LatLngFile = open('LatLng.csv', 'wb')

token = "3MRZ7UXGZUXFX7EYSQ5K"

for line in open('events.json', 'r'):
    start = 0
    print string.find(line, "venue_id", start)


# for k in events: 
#     if k['venue_id'] is None:
#         continue	
#     else:
#         print k["venue_id"]
#         venue = requests.get(
#             "https://www.eventbriteapi.com/v3/venues/"+k['venue_id']+"/?token=" + token,
#             headers = {
#                 "Authorization": "Bearer " + token,
#             },
#             verify = True,  # Verify SSL certificate
#         ).json()
        
#         s += venue['latitude'] + "," + venue['longitude'] + "," + str(k['start']['local']) + "," + str(k['format_id']) + "\n"
    
# LatLngFile.write(s)
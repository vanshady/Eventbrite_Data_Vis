This directory contains all the codes (Python, D3, jQuery) which were used for data visualizations of this project. Refer the README.md files for each of the directory to learn more about the visualizations and details about the source code along with steps for execution.


#####DIRECTORIES
* GoogleMapsAPIHeatmap : Heatmap of geographical location of events across the world (with integration to Google Maps)  
* D3HeatmapUnitedStates :  Heatmap of count of events in the United States (using D3.js)
* FormatDataRepresentation : Bubble Chart showcasing the different types/ formats of events that occur on Eventbrite (using D3.js).
* CalendarHeatmap : Calendar Heatmap representing the heatmap of dates for the events on Eventbrite (using D3.js).

##### FILES
* GetEventBriteData.py: Get location, date and formatID data from the APIs that are exposed by Eventbrite API interface.



##### Usage
To update data
```
$ python GetEventBriteData.py
```
This will create a file named `data.csv` in the current directory, and 

##### Notes
The Eventbrite token used for fetching the data is private to me, so I have masked the token using Xs. You can generate your own token using the API provided by EventBrite at [this](http://www.eventbriteapi.com) link.
 

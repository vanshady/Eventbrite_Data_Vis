# Eventbrite Data Visualizations
This repository contains data analysis and visualization of data from [Eventbrite](https://www.eventbrite.com/). The data required for these optimizations is obtained from the API provided by [Eventbrite API](http://eventbriteapi.com/). 

# Demos
Please have a look at the [DEMO](https://eventbrite-data-vis.herokuapp.com/index.html). 

#### Development Platforms and Languages
Python, [D3.js](http://d3js.org/), [Google Maps API v3](https://developers.google.com/maps/), jQuery

#### Author
[Minwei Xu](http://mwxu.me)   
Computer Science Undergraduate Student,  
UC Davis

This repository is modified from [Ashwin Tumma's](https://sites.google.com/site/ashwintumma23) version

#### License
GNU GPL v2

#### Visualizations
This section lists the various visualizations that are developed for this project
* Heatmap of geographical location of events across the world (with integration to Google Maps)
* Heatmap of count of events in the United States (using D3.js)
* Bubble Chart showcasing the different types/ formats of events that occur on Eventbrite (using D3.js).
* Calendar Heatmap showing the heatmap according to the dates of the events (using D3.js)

Heatmap of Geographical Location of Events across the world (Google Maps API)
================================================================================
In this visualization, the geographical location of Eventbrite events is plotted on the global map. Google Maps API is used, so the values for the location are encoded as the `latitude` and `longitude` values of the location. We leverage the power of Google Maps to zoom in and zoom out to have a closer look into any geogprahical location in the world.

###### DEMO
[Google Heatmap](https://eventbrite-data-vis.herokuapp.com/googleheatmap)

###### Code Details: 
* Source Code Directory: `GoogleHeatmap` (Read the README.md file in the corresponding directory)

* References: Google maps API code samples from Google Developers [website](https://developers.google.com/maps/).

Following figure shows the screenshot of the data visualization looking from the global perspective
 ![My image](https://github.com/vanshady/Eventbrite_Data_Vis/blob/master/images/GMapFull.png)
  
While, the next figure shows the screenshot of the event location plots for United States:
![My image](https://github.com/vanshady/Eventbrite_Data_Vis/blob/master/images/UnitedStates.png)

Heatmap of count of events in the United States (using D3.js)
================================================================================
In this data visualization, we create a heatmap of the states in the United States of America indicating the number of events which have occured/ will occur in that particular state. The heatmap allows us to have a glance of the event distribution, while on hovering the mouse over the state, the count of the events in that state are displayed.

###### DEMO
[D3 Heatmap](https://eventbrite-data-vis.herokuapp.com/d3heatmap)

###### Code Details: 
* Source Code Directory: `D3HeatmapUnitedStates` (Read the README.md file in the corresponding directory)

* References: DataMaps - Open Source code for creating maps [website](http://datamaps.github.io/).  
Tipsy [Website](http://bl.ocks.org/ilyabo/1373263) - For displaying tips on mouse hover

Following figure shows the screenshot of distributions of events based on their count in the United States
 ![My image](https://github.com/vanshady/Eventbrite_Data_Vis/blob/master/images/D3Maps.png)
  
================================================================================  
##### Bubble Chart showcasing the different types/ formats of events that occur on Eventbrite (using D3.js)
This is a simple visualization showcasing the weight of the formats of the events on Eventbrite globally. On the event of hovering the mouse over the bubble, shows a detailed description of the format, and also its count.

###### DEMO
[Bubble Chart](https://eventbrite-data-vis.herokuapp.com/bubble)

###### Code Details: 
* Source Code Directory: `FormatDataRepresentation` (Read the README.md file in the corresponding directory)

* References: Bubble Charts D3 [Website](http://bl.ocks.org/mbostock/4063269) - For displaying the bubbles

Following figure shows the screenshot of distributions of events based on their formats
 ![My image](https://github.com/vanshady/Eventbrite_Data_Vis/blob/master/images/BubbleChart.png)

================================================================================    
##### Calendar Heatmap of Eventbrite events shown according to the dates (using D3.js)
In this data visualization we construct a calendar, and then map the events to its particular date. This heatmap representation shows us at a single glance which date or month has the highest concentration of events.

###### DEMO
[Calendar Heatmap](https://eventbrite-data-vis.herokuapp.com/calendar)

###### Code Details: 
* Source Code Directory: `CalendarHeatMap` (Read the README.md file in the corresponding directory)

* References: Calendar Heatmap D3 [Website](http://kamisama.github.io/cal-heatmap/) - For displaying the calendar heatmap

Following figure shows the screenshot of distributions of events based on their start date
 ![My image](https://github.com/vanshady/Eventbrite_Data_Vis/blob/master/images/CalendarJune.png)
  
#### Possible Enhancements
We need to figure out how to scrawl data more efficiently because for each venue_id, we have to make a new request, which may trigger the rate limit on our account.
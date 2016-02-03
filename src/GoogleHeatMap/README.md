In this data visualization, we see the distribution of Eventbrite events for the entire globe. Eventbrite's data is accessible through their JSON API. This visualization makes use of the same API to query and get the data related to the all the locations throughout the world. 

### Features
This section enlists the features of the Google Maps heatmap data visualization. 
* Displays the data for the all the regions of the world at once.
* Leverages the aesthetic features of the Google Maps API and also allows us to zoom in and zoom out with respect to a particular geographical location (See screenshots below).
* The darker the heat in a particular region, more the number of events that were held in that region and vice versa.
* Data is extracted from 194,885 region (latitude and longitude) values.

### Files
This section provides a brief description of the all the files and their purpose in this directory. 
* `CreateHeatmap.py`: Python script for creating the HTML file which contains the data points for event location. The data visualization format we will be leveraging in this code is of Google Maps API version 3. (See file header  comments for detailed description and elaborate comments).
* `GoogleHeatmap.html`: HTML5 code for rendering the Javascript heatmap in the browser
* `data.csv`: Text file containing the latitude and the longitude values of the events held. This file is prepared using the `GetData.py` Python script.
* `REAME.md:` This file
* `HeatmapTemplate.html`: Template header HTML file used by `CreateHeatmap.py` to create the `GoogleHeatmap.html` file.

### Code References
* Google maps API code samples from Google Developers [website](https://developers.google.com/maps/).

### Screenshots 
Following figure shows the screenshot of the data visualization looking from the global perspective
 ![My image](https://github.com/vanshady/Eventbrite_Data_Vis/blob/master/Images/GMapFull.png)
  
While, the next figure shows the screenshot of the event location plots for United States:
![My image](https://github.com/vanshady/Eventbrite_Data_Vis/blob/master/Images/UnitedStates.png)
 
### Other Enhancements: 
 This section lists some of the enhancements that are possible for in this data visualization. 
 * Explore how Google Maps API can be used for creating a pin when the map is zoomed to a more fine granular context. 
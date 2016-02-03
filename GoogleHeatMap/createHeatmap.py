# HTML Header information
template = open('heatmapTemplate.html','r')
heatmapFile = open('./public/heatmap.html','wb')
search = 'var eventsData'

for line in template:
    heatmapFile.write(line)
    if (search in line):
        # Start writing the data points value to the output file
        eventsFormattedcsv = open('LatLng.csv')
        heatmapFile.write("\n")
        for line in eventsFormattedcsv: 
            heatmapFile.write("\t\t\tnew google.maps.LatLng("+line.split(',')[0]+","+line.split(',')[1]+"),\n")
        eventsFormattedcsv.close()

template.close()
heatmapFile.close()

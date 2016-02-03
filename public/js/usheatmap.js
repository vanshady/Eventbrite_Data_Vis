// JavaScript file for Building the United States map and displaying data over the same

function buildMap(data){
 
    var width = 800,
        height = 600,
    projection, path,
    svg, g, mapColor,
    values = {};
 
    data.heatmap.forEach(function(state){
        values[state.label] = state.value;
    });


    projection = d3.geo.albersUsa()
            .scale(width)
            .translate([0, 0]);
 
    path = d3.geo.path()
            .projection(projection);
 
    svg = d3.select(document.getElementById('map')).append('svg')
            .attr('width', width)
            .attr('height', height); // lets leave a space for 'legend'

 
    g = svg.append('g')
            .attr('transform', 'translate(' + width / 2.5 + ',' + height / 2 + ')')
            .attr('height', height)
            .append('g')
            .attr('class','states');
 
    mapColor = d3.scale.linear()
            .domain([0,d3.max(data.states, function(d) {
                return Math.log(values[d.properties.abbr] || 1);
            })])
            .interpolate(d3.interpolateRgb)
            .range(['#FFCCCC', '#FF0000']);
 
    g.selectAll('path')
            .data(data.states)
            .enter()
            .append('path')
            .attr('d', path)
            .attr('id', function(d) { return d.properties.abbr; })
            .style('fill', function(d) { return mapColor(Math.log(values[d.properties.abbr] || 1)); });
 
    g.selectAll('text')
            .data(data.states)
            .enter()
            .append('text')
            .attr('transform', function(d) { return 'translate(' + path.centroid(d) + ')'; })
            .attr('id', function(d) { return 'label-'+d.properties.abbr ; })
            .attr('dy', '.35em')
            .text(function(d) { return d.properties.abbr; });

      // Integration of Tipsy for rendering of state count values
      $('svg path').tipsy({ 
        gravity: 'w', 
        html: true, 
        title: function() {
          return this.__data__.properties.name + ': ' + values[this.__data__.properties.abbr]; 
        }
      });

      $('svg text').tipsy({ 
        gravity: 'w', 
        html: true, 
        title: function() {
          return this.__data__.properties.name + ': ' + values[this.__data__.properties.abbr]; 
        }
      });
}
 
$.getJSON("us.json", function(data) {
    buildMap(data);
});


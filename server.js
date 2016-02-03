
var express = require('express'),
    app = express();
    path = require("path");

// all environments  
app.set('port', process.env.PORT || 3000); 

app.use(express.static(path.join(__dirname, 'public')));  
app.use("/public", express.static(path.join(__dirname, 'public')));

__dirname += '/public/'  

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname+'/GoogleHeatmap.html'));
});

app.get('/googleheatmap', function (req, res) {
    res.sendFile(path.join(__dirname+'/GoogleHeatmap.html'));
});

app.get('/d3heatmap', function (req, res) {
    res.sendFile(path.join(__dirname+'/D3Heatmap.html'));
});

app.get('/bubble', function (req, res) {
    res.sendFile(path.join(__dirname+'/FormatBubbleChart.html'));
});

app.get('/calendar', function (req, res) {
    res.sendFile(path.join(__dirname+'/CalendarHeatmap.html'));
});

var port = process.env.PORT || 3000;
app.listen(port);
console.log('listening at:', port);

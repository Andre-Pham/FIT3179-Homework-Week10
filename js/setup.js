var areachart = "js/areachart.json";
vegaEmbed('#areachart', areachart, { "actions": false }).then(function(result) { })
    .catch(console.error);

var map = "js/map.json";
vegaEmbed('#map', map, { "actions": false }).then(function(result) { })
    .catch(console.error);
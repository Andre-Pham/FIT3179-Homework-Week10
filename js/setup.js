var areachart = "js/areachart.json";
vegaEmbed('#areachart', areachart).then(function(result) { })
    .catch(console.error);

var map = "js/map.json";
vegaEmbed('#map', map).then(function(result) { })
    .catch(console.error);
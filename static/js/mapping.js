//Function to create the map 
function createMap(snowStations) {

  // Create the tile layer for the background of the map
  let satmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.satellite",
    accessToken: API_KEY
  });

  console.log(satmap);

  // Create a baseMaps object to hold the tile layer
  let baseMaps = {
    "Satellite Map": satmap
  };

  // Create an overlayMaps object to hold the snowStations layer
  let overlayMaps = {
    "Measurement Stations": snowStations
  };

  // Create the map object with options
  const myMap = L.map("map", {
    center: [41.5516759, -111.3655038],
    zoom: 5,
    layers: [satmap, snowStations]
  });

  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);
}

//Collect data from flask and to create markers and popups
function createMarkers(stations) {
  
  console.log(stations);

  // Initialize an array to hold station markers
  let stationMarkers = stations.map(station => {
    return L.marker([station.Latitude, station.Longitude])
      .bindPopup("<h3>Station: " + station.StationName + "<h3><h3>Elevation: " + station.Elevation + "<h3>")
  });

  console.log(stationMarkers);

  // Create a layer group made from the station markers array, pass it into the createMap function
  createMap(L.layerGroup(stationMarkers));
}

// Perform an API call to the Flask app to get station information. Call createMarkers when complete
d3.json(`/stations`, createMarkers);

/*
var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([51.5, -0.09]).addTo(map)
    .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
    .openPopup();
*/
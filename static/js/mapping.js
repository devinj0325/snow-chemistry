//Function to create the map 
function createMap(snowStations) {

  // Create the tile layer for the background of the map
  let satmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.satellite",
    accessToken: API_KEY
  });

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
function createMarkers(response) {
  
  console.log(response);
  // Pull the "stations" property off of the response, rename for readability
  let stations = response;

  // Initialize an array to hold station markers
  let stationMarkers = [];

  // Loop through the stations array
  for (let index = 0; index < stations.length; index++) {
    let station = stations[index];

    // For each station, create a marker and bind a popup with the station's name
    let stationMarker = L.marker([station.Latitude, station.Longitude])
      .bindPopup("<h3>Station: " + station.StationName + "<h3><h3>Elevation: " + station.Elevation + "<h3>");

    // Add the marker to the stationMarkers array
    stationMarkers.push(stationMarker);
  };

  // Create a layer group made from the station markers array, pass it into the createMap function
  createMap(L.layerGroup(stationMarkers));
}

// Perform an API call to the Flask app to get station information. Call createMarkers when complete
d3.json(`/stations`, createMarkers);

//Create map
const myMap = L.map("map", {
  center: [41.5516759, -111.3655038],
  zoom: 5
});


L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.satellite",
  accessToken: API_KEY
}).addTo(myMap);

// An array containing each city's name, location, and population
var cities = [{
  location: [48.51805556, -114.02],
  name: "APGAR LOOKOUT MT",
  elevation: "5179"
},
{
  location: [36.57277778, -105.4452778],
  name: "TAOS SKI VALLEY NM",
  elevation: "10890"
},

{
  location: [44.3033333, -115.2344444],
  name: "BANNER SUMMIT ID",
  elevation: "7042"
},
{
  location: [48.50805556, -114.345],
  name: "BIG MOUNTAIN MT",
  elevation: "6426"
}
]
// Loop through the cities array and create one marker for each city, bind a popup containing its name and population add it to the map
for (var i = 0; i < cities.length; i++) {
  var city = cities[i];
  L.marker(city.location)
    .bindPopup("<h2>" + city.name + "</h2> <hr> <h3>Elevation: " + city.elevation + "</h3>")
    .addTo(myMap);
}
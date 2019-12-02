// Line graph – Snow depth by station by year

// Set the dimensions of the graph
let svgWidth = 960;
let svgHeight = 500;

// Set margins
let margin = {top: 30, right: 20, bottom: 75, left: 150};

// Define dimensions of the chart area
var chartWidth = svgWidth - margin.left - margin.right;
var chartHeight = svgHeight - margin.top - margin.bottom;

let svg = d3.select('#snowDepthChart')
  .attr('width', svgWidth)
  .attr('height', svgHeight);

// Append a group area, then set its margins
let chartGroup = svg.append("g")
  .attr('transform', `translate(${margin.left}, ${margin.top})`);

// add labels
svg.append('text')
  .attr('x', svgWidth / 2 + margin.left / 2)
  .attr('y', svgHeight - 20)
  .text('Year')
  .classed('chart-label', true);

svg.append('text')
.attr('x', 0)
.attr('y', svgHeight / 2)
.text('Depth (cm)')
.classed('chart-label', true);
  
// Create variable to store all snow data, globally 
let snowData = [];

let renderChart = function(filteredData) {
  
  // Clear chartGroup on svg for rerender
  chartGroup.selectAll("*").remove();
  
  // Configure a scale
  // d3.extent returns an array containing the min and max values for the property specified
  var xLinearScale = d3.scaleLinear()
  .domain(d3.extent(filteredData, data => data['WaterYear']))
  .range([0, chartWidth]);
  
  // Configure a linear scale with a range 
  var yLinearScale = d3.scaleLinear()
  .domain([0, d3.max(filteredData, data => data['Snow_depth'])])
  .range([chartHeight, 0]);
  
  // Create two new functions passing the scales in as arguments
  // These will be used to create the chart's axes
  var bottomAxis = d3.axisBottom(xLinearScale).tickFormat(d3.format("d"));
  var leftAxis = d3.axisLeft(yLinearScale);
  
  // Configure a line function which will plot the x and y coordinates using our scales
  var drawLine = d3.line()
  .x(data => xLinearScale(data['WaterYear']))
  .y(data => yLinearScale(data['Snow_depth']));
  
  // Append an SVG path and plot its points using the line function
  // The drawLine function returns the instructions for creating the line for forceData
  
  chartGroup.append("path")
  .attr("d", drawLine(filteredData))
  .classed("line", true);
  
  // Append an SVG group element to the chartGroup, create the left axis inside of it
  chartGroup.append("g")
  .classed("axis", true)
  .call(leftAxis);
  
  // Append an SVG group element to the chartGroup, create the bottom axis inside of it
  // Translate the bottom axis to the bottom of the page
  chartGroup.append("g")
  .classed("axis", true)
  .attr("transform", `translate(0, ${chartHeight})`)
  .call(bottomAxis);
};
  
// Function for updating chart based on station name
let updateStation = function(stationName) {
  let filteredData = snowData
    .filter(data => data['StationName'] === stationName);
  
  // Renders chart
  renderChart(filteredData);
};

// Use D3 to pull snow depth data from flask app
d3.json('/snow').then(function(jsonData) {
  
  snowData = jsonData;

  // Use D3 tp pull stations from flask app
  d3.json('/stations').then(function(stationData) {
    
    // Select element in html
    let selStation = d3.select('#selStation');

    // Populate options for each station
    stationData.forEach(station => {
      selStation.append('option')
        .attr('value', station['StationName'])
        .text(station['StationName']);

      });
      
    let defaultStationName = stationData[0]['StationName'];
    selStation.node().value = defaultStationName;
    updateStation(defaultStationName);
  });
});
  


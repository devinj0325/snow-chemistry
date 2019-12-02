function buildMetadata(sample) {
    d3.json(`/metadata/${sample}`).then((data) => {
      // Use d3 to select the panel with id of `#sample-metadata`
      var PANEL = d3.select("#sample-metadata");
  
      // Use `.html("") to clear any existing metadata
      PANEL.html("");
  
      // Use `Object.entries` to add each key and value pair to the panel
      // Hint: Inside the loop, you will need to use d3 to append new
      // tags for each key-value in the metadata.
      Object.entries(data).forEach(([key, value]) => {
        PANEL.append("h6").text(`${key}: ${value}`);
      });
  
      // BONUS: Build the Gauge Chart
      buildGauge(data.WFREQ);
    });
  }
  
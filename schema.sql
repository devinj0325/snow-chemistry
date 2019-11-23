CREATE DATABASE snow_chemistry;

	CREATE TABLE snow_data 
	(id SERIAL PRIMARY KEY,
	 StationName VARCHAR,
	 WaterYear INT,
	 pH FLOAT, 
	 Hydrogen VARCHAR,
	 Calcium VARCHAR,
	 Magnesium VARCHAR,
	 Sodium VARCHAR,
	 Potassium VARCHAR,
	 Ammonium VARCHAR,
	 Chloride VARCHAR,
	 Sulfate VARCHAR,
	 Nitrate VARCHAR,
	 Dissolved_organic_carbon VARCHAR,
	 Snow_depth INT
	)
	;
	
	CREATE TABLE stations (
	id SERIAL PRIMARY KEY,
	StationName VARCHAR,
	Latitude FLOAT,
	Longitude FLOAT,
	Elevation INT
	)
	;
# Import dependencies
import pandas as pd
from sqlalchemy import create_engine

# Path to Snow CSV file
snow_data_to_load = "data/data_1993_2018.csv"

# Store Snow CSV into DataFrame
snow_data = pd.read_csv(snow_data_to_load)

# Drop unnecessary columns
filtered_snow_data = snow_data.drop(columns=['SiteNumber', 'SampleDate', 'SampleType', 
'ANC (ueq/L)', 'SC (uS/cm)', 'Total N (mg/L)', 'Total Dissolved N (mg/L)', 
'Hg (ng/L) Roth 1994', 'Hg (ng/L) USEPA 1631', 'd34S (per mil)', 'SWE (cm)', 'Ionic Balance (%)'])

# Determine which stations have 20 or more observations; drop the stations that have fewer than 20 observations
station_count = pd.DataFrame(station_count)
station_count.reset_index(inplace=True)
station_count.rename(columns={"index": "StationName", "StationName": "Station_Count"}, inplace=True)
filtered_snow_data = filtered_snow_data.merge(station_count, on = 'StationName', how = 'left')
filtered_snow_data.dropna(inplace=True)

#Renaming columns for readability
filtered_snow_data.rename(columns={"H (ueq/L)": "Hydrogen", "Ca (ueq/L)": "Calcium", 
"Mg (ueq/L)": "Magnesium", "Na (ueq/L)": "Sodium", "K (ueq/L)": "Potassium", 
"NH4 (ueq/L)": "Ammonium", "Cl (ueq/L)": "Chloride", "SO4 (ueq/L)": "Sulfate", 
"NO3 (ueq/L)": "Nitrate", "DOC (mg/L)": "Dissolved_organic_carbon", "Snow Depth (cm)": "Snow_depth"}, inplace=True)

#Removing Station Count column
final_snow_data = filtered_snow_data.drop(columns=['Station_Count'])

# Connect to local database
engine = create_engine('postgresql://postgres:postgres@localhost:5432/snow_chemistry')


# # Use Pandas To Load CSV converted DataFrame into database
final_snow_data.to_sql(name='snow_data', con=engine, if_exists='replace', index=True, index_label='id')
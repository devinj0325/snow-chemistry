from flask import Flask, request, render_template, jsonify
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

#############
# Flask Setup
#############
app = Flask(__name__)

################
# Database Setup
################
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:postgres:postgres@localhost:5432/snow_chemistry'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
# reflect an existing database into a new model
Base = declarative_base()
# reflect the tables
#Base.prepare(db.engine, reflect=True)

#print(dir(Base.classes))

# Save reference to the table
# test = Base.classes.test
#stations = Base.classes.stations
#snow_data = Base.classes.snow_data
class Station(Base):
      __tablename__ = 'stations'

      id = Column(Float, primary_key=True)
      StationName = Column(String)
      Latitude = Column(Float)
      Longitude = Column(Float)
      Elevation = Column(Float)

class snow_data(Base):
      __tablename__ = 'snow_data'

      id = Column(Float, primary_key=True)
      StationName = Column(String)
      WaterYear = Column(Float)
      pH = Column(Float)
      Hydrogen = Column(String)
      Calcium = Column(String)
      Magnesium = Column(String)
      Sodium = Column(String)
      Potassium = Column(String)
      Ammonium = Column(String)
      Chloride = Column(String)
      Sulfate = Column(String)
      Nitrate = Column(String)
      Dissolved_organic_carbon = Column(String)
      Snow_depth = Column(Float) 
##############
# Flask Routes
##############
@app.route("/")

def index():
  return render_template("templates/index.html")


  
@app.route("/snow")
def snow_chemistry():

    # Use Pandas to perform the sql query
    stmt = db.session.query(snow_data).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[1:])

@app.route("/snowDepth")
def sample_metadata(sample):
    """Return the MetaData for a given sample."""
    sel = [
        snow_data.StationName,
        snow_data.WaterYear,
        snow_data.Snow_depth,
    ]
    results = db.session.query(*sel).filter(snow_data.sample == sample).all()
    print(results)


@app.route("/stations")
def stations():

    # Use Pandas to perform the sql query
    stmt = db.session.query(stations).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[1:])

@app.route("/stationInfo")
def metadata(location):
    """Return the MetaData for a given sample."""
    sel = [
        stations.StationName,
        stations.Latitude,
        stations.Longitude,
        stations.Elevation
    ]
    info = db.session.query(*sel).filter(stations.location == location).all()
    print(info)





if __name__ == "__main__":
  app.run()

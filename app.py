from flask import Flask, request, render_template, jsonify
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
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
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@localhost:5432/snow_chemistry'
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = declarative_base()
# reflect the tables
#Base.prepare(db.engine, reflect=True)

#print(dir(Base.classes))

# Save reference to the table
# test = Base.classes.test
#stations = Base.classes.stations
#snowData = Base.classes.snow_data
class User(Base):
      __tablename__ = 'users'

      id = Column(Integer, primary_key=True)
      StationName = Column(Integer)
      Latitude = Column(Integer)
      Longitude = Column(Integer)
      Elevation = Column(Integer)
      
##############
# Flask Routes
##############
@app.route("/")

def index():
  render_template("index.html")

@app.route("/snow")
def snow_chemistry():

    # Use Pandas to perform the sql query
    stmt = db.session.query(snowData).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[1:])

@app.route("/snowDepth")
def sample_metadata(sample):
    """Return the MetaData for a given sample."""
    sel = [
        snowData.StationName,
        snowData.WaterYear,
        snowData.Snow_depth,
    ]

    results = db.session.query(*sel).filter(snowData.sample == sample).all()



if __name__ == "__main__":
  app.run()

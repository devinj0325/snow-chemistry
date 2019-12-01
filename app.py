from flask import Flask, request, render_template, jsonify
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
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

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Station(db.Model):
    __tablename__ = 'stations'

    id = db.Column(db.Integer, primary_key=True)
    StationName = db.Column(db.String)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    Elevation = db.Column(db.Float)

    def __repr__(self):
        return '<Station %r>' % self.id
    
    def as_dict(self):
        return {
            'id': self.id,
            'StationName': self.StationName,
            'Latitude': self.Latitude,
            'Longitude': self.Longitude,
            'Elevation': self.Elevation
        }

class SnowData(db.Model):
    __tablename__ = 'snow_data'

    id = db.Column(db.Integer, primary_key=True)
    StationName = db.Column(db.String)
    WaterYear = db.Column(db.Float)
    pH = db.Column(db.Float)
    Hydrogen = db.Column(db.String)
    Calcium = db.Column(db.String)
    Magnesium = db.Column(db.String)
    Sodium = db.Column(db.String)
    Potassium = db.Column(db.String)
    Ammonium = db.Column(db.String)
    Chloride = db.Column(db.String)
    Sulfate = db.Column(db.String)
    Nitrate = db.Column(db.String)
    Dissolved_organic_carbon = db.Column(db.String)
    Snow_depth = db.Column(db.Float) 

    def __repr__(self):
        return '<SnowData %r>' % self.id
    
    def as_dict(self):
        return {
            'id': self.id,
            'StationName': self.StationName,
            'WaterYear': self.WaterYear,
            'pH': self.pH,
            'Hydrogen': self.Hydrogen,
            'Calcium': self.Calcium,
            'Magnesium': self.Magnesium,
            'Sodium': self.Sodium,
            'Potassium': self.Potassium,
            'Ammonium': self.Ammonium,
            'Chloride': self.Chloride,
            'Sulfate': self.Sulfate,
            'Nitrate': self.Nitrate,
            'Dissolved_organic_carbon': self.Dissolved_organic_carbon,
            'Snow_depth': self.Snow_depth
        }
    
##############
# Flask Routes
##############
@app.route("/")
def index():
    return template("index")

@app.route("/<string:page>.html")
def template(page):
    return render_template(f"{page}.html")
 
@app.route("/snow")
def snow_chemistry():
    rows = SnowData.query.all()

    # Return a list of the db.Column names (sample names)
    return jsonify([row.as_dict() for row in rows])

@app.route("/stations")
def stations():

    locations = Station.query.all()

    # Return a list of the db.Column names (sample names)
    return jsonify([location.as_dict() for location in locations])

if __name__ == "__main__":
  app.run(debug=True)

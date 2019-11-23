from flask import Flask, request, render_template
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#############
# Flask Setup
#############
app = Flask(__name__)

################
# Database Setup
################
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Noodle07!@localhost:5432/snow_chemistry"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save reference to the table
snowData = Base.classes.snow_data
stations = Base.classes.stations

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
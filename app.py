import numpy as numpy

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify
#########################################################
#create engine
engine=create_engine("sqlite:///hawaii.sqlite")

Base=automap_base()
Base.prepare(engine,reflect=True)

Measurement=Base.classes.Measurement
Stations=Base.classes.Stations

session=Session(engine)
#########################################################
#Flask Setup

app=Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/precipitation<br/>"
        f"/api/stations<br/>"
        f"/api/temperature<br/>"
        f"/api/<start><br/>"
        f"/api/<start>/<end>"

    )

    @app.route("/api/precipitation")
    def Precip():
        """Return the data as a json"""
        return jsonify(Measurement)
    
    @app.route("/api/stations")
    def Station():
        """Return the data for stations as json"""
        return jsonify(Stations)

    @app.route("/api/temperature")
    def Temp():
        """Last year temperature"""
        last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
        last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
        

#


if __name__=="__main__":
    app.run(debug=True)
import numpy as numpy

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/"
    )

#


if __name__=="__main__":
    app.run(debug=True)
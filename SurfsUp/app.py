# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"Replace start and end as the date written in the format YYYY-MM-DD"
    )

## Convert the query results from your precipitation analysis 
## (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create session to query the database
    session = Session(engine)

    # Define the date
    one_year_date = dt.datetime(2017, 8, 23) - dt.timedelta(days=365)

    # Query the Measurement table to get the date and precipitation (prcp) values 
    # for the last 12 months from the defined date
    query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_date).all()

    # Close the session
    session.close()
    
    # Convert the query result into a dictionary (date as key, prcp as value)
    prcp_dict = {date: prcp for date, prcp in query}


    return jsonify(prcp_dict)


## Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
   # Creat session to query the database
    session = Session(engine)

    # Query all station names or ids from the Station model
    results = session.query(Station.station).all()

    # Close the session
    session.close()

    # Unpack the results into a list
    all_stations = list(np.ravel(results))

    # Return the list of stations as a JSON response
    return jsonify(all_stations)


## Query the dates and temperature observations of the most-active station for the previous year of data.
##Return a JSON list of temperature observations for the previous year.

@app.route("/api/v1.0/tobs")
def temperature_observations():
    # Create a session to connect to the database
    session = Session(engine)

    # Calculate the date one year from the current date
    one_year_date = dt.datetime(2017, 8, 23) - dt.timedelta(days=365)

    # Query the dates and temperature observations (tobs) for the most active station (USC00519281) in the last year
    temperature_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= one_year_date).\
        all()

    # Close the session after the query is done
    session.close()

    # Convert the query result into a list of dictionaries (to return as JSON)
    temp_list = [{date: tobs} for date, tobs in temperature_data]

    # Return the temperature data as JSON
    return jsonify(temp_list)


## Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

@app.route("/api/v1.0/<start>")
def start_temp(start):
    # Create a session to query the database
    session = Session(engine)

    # Query to calculate TMIN, TAVG, TMAX for all dates greater than or equal to the start date
    results = session.query(
        func.min(Measurement.tobs), 
        func.avg(Measurement.tobs), 
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start).all()

    # Close the session
    session.close()

    # Extract the results from the query and format them as a dictionary
    temp_data = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    # Return the JSON response
    return jsonify(temp_data)

# Return a JSON list of the minimum temperature, average temperature, and maximum temperature for a start and end date range.
@app.route("/api/v1.0/<start>/<end>")
def start_end_temp(start, end):
    # Create a session to query the database
    session = Session(engine)

    # Query to calculate TMIN, TAVG, TMAX for all dates between the start and end dates (inclusive)
    results = session.query(
        func.min(Measurement.tobs), 
        func.avg(Measurement.tobs), 
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Close the session
    session.close()

    # Extract the results from the query and format them as a dictionary
    temp_data = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    # Return the JSON response
    return jsonify(temp_data)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

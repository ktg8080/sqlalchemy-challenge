# sqlalchemy-challenge

Honolulu Climate Analysis and Flask API

Overview

This project involves conducting a climate analysis on Honolulu, Hawaii, using Python, SQLAlchemy, and Flask. The goal is to explore climate data from a SQLite database, visualize key metrics, and develop a Flask API to serve the results of this analysis. The project is divided into two main parts: data analysis and the creation of a Flask API.

Part 1: Climate Data Analysis

Tools and Libraries

	•	Python, SQLAlchemy, Pandas, and Matplotlib

Steps:

	1.	Database Connection:
	•	Connect to a SQLite database using SQLAlchemy.
	•	Reflect database tables and link them to Python classes.
	•	Create a session to interact with the database.
	2.	Precipitation Analysis:
	•	Find the most recent date in the dataset.
	•	Query and analyze precipitation data for the last 12 months.
	•	Load the data into a Pandas DataFrame and visualize it using Matplotlib.
	•	Print summary statistics of the precipitation data.
	3.	Station Analysis:
	•	Query the total number of weather stations.
	•	Identify the most active stations and analyze their data.
	•	Perform temperature analysis (lowest, highest, and average temperatures) for the most active station.
	•	Query and visualize temperature observations for the previous 12 months.

Part 2: Flask API

A Flask API is created to serve the climate analysis results. The following routes are available:

	1.	/ - Homepage that lists all available routes.
	2.	/api/v1.0/precipitation - Returns the last 12 months of precipitation data as a JSON dictionary.
	3.	/api/v1.0/stations - Returns a JSON list of all weather stations.
	4.	/api/v1.0/tobs - Returns the temperature observations for the most active station for the previous year.
	5.	/api/v1.0/ and /api/v1.0// - Returns the minimum, average, and maximum temperatures for a specified date range.

How to Run

	1.	Clone the repository.
	2.	Install dependencies via requirements.txt.
	3.	Run the climate analysis using the provided Jupyter Notebook (climate_starter.ipynb).
	4.	Start the Flask API to access the results.

 Credits
 
  1. Classwork was used for Part 1. ChatGPT was used in assitance with the classwork for Part 2. 

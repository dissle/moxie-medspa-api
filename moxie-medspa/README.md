--DESCRIPTION--
This is a Restful API project written in Python to connect with a SQL database (PostgreSQL).
At the moment it works with writing json strings to file (in place of db inserts and updates) and reading from json file (db select or fetches)


--REQUIREMENTS--

Python 3.13.1

Modules:
FastAPI (fastapi[standard])
Uvicorn (webserver)
psycopg2 (PostgreSQL database adapter)

Kindly install the above two modules in your project virtual environment

--INFO--

FastAPI doc provides

Start application from the shell with:
$ fastapi dev main.py

If you see any encoding error (UNICODEon starting the app, try below:

$ export PYTHONIOENCODING=utf-8

If server starts successfully,

Visit project url at:
http://localhost:8000 | http://127.0.0.1:8000

Visit documentation url:
http://localhost:8000/docs | http://127.1.1.0:8000/docs

You can test the API functionality at the documentation url above or with your favorite api tester


--HOW IT WORKS--

-Assumptions:
CASE 1: In the case where requests do not require authentication, a medspa ID should be passed as an arg. 
CASE 2: All API calls happen as authenticated requests meaning that the medspa ID is know for an authenticated medspa.
This project assumes CASE 1

In all cases queries params and request body will make use of primary keys i.e. IDs to make make queries so that db can be queried
due to time considerations, this is not implemented yet but rather json read and write to disk have been implemented.

-Important:
The port for the instance of PostgreSQL used for this build is 5433 not the default of 5432. Kindly update db settings to suit your instance.

Test examples below (by using the try it out button):


-Service 

Sample data to create a service in JSON:
Create appointment
{
    "name": "botox",
    "description": "testing",
    "price": 50.00,
    "duration": 8000
}




-Appointment

Sample data to create an appointment in JSON:

{
    "start_time": "2025-03-20 22:04:12",
    "total_duration": 0,
    "total_price": 0,
    "services": [{"name": "botox", "price": 50.00, "duration": 1000}, {"name": "daxxify", "price": 100.00, "duration": 2000}, {"name": "xeomin", "price": 150.00, "duration": 2000}]
}

--TESTS--
Test script
run at console with command below:
$ python test.py

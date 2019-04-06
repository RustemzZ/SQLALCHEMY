
# coding: utf-8

# In[ ]:

from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


# In[ ]:

import numpy as np
import pandas as pd


# In[ ]:

import datetime as dt


# In[ ]:

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func


# In[ ]:

engine = create_engine("sqlite:///hawaii.sqlite")


# In[ ]:

Base = automap_base()
Base.prepare(engine, reflect=True)


# In[ ]:

Base.classes.keys()


# In[ ]:

Measurement = Base.classes.measurement
Station = Base.classes.station


# In[ ]:

session = Session(engine)


# In[ ]:

R = session.query(Measurement.prcp, Measurement.date).    group_by(Measurement.prcp).    order_by((Measurement.date).desc()).all()  
R


# In[ ]:

df = pd.DataFrame(R[:42], columns=['prcp', 'date'])
df.set_index('date', inplace=True, )
df.head(25)


# In[ ]:

df.plot(kind="bar",figsize=(20,3),color='b')

plt.title("Date")

plt.show()


# In[ ]:

results = session.query(Station.station, func.sum(Measurement.tobs)).     filter(Station.station == Measurement.station).     group_by(Station.station).      order_by((func.sum(Measurement.tobs)).desc()).all()
              
results


# In[ ]:

df_1 = pd.DataFrame(results, columns=['station','frequency'])
df_1.set_index('frequency',)
df_1.head(10)


# In[ ]:

df_1.plot(kind="hist",figsize=(20,3),color='b')
plt.show()


# In[ ]:

from flask import Flask, jsonify


# In[ ]:

app = Flask(__name__)


# In[ ]:

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/Precipitation Analysis<br/>"
        f"/api/v1.0/Station Analysis"
        f"/api/v1.0/tobs"
    )


# In[ ]:

@app.route("/api/v1.0/Precipitation Analysis")
def prcp():
    """Precipitation Analysis"""
    
    R = session.query(Measurement.prcp, Measurement.date).    group_by(Measurement.prcp).    order_by((Measurement.date).desc()).all()
    
    return jsonify(R)


# In[ ]:




# In[ ]:




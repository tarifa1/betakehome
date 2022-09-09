import os
import pandas as pd
from sqlalchemy import create_engine
from project import Equipment, Events, Locations, Waybills

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
engine = create_engine(SQLALCHEMY_DATABASE_URI)

def ingest_csv(filename, table):
    file = f'/usr/src/app/project/data/{filename}'
    df = pd.read_csv(file)
    df.to_sql(con=engine, name=table.__tablename__, if_exists='replace')

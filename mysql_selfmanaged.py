##import SQLalchemy and pa
from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME")
MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

#Create the engine
engine = create_engine(f'mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}')

#define a query
query = """SELECT * FROM test_EMR.patients;"""

#read the query into a dataframe
df = pd.read_sql(query, con=engine)
df
#prepare a table to upload a dataframe to a mysql table
test_df = pd.read_csv('patients.csv')
test_df_small = test_df.head(10)

#upload to the database
test_df_small.to_sql('patients', con=engine, if_exists='replace')
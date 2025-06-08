import pandas as pd
from sqlalchemy import create_engine

mysql_engine = create_engine('mysql+pymysql://admin:Vijay231199@mysqldb.c4xww0e6m7au.us-east-1.rds.amazonaws.com:3306/aws_demo_db')

def read_from_mysql():
    query = """select * from flights where status = 'On Time' """
    df = pd.read_sql(query, mysql_engine)
    print(df)

    # write this sql table to db
    df.to_sql("flights_ontime", mysql_engine, index=False, if_exists='replace')

read_from_mysql()




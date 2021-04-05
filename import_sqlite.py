import sqlite3
from sqlalchemy import create_engine
from configparser import ConfigParser
import os
import re
import pandas as pd
import sys


def create_connection(sqlite_db_file):
    """
    Reading configuration file to set up the parameters needed 
    Creating a connection to a SQLite database 
    """
    try:
        connection_db = sqlite3.connect(sqlite_db_file)
        return connection_db
    except Exception:
        pass 
    

def create_table_from_csv (sqlite_db_file):
    """
    Import csv files with coma separator (change only if layout differs) from current working directory
    """
    files = [f for f in os.listdir(os.curdir) if f.endswith(".csv")]
    name_df = [re.findall('(.*)\.csv',f)[0] for f in files ]
    engine = create_engine('sqlite:///' + sqlite_db_file)
    for n, f_n in zip(name_df, files):
        try:
            df = pd.read_csv(f"{f_n}", sep=',')
            df.to_sql(f"{n}", engine, if_exists="fail")

        except Exception:
            pass

if __name__ == '__main__':

    #Enter database name 
    database_name = str(sys.argv[1])
    #creating connection and database in current working directory
    connection_db = create_connection(f"{database_name}.db")
    
    create_table_from_csv(f"{database_name}.db")
    connection_db.close()
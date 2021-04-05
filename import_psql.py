import psycopg2 as dbpsql
from configparser import ConfigParser
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
import re
import pandas as pd
from sqlalchemy import create_engine

def create_connection_from_info_file(file) :
    """
    Reading configuration file to set up the parameters needed 
    """
    con_psql_info = ConfigParser()
    con_psql_info.read(file)
    elements_con = {k:v for k, v in con_psql_info.items('postgresql')}
    user, password, database_name = elements_con['user'], elements_con['password'], elements_con['database']
    connection_db = dbpsql.connect(f"user={user} password={password}")
    return connection_db, database_name
    

def create_database (db_cursor, database_name):    
    """
    Creating database (database name specified in the configuration file)
    """
    try:
        db_creating = 'create database ' + database_name + ' ;'
        db_cursor.execute(db_creating)
    except Exception:
        pass

def create_table_from_csv (database_name):
    """
    Import csv files with coma separator (change only if layout differs) from current working directory
    """
    files = [f for f in os.listdir(os.curdir) if f.endswith(".csv")]
    name_df = [re.findall('(.*)\.csv',f)[0] for f in files ]
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/'+ database_name)

    for n, f_n in zip(name_df, files):
        try:
            df = pd.read_csv(f"{f_n}", sep=',')
            df.to_sql(f"{n}", engine, if_exists="fail")

        except Exception:
            pass
      
if __name__ == "__main__":
    
    connection_db,database_name = create_connection_from_info_file(''.join([f for f in os.listdir(os.curdir) if f.endswith('.cfg')]))
    #connection with autocommit
    connection_db.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    #creating cursor to execute query statements.
    db_cursor = connection_db.cursor()
    create_database(db_cursor, database_name)
    create_table_from_csv (database_name)
    connection_db.close()
    db_cursor.close()
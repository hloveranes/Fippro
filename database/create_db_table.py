import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from database.config import config


def create_database():
  conn = None
  try:
    # read the connection parameters
    params = config()
    # format params in string obtained in config
    new_str = ""
    new_str = "host=%s "%params['host']
    new_str += "user=%s "%params['user']
    new_str += "password=%s"%params['password']
    # Connect to PostgreSQL DBMS
    conn = psycopg2.connect(new_str)
    # conn = psycopg2.connect(host=params['host'],user=params['user'],password=params['password'])

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Obtain a DB Cursor
    cursor = conn.cursor()
    # Obtain database name in config
    name_Database = params['database']
    # Create table statement
    sqlCreateDatabase = "create database "+name_Database+";"
    # Create a table in PostgreSQL database
    cursor.execute(sqlCreateDatabase)
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()


def create_tables(query):
  """ create tables in the PostgreSQL database """
  commands = query
  conn = None
  try:
    # read the connection parameters
    params = config()
    # connect to the PostgreSQL server
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    # create table one by one
    for command in commands:
      cur.execute(command)
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()

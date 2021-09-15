import psycopg2
from database.config import config

# supported list, array, tupples
# remove 1st and last character then replace '(quote) with "(quote)
def string_formatter(string=None):
    # remove character in first & last position
    res = str(string)[1:-1]
    # replace ' character with " 
    res = res.replace('\'', '"')

    return res

# supported dict
# strip dictionary values and format to single '(quote) string
def dict_formatter(kwargs=None):
    res = ''
    for args in kwargs.values():
        res += "\'" + args + "\'" + ","
    # remove last character ,
    res = res[:-1]
    return res


def insert_data(table_name, columns, contents):
    """ insert a new record into the table """
    
    conn = None
    row = None

    # get contents length
    cont_length = len(contents)
    for x in range(0, cont_length):
        data_val = dict_formatter(contents[x])

        # construct sql
        sql = """INSERT INTO """ + table_name + """ (""" + string_formatter(columns) + """) VALUES (""" + data_val + """) RETURNING *;"""

        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql)
            # get the generated id back
            row = cur.fetchall()
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if conn is not None:
                conn.close()

    return row


def update_data(id, table_name):
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # Executing a SQL query to update table
        update_query = """Update """+table_name+""" set price = 1500 where id = {}""".format(id)
        cur.execute(update_query)
        # committing our changes to the database
        conn.commit()
        count = cur.rowcount
        print(count, "Record updated successfully ")
        # Fetch result
        cur.execute("SELECT * from {}".format(str(table_name)))
        print("Result ", cur.fetchall())
        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if conn is not None:
            conn.close()


def update_in_bulk(id, table_name):
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # Executing a SQL query to update table
        update_query = """Update """+table_name+""" set price = 1500 where id = {}""".format(id)
        cur.executemany(update_query)
        # committing our changes to the database
        conn.commit()
        count = cur.rowcount
        print(count, "Record updated successfully ")
        # Fetch result
        cur.execute("SELECT * from {}".format(str(table_name)))
        print("Result ", cur.fetchall())
        # close communication with the database
        cur.close()

        
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if conn is not None:
            conn.close()


# delete single item
def delete_data(id, table_name):
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # Executing a SQL query to delete table
        delete_query = """Delete from """+table_name+""" where id = {}""".format(id)
        # execute the DELETE statement
        cur.execute(delete_query)
        # committing our changes to the database
        conn.commit()
        count = cur.rowcount
        print(count, "Record deleted successfully ")
        # Fetch result
        cur.execute("SELECT * from {}".format(str(table_name)))
        print("Result ", cur.fetchall())
        
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if conn is not None:
            conn.close()


def delete_in_bulk(records, table_name):
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        delete_query = """Delete from """+table_name+""" where id = %s"""
        # execute the DELETE many statement
        cur.executemany(delete_query, records)
        # committing our changes to the database
        conn.commit()
        row_count = cur.rowcount
        print(row_count, "Record Deleted")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")


from database.create_db_table import create_database, create_tables
from database.database_schema import query
from database.populate import populates

def on_install():
    create_database()
    create_tables(query=query)
    populates()
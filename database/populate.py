from database.auto_populate.body import populates_body
from database.auto_populate.authorizations import populates_authorization


def populates():
  populates_body(table_name='body')  
  populates_authorization(table_name='authorizations')
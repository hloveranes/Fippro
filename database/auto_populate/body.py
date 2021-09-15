from database.function import insert_data


def populates_body(table_name):
  columns = [
    "type",
    "description"
  ]
  contents = [
    {"name": "none", "description": "description 1"},
    {"name": "form-data", "description": "description 2"},
    {"name": "x-www-form-urlencoded", "description": "description 3"},
    {"name": "raw", "description": "description 4"},
    {"name": "binary", "description": "description 5"},
    {"name": "GraphQL", "description": "description 6"},
    {"name": "No Schema", "description": "description 7"},
  ]

  insert_data(table_name=table_name, columns=columns, contents=contents)
  
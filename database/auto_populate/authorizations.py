from database.function import insert_data


def populates_authorization(table_name):
  columns = [
    "type",
    "description"
  ]
  contents = [
    {"name": "Inherit Auth From Parent", "description": "description 1"},
    {"name": "No Auth", "description": "description 2"},
    {"name": "API Key", "description": "description 3"},
    {"name": "Bearer Token", "description": "description 4"},
    {"name": "Basic Auth", "description": "description 5"},
    {"name": "Digest Auth", "description": "description 6"},
    {"name": "OAuth 1.0", "description": "description 7"},
    {"name": "Oauth 2.0", "description": "description 8"},
    {"name": "Hawk Authentication", "description": "description 9"},
    {"name": "AWS Signature", "description": "description 10"},
    {"name": "NTLM Authentication", "description": "description 11"},
    {"name": "Akamai EdgeGrid", "description": "description 12"},
  ]


  insert_data(table_name=table_name, columns=columns, contents=contents)

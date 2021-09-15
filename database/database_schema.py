query = (
  """ CREATE TABLE apis (
        id SERIAL PRIMARY KEY,
        method VARCHAR(255) UNIQUE NOT NULL,
        url VARCHAR(255) UNIQUE NOT NULL,
        response TEXT
    )
  """,
  """ CREATE TABLE params (
        id SERIAL PRIMARY KEY,
        key VARCHAR(255) UNIQUE NOT NULL,
        value VARCHAR(255),
        description TEXT
    ) 
  """,
  """ CREATE TABLE authorizations (
        id SERIAL PRIMARY KEY,
        type VARCHAR(100),
        description TEXT
    )
  """,
  """ CREATE TABLE headers (
        id SERIAL PRIMARY KEY,
        key VARCHAR(255) UNIQUE NOT NULL,
        value VARCHAR(255),
        description TEXT
    )
  """,
  """ CREATE TABLE body (
      id SERIAL PRIMARY KEY,
      type VARCHAR(100),
      description TEXT
  )
  """
)

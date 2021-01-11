import sqlite3

connection = sqlite3.connect('../db/melonkit.db')
cursor = connection.cursor()

print("Opened database successfully")

# create table
create_category = """
                  CREATE TABLE IF NOT EXISTS
                  category (
                        id          INTEGER PRIMARY KEY,
                        category    VARCHAR                 NOT NULL,
                        description VARCHAR                 NULL
                        )
                  """

create_code = """
            CREATE TABLE IF NOT EXISTS
            code (
                  id                INTEGER PRIMARY KEY,
                  id_category       INT                     NOT NULL,
                  url               VARCHAR                 NULL,
                  title             VARCHAR                 NOT NULL,
                  syntax            MEDIUMTEXT              NULL,
                  description       VARCHAR                 NULL,
                  created_at        DATETIME,
                  updated_at        DATETIME                NULL,
                  deleted_at        DATETIME                NULL,
                  FOREIGN KEY ( id_category ) REFERENCES category ( id )
                  )
            """


cursor.execute(create_category)
cursor.execute(create_code)
connection.close()
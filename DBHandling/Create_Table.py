import os
from dotenv import load_dotenv, find_dotenv
import mysql.connector
load_dotenv(find_dotenv())
db_config = {
    "host": os.environ.get("host"),
    "user": os.environ.get("user"),
    "password": os.environ.get("password"),
    "database": os.environ.get("database")
}

def create_table(table_name):
  try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    create_table_sql = f"""
        CREATE TABLE {table_name} (
            date_time DATETIME NOT NULL PRIMARY KEY,
            open_price DECIMAL(10,2) NOT NULL,
            high_price DECIMAL(10,2) NOT NULL,
            low_price DECIMAL(10,2) NOT NULL,
            close_price DECIMAL(10,2) NOT NULL,
            volume INTEGER NOT NULL
        );
    """
    cursor.execute(create_table_sql)
    connection.commit()
    cursor.close()
    connection.close()
    print("Table created successfully!")

  except mysql.connector.Error as err:
    print(f"Error connecting to database: {err}")
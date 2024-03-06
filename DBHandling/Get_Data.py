import os
from dotenv import load_dotenv, find_dotenv
import mysql.connector
import csv

load_dotenv(find_dotenv())
db_config = {
    "host": os.environ.get("host"),
    "user": os.environ.get("user"),
    "password": os.environ.get("password"),
    "database": os.environ.get("database")
}

def get_data_as_array(table_name):
  try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    sql = f"SELECT * FROM {table_name}"

    cursor.execute(sql)
    data = cursor.fetchall()
    data_array = []
    for row in data:
      data_array.append(list(row))

    cursor.close()
    connection.close()
    print("Data retrieval successful")
    return data_array

  except mysql.connector.Error as err:
    print(f"Error connecting to database: {err}")
    return None

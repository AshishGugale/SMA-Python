import os
from dotenv import load_dotenv, find_dotenv
import mysql.connector
from DBHandling.Unit_Test import validate_data
import csv

load_dotenv(find_dotenv())
db_config = {
    "host": os.environ.get("host"),
    "user": os.environ.get("user"),
    "password": os.environ.get("password"),
    "database": os.environ.get("database")
}
table_name = os.environ.get("table_name")

def insert_data_from_csv(data):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = f"""INSERT INTO {table_name} (date_time, close_price, high_price, low_price, open_price, volume)
                  VALUES (%s, %s, %s, %s, %s, %s)"""
        for row in data:
            if validate_data(row):
                cursor.execute(sql, row)
            else:
                print(f"Error: Invalid data type in row: {data.index(row) + 2}")
        connection.commit()
        cursor.close()
        connection.close()
        print("Data insertion successful")

    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")

def csv_reader(csv_path):
    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        data = list(reader)
        insert_data_from_csv(data)

def insert_data(csv_path):
    csv_reader(csv_path)
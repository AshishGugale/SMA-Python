import os
from dotenv import load_dotenv, find_dotenv
import DBHandling.Create_Table as CT
import DBHandling.Get_Data as GT
import DBHandling.Insert_Data as IT
import SMA.Strategy as ST

load_dotenv(find_dotenv())
table_name = os.environ.get("table_name")

if __name__ == "__main__":
    CT.create_table(table_name)
    IT.insert_data("path//to//csv")
    data = GT.get_data_as_array(table_name)
    ST.get_strategy(data)

from datetime import datetime

def validate_datetime(datetime_str, format="%Y-%m-%d %H:%M:%S"):
  try:
    datetime.strptime(datetime_str, format)
    return True
  except ValueError:
    return False
  
def validate_data(row):
    try:
        if not validate_datetime(row[0]):
           return False
        float(row[1])  # Close price
        float(row[2])  # High price
        float(row[3])  # Low price
        float(row[4])  # Open price
        int(row[5])   # Volume
    except ValueError:
        return False
    return True

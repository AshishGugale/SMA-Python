import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


window_size_short = int(os.environ.get("window_size_short"))
window_size_long = int(os.environ.get("window_size_long"))


def sma_vals(data):
  arr = [[0] * 2 for i in range(len(data))] 
  sm = 0;
  for i in range(window_size_short):
    sm += float(data[i][1])
    arr[i][0] = sm / (i + 1)
  sm = 0;
  for i in range(window_size_long):
    sm += float(data[i][1])
    arr[i][1] = sm / (i + 1)
  for i in range(window_size_short, len(data)):
    arr[i][0] = (arr[i - 1][0] * window_size_short + float(data[i][1]) - arr[i - window_size_short + 1][0]) / window_size_short
  for i in range(window_size_long, len(data)):
    arr[i][1] = (arr[i - 1][1] * window_size_long + float(data[i][1]) - arr[i - window_size_long + 1][1]) / window_size_long
  return arr
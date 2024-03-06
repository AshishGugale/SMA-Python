import os
from dotenv import load_dotenv, find_dotenv
from SMA.Calculate_Sma import sma_vals
load_dotenv(find_dotenv())

window_size_long = int(os.environ.get("window_size_long"))

def strat(arr):
  signals = [0] * (len(arr))
  for i in range(len(arr)):
    if i < window_size_long:
      pass
    if (arr[i][0] > arr[i][1]) and signals[i - 1] != 1:
      signals[i] = 1
    elif (arr[i][0] < arr[i][1]) and signals[i - 1] != -1:
      signals[i] = -1
  return signals

def calcPerf(data, signals):
  total_return = 0
  num_trades = 0
  curr = 0
  entry_price = None
  exit_price = None
  for i in range(len(data)):
    if(signals[i] == 1 and curr == 0):
      entry_price = float(data[i][1])
      curr = 1
    elif signals[i] == -1 and curr == 1:
      exit_price = float(data[i][1]) 
      curr = 0
      total_return += (exit_price - entry_price) / entry_price 
      num_trades += 1
      entry_price = None
      exit_price = None

  if curr == 1:
    exit_price = float(data[-1][1]) 
    total_return += (exit_price - entry_price) / entry_price  
    num_trades += 1

  return [total_return, num_trades]

def get_strategy(data):
  arr = sma_vals(data)
  signals = strat(arr)
  [total_return, num_trades] = calcPerf(data, signals)
  print("Total return obtained by this strategy is: ", total_return)
  print("Total trades performed by this strategy is: ", num_trades)





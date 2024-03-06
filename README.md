# SMA-Python

**#Description:**

This Python project implements the Simple Moving Average (SMA) indicator used in technical analysis. It calculates the SMA for a given time series of closing prices.

**## Strategy used:**

* Calculates SMA for two window sizes and uses their crossover
* Working - 
  *Calculates both short-term and long-term SMAs for the closing prices in the provided data.
  *Generates buy/sell signals based on the crossover of the two SMAs:
  *Buy signal: When the short-term SMA crosses above the long-term SMA.
  Sell signal: When the short-term SMA crosses below the long-term SMA.
  *Tracks performance metrics including total return and number of trades.

**## Installation:**

This project requires Python 3.x. You can install it by running the following command in your terminal:

```bash
pip install python
```
Installation of the modules required: 

```bash
pip install python-dotenv mysql-connector-python
```

**## Usage:**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AshishGugale/SMA-Python
   ```

2. **Adding environment variables:**

Create a .env file in the project directory and set the following environment variables: 
For connecting with the MySQL DB - 
 * host = MySQL host server (usually localhost for the local server)
 * user = MySQL username
 * password = MySQL password for "user"
 * database = Name of the MySQL database

User variables - 
* window_size_long = The long window to watch for SMA swings
* window_size_short = The short window to watch for SMA swings

3. **Data:**

Add the .csv file to the Data folder and update its path in the main file.

4. **SMA:**
   
Use the main.py script to get the values of total returns and number of trades performed for the given strategy. Tune the values of shorter and longer windows to get a varied output. 

**## Contributing:**

We welcome contributions to this project! Feel free to fork the repository, make changes, and submit a pull request.

**## License:**

This project is licensed under the MIT License. See the LICENSE file for details.


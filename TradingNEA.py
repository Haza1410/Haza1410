import numpy as np
import pandas as pd
import xlswriter
import requests
from scipy import stats
import math
from secrets import IEX_CLOUD_API_TOKEN
#Imports the software libraries: 
#NumPy - a numerial computing library, 
#Pandas - data frame for storing data, 
#XLSxWriter - module used to save Pandas data frame as an Excel file, 
#Requests - used to make HTTP requests, 
#SciPy Stats - a module containing probability distributions, summary and frequency statistics, correlation functions and statistical tests, 
#Math - a standard module that allows the use of mathematical functions.
#Secrets IEX_CLOUD_API_TOKEN - a platform that makes financial data accessible and imports the list of our stocks and API tokens.

stocks = pd.read_csv("sp_500_stocks.csv")
#Imports the list of stocks and our API token (a unique identifier of an application requesting access to a service) into a panda's data frame caled stocks; a csv file.

symbol = "aapl"
api_url = f"https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}"
#This takes data from IEX website to star building a value screener that ranks stocks based on the price to earnings ratio of a company (current stock price divded by estimated yearly earnings estimate)
#Add "stable" to the web address to ensure the website is fully tested and it uses no beta features.
#Turn the string into an "f" string to ensure the "symbol" becomes interpolated
data = requests.get(api_url).json()
#This creates an API call using th rerequests library
print(data.status_code)
#This is a stats code which tells you if your HTTP request was successful. A successful request will return a value of 200, an erroneous request will return a result between 400 -500

import numpy as np
import pandas as pd
import xlswriter
import requests
from scipy import stats
import math
#Imports the software libraries: NumPy - a numerial computing library, Pandas - data frame for storing data, XLSxWriter - module used to save Pandas data frame as an Excel file, Requests - used to make HTTP requests, SciPy Stats - a module containing probability distributions, summary and frequency statistics, correlation functions and statistical tests, Math - a standard module that allows the use of mathematical functions.

stocks = pd.read_csv("sp_500_stocks.csv")
#Imports the list of stocks and our API token (a unique identifier of an application requesting access to a service) into a panda's data frame caled stocks; a csv file.
stocks["Ticker"]

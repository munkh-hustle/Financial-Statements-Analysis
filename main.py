import requests
from bs4 import BeautifulSoup
import csv
import time
import random

companies = ['aapl']
balance = '_balance_sheet_statement_annual.csv'

site_url =''

session = requests.Session()
req = session.get(site_url).text
html = BeautifulSoup(req, "html.parser")

print(html.contents)
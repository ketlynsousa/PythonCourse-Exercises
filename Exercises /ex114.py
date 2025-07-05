# Python Exercise 114 Is the website accessible?
# Create a Python code that tests whether the website pudim.com.br is accessible from the computer used.
import requests
from ex_modules.colours import use_colours

url = 'https://www.pudim.com.br/'
try:
    response = requests.get(url)
    if response:
        print(f"{use_colours('green')}I managed to access successfully the website {url}.{use_colours('clean')}")
except requests.exceptions.RequestException:
    print(f"{use_colours('red')}The website {url} could not be reached at the moment.{use_colours('clean')}")

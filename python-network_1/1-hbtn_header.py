import requests
import sys
"""Taking a url from the command line arguements using sys"""
url = input("Enter URL:")if len(sys.argv) < 2 else sys.argv[1]

"""Returning the output"""
response = requests.get(url=url)
"""checking whether the variables x-Request-id is in the response header"""
if 'X-Request-Id' in response.headers:
    value = response.headers['X-Request-Id']
    print(value)

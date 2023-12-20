'''Make a request to fiverr server 
Request URL = https://fiverr.com
Request method = GET
'''
import requests
url ="https://fiverr.com"

response = requests.get(url)
print(response)

# print(dir(requests))
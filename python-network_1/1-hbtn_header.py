'''importing sys and requests which are inbuild/installed modules in python'''
import requests
import sys

def fetch_request_id(url):
    ''' Send a GET request to the provided URL'''
    response = requests.get(url)

    '''Check if X-Request-Id header is present in the response'''
    if 'X-Request-Id' in response.headers:
        request_id = response.headers['X-Request-Id']
        print(f"The value of the X-Request-Id header is: {request_id}")
    else:
        print("X-Request-Id header not found in the response.")

'''URL from command line argument'''
url= sys.argv[1]

'''Call the function with the provided URL'''
fetch_request_id(url)


import requests
import sys
"""Taking a url from the command line arguements using sys"""
url = input("EnterURL:")if len(sys.argv) < 2 else sys.argv[1]

"""Returning the output"""
response = requests.get(url=url)
"""checking whether the variables x-Request-id is in the response header"""
if 'X-Request-Id' in response.headers:
    value = response.headers['X-Request-Id']
    print(value)

# def get_request_id(url):
#     try:
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             request_id = response.headers.get('X-Request-Id')
#             print({request_id})
#         else:
#             print({response.status_code})
#     except requests.RequestException as e:
#         print({e})

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("https://alu-intranet.hbtn.io/status")
#         sys.exit(1)
    
#     url = sys.argv[1]
#     get_request_id(url)



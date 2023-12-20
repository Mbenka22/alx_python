import requests
import sys

url = "https://alu-intranet.hbtn.io/status"


def get_request_id(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            request_id = response.headers.get('X-Request-Id')
            print({request_id})
        else:
            print({response.status_code})
    except requests.RequestException as e:
        print({e})

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage:python script.py<URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    get_request_id(url)



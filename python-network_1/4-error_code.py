"""importing the required modules sys and requests"""
import requests
import sys
url = sys.argv[1]
def get_url_response(url):
    response = requests.get(url)

    
    """ Display the body of the response"""
    print(response.text)
    
    """Check if status code is greater than or equal to 400"""
    if response.status_code >= 400:
        print("Error code {response.status_code}" .format)
    else:
        print(response.status_code)



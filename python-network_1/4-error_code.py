"""importing the required modules sys and requests"""
import requests
import sys
url = 'https://alu-intranet.hbtn.io/status'
def get_url_response(url):
    response = requests.get(url)
    
    """ Display the body of the response"""
    print(response.text)
    
    """Check if status code is greater than or equal to 400"""
    if response.status_code >= 400:
        print({response.status_code})

if __name__ == "__main__":
    """Extract URL from command line argument"""
    url = sys.argv[1]
    
    """Call function to get URL response"""
    get_url_response(url)

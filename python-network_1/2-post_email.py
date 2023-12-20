

import requests
import sys
URL = "https://alu-intranet.hbtn.io/status"
email = "hr@holbertonschool.com"
def send_post_request(url, email):
    # Create a dictionary with the email parameter
    payload = {'email': "hr@holbertonschool.com"}
    
    # Send a POST request to the URL with the payload (email)
    response = requests.post(url, data=payload)
    
    # Display the body of the response
    print(response.text)

if __name__ == "__main__":
    # Check if enough arguments are passed
    if len(sys.argv) < 3:
        print("Usage: python script.py <https://alu-intranet.hbtn.io/status> <hr@holbertonschool.com")
        sys.exit(1)
    
    # Extract URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Call the function to send the POST request
    send_post_request(url, email)


"""importing the required modules sys and requests to work on the project"""
import requests
import sys

def get_github_id(username, password):
    url = 'https://api.github.com/user'
    auth = (username, password)

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        user_info = response.json()
        print(f"Your GitHub ID is: {user_info['id']}")
    else:
        print("Failed to retrieve GitHub ID")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]
        get_github_id(username, password)
    else:
        print("Usage: python script.py <mbenka22> <personal_access_token>")

import requests
import sys
"""Variable for storing url and a letter"""
url = sys.argv[1]
q = "" if len (sys.argv) < 2 else (sys.arv[2])

"""data transmitted over our url in a json """
data_send = {
    'q' : q
}
"""post to url"""
response = requests.post(url=url, data=data_send)
try:
   check_json = response.json()
   if not check_json:
      print("No result")
    else:
         id =check_json.get("id")
         name = check_json.get("name")
         print(f"{id} {name}")

except ValueError:
print()         

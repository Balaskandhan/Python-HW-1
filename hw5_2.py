import urllib.request
import json
from pprint import pprint

page = urllib.request.urlopen(" https://restcountries.eu/rest/v1/alpha/co")
content=page.read()
content_string = content.decode("utf-8")
json_data = json.loads(content_string)
country_code=input("Enter a country code to get it's name and capital:")
print("-"*55)
if (json_data["callingCodes"][0]) == (country_code):
    print("The country is: ",json_data["name"])
    print("The capital is: ",json_data["capital"])
else:
    print("sorry,code not found")
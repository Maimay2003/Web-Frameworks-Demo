from unittest.mock import Mock  # Imports Mock into project

newMockObj = Mock()  # Creates a new mock object

#print(newMockObj)  #Print the object to the terminal for inspection

import requests

apiResponse1 = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
print(apiResponse1, "\n")  # Regular api response

requests = newMockObj  # Patches, or imitates, the request object using newMockObj
print(dir(requests), "\n")  #. prints all methods associated with `requests`

apiResponse2 = requests.get('https://pokeapi.co/api/v2/pokemon')
print(apiResponse2, "\n")

print(dir(requests), "\n")
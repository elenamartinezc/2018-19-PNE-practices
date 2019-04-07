# Example of getting information about the weather of
# a location

import http.client
import json
import sys

yourCity = input("Insert a city to know the weather: ")
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query=" + yourCity
METHOD = "GET"
headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

weather = json.loads(text_json)
#-- If the city inserted is not valid
#-- It gives you an empty list
if len(weather) == 0:
    print('That city is not valid')
    sys.exit(0)
#print(weather)

woeid = weather[0]['woeid']


# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/"
LOCATION_WOEID = str(woeid)
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + LOCATION_WOEID + '/', None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
#print(text_json)

# -- Generate the object from the json file
weather = json.loads(text_json)

# -- Get the data
time = weather['time']
temp0 = weather['consolidated_weather'][0]
temp = temp0['the_temp']
place = weather['title']
sunset = weather['sun_set']

print()
print("Place: {}".format(place))
print("Time: {}".format(time))
print("Current temp: {} degrees".format(temp))
print("The sunset time is: {}".format(sunset))






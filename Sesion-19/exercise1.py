# -- Total number
# -- Categories
# -- Random joke
import http.client
import json
import random

#1
# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/count"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standard one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

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
obtained = json.loads(text_json)
value = obtained['value']
print ('Total number of jokes:', value)



#2
ENDPOINT = "/categories"

conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

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
obtained = json.loads(text_json)
categories = obtained['value']
print('The number of categories is:', len(categories))
for element in categories:
    print('-', element)



#3
ENDPOINT = "/jokes/random"

conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

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
obtained = json.loads(text_json)
joke = obtained['value']['joke']
print(joke)


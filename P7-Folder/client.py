import http.client
import json
from Seq import Seq

PORT = 80
SERVER = 'rest.ensembl.org'

conn = http.client.HTTPConnection(SERVER, PORT)
conn.request("GET", "/homology/symbol/human/FRAT1?content-type=application/json")
r1 = conn.getresponse()
data = r1.read().decode('utf-8')
answer = json.loads(data)
id = answer ['data'][0]['id']

conn.request("GET", "/sequence/id/" + id+ "?content-type=application/json")
r1 = conn.getresponse()
data = r1.read().decode("utf-8")
answer = json.loads(data)
dna = answer ['seq']

s1 = Seq(dna)
print ("Total", s1.len())
print ("The number of total T:",s1.count('T') )
print('The maximum number is:', max(s1.count('A'),s1.count('C'),s1.count('G'),s1.count('T')))
print ('The percentage of Gs:', s1.perc('G'), '%')
print ('The percentage of As:', s1.perc('A'), '%')
print ('The percentage of Cs:', s1.perc('C'), '%')
print ('The percentage of Ts:', s1.perc('T'), '%')

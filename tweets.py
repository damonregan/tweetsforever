import httplib
import json
from pprint import pprint

host = "api.twtter.com"
searchHost = "search.twitter.com"

connection = httplib.HTTPConnection(searchHost)
url = "/search.json?q=%40twitterapi%20%40anywhere"

connection.request("GET", url)

response = connection.getresponse()

jsonData = json.loads(response.read())

#pprint(json_data)

pprint(jsonData["results"][0])


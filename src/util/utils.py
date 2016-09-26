import urllib2
import json

def load_url(url, node_name):
    response = json.loads(urllib2.urlopen(url).read())
    return response[node_name]



import urllib2
import json
from pymongo import MongoClient

#connect to mongodb server and create database...
client = MongoClient()
db= client.nh1


data=[]
per_page='100'
search="new_haven"
page=1

while page<104:
    params="page="+str(page)+"&per_page="+per_page +"&search="+search
    response=urllib2.urlopen("https://seeclickfix.com/api/v2/issues?"+params)
    data = json.loads(response.read())["issues"]
    for document in data:
         db.issues.insert_one(document)
    page+=1

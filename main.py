from threading import Event
import time
from serveraction import dumptodatabase, textinfo, grabfromdatabase

from timer import MyThread

'''
#Unusable MongoDB insert and retrieve stuff
client = MongoClient('localhost', 27017)
db = client.plant_database
collection = db.plant_collection

def inserttodatabase(payload):
    post_id = collection.insert_one(payload).inserted_id
    return post_id

def retrievefromdatabase(parameter, value):
    return collection.find_one({parameter:value})
'''
starttime = time.time()

def main():
    while(getdata()!=False):
        if((time.time()-starttime)%1==0):
            print ("Getting data...")
            getdata({})
        elif((time.time()-starttime)%5==0):
            print ("Texting end user...")
            textinfo(grabfromdatabase)


def getdata(jsonobj):
    if(jsonobj==False):
        return False
    else:
        dumptodatabase(jsonobj)

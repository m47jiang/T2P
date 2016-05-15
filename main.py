from threading import Event
import time
from serveraction import dumptodatabase

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
def main():
    stopFlag = Event()
    msgThread = MyThread(stopFlag)
    msgThread.start()
    # this will stop the timer
    while(getdata()!=False):
        getdata({})
        time.sleep(1)
    stopFlag.set(getdata()==False)


def getdata(jsonobj):
    if(jsonobj==False):
        return False
    else:
        dumptodatabase(jsonobj)

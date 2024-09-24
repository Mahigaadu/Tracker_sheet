from pymongo import MongoClient

def get_db():
    #url='mongodb+srv://*******:********@cluster0.drxtl.mongodb.net/'
    myclient=MongoClient('mongodb+srv://*******:********cluster0.drxtl.mongodb.net/')# use mongodb connection string
    mydb=myclient['Tracker_sheet']
    return mydb

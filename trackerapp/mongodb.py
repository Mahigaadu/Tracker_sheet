from pymongo import MongoClient

def get_db():
    #url='mongodb+srv://mahigaadu09:MongoPassword@cluster0.drxtl.mongodb.net/'
    myclient=MongoClient('mongodb+srv://mahigaadu09:MongoPassword@cluster0.drxtl.mongodb.net/')
    mydb=myclient['Tracker_sheet']
    return mydb
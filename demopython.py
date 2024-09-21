import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
 
# Database Name
db = client["dbmycrawler"]
 
# Collection Name
col = db["tblunitop"]
 
x = col.find()
 
for data in x:
    print(data)
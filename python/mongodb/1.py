from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.myNewDatabase
collection = db.myCollection


collection.insert_one(dict(
    name="東京スカイツリー",
    prefecture="東京"
))

collection.insert_many([
    dict(
        name="東京ディズニーランド",
        prefecture="千葉"
    ),
    dict(
        name="東京ドーム",
        prefecture="東京"
    )
])

for spot in collection.find(dict(prefecture="東京")):
    print(spot)

import pymongo

m = pymongo.MongoClient()
m.test.users
# m.test.users.insert({'a': 1, 'l', [1234, 23, 43]})



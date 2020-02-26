from pymongo import MongoClient
import datetime, time

client = MongoClient()
db = client['circle_mind_db']

collect1 = db['collect1']
collect2 = db['collect2']

data = {'_id': 'doc', 'doc_list': []}

doc = collect2.find_one({'_id': 'doc'})

print(doc)
doc['doc_list'].append(54)

collect2.update_one(doc, {'$set': {'doc_list': doc['doc_list']}})
print(doc)

# doc['doc_list'].append(228)
# print(doc)

# del_data = [{'_id': 1}, {'_id': 2}]


# collect2.insert_many([{'id': 12}, {'id': 13}])
# print(collect2.find({{'id': '$all'}}))


# doc = collect2.find_one({'_id': 'doc'})
# print(doc)

# doc['doc_list'].append(3)

# print(doc, '\n', time.strftime("%Y.%m.%d.%H.%M.%S"))


# collect1.insert_one(data)
# collect2.insert_one(data)


# print(collect2.count_documents({}))

# print(db_queries.insert_data_1(data, db))


client.close()

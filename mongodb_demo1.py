from pymongo import MongoClient

client = MongoClient("mongodb+srv://user1:user1p@cluster1-eqyia.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('students')

collection = db.student_info

student_2 = {
    "name" : "xyz",
    "roll_no" : 2,
    "dept" : "it"
}

#collection.insert_one(student_2)
print(collection.count_documents({}))

student_3_to_5 = [{
    "name": "def",
    "roll_no": 3,
    "dept": "entc"
},
{
    "name": "ghi",
    "roll_no": 4,
    "dept": "elex"
},
{
    "name": "jkl",
    "roll_no": 5,
    "dept": "instru"
}
]
#collection.insert_many(student_3_to_5)
print(collection.count_documents({}))
print(list(collection.find()),end="\n")

#collection.update_one({"name":"def"},{"$set":{"name":"DEF"}})

print("\n\n After update : ",list(collection.find()),end="\n")

#collection.delete_one({"name": "DEF"})

print("No. of Documents is :",collection.count_documents({}))

#collection.delete_many({})
print(collection.count_documents({}))




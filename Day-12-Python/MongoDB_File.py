from pymongo import MongoClient

connection = MongoClient("localhost", 27017)

pythonDataTypes = {
    "Numeric": {
        "int": 10,
        "float": 12.5,
        "complex": "10 + 5j",
    },
    "Sequence Type": {
        "str": "BestEnlist Internship",
        "list": "[1, 2, 3, 4, 5]",
        "tuple": "(1, 2, 3, 4, 5)"
    },
    "Boolean": {
        "bool": "True"
    },
    "Set": {
        "set": "{1, 2, 3, 4, 5}"
    },
    "Dictionary": {
        "dict": {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    }
}

db = connection['bepythonDB']

collection = db['datatype']

collection.insert_one(pythonDataTypes)

if collection:
    print("Data inserted successfully")
    for data in collection.find({}):
        print(data)
else:
    print("Error")
'''from pymongo import MongoClient
client = MongoClient('mongodb+srv://josephabaeza:test!1@cluster0.nud7d8s.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database('cars_db')
records = db.car_records

#records.count_documents({})
























import csv
import pymongo

# MongoDB connection settings
mongo_client = pymongo.MongoClient("mongodb+srv://josephbaeza:password@cluster0.nud7d8s.mongodb.net/?retryWrites=true&w=majority")  # Replace with your MongoDB connection string
db = mongo_client['cars_db']  # Replace 'my_database' with your database name
collection = db['cars_records']  # Replace 'my_collection' with your collection name

# CSV file path
csv_file_path = 'table_data.csv'  # Replace with your CSV file path

# Open the CSV file and insert data into MongoDB
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Insert each row as a document in the MongoDB collection
        collection.insert_one(row)

print('Data from CSV file has been imported into MongoDB.')

from pymongo import MongoClient
client = MongoClient ("mongodb+srv://josephbaeza:password@cluster0.a08odj5.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('cars_db')
records = db.car_records



records.count_documents({})'''

import csv
from pymongo import MongoClient

# MongoDB connection settings
client = MongoClient("mongodb+srv://josephbaeza:password@cluster0.a08odj5.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('cars_db')
records = db.car_records

# CSV file path
csv_file_path = 'table_data.csv'  # Replace with your CSV file path

# Open the CSV file and insert data into MongoDB
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Insert each row as a document in the MongoDB collection
        records.insert_one(row)

print('Data from CSV file has been imported into MongoDB car_records.')

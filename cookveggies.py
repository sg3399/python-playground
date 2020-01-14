#by Lucas and Siddhant

#loading libaries
import csv
import json

#reading csv into a variable called vegetables
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)
    vegetables = [dict(row) for row in vegetables] # Convert OrderedDict to regular dict

#checking dictionary
print(vegetables)

#Reading dictionary into json
with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent=1)
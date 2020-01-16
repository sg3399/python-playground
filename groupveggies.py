#by Lucas and Siddhant

#loading libraries
from pprint import pprint
import csv
import json

# Read vegtables.csv into a variable called vegtables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)
    vegetables = [dict(row) for row in vegetables] # Convert OrderedDict to regular dict

# Group vegtables by color as a variable vegtables_by_color.
vegtables_by_color = {}
for row in vegetables:
    color = row['color']
    if color in vegtables_by_color:
        vegtables_by_color[color].append(row)
    else:
        vegtables_by_color[color] = [row]

pprint(vegtables_by_color)

# Output vegtables_by_color into a json called vegtables_by_color.json.
with open('vegetables_by_color.json', 'w') as f:
    json.dump(vegtables_by_color, f, indent=1)



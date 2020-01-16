#by Lucas and Siddhant

#loading libraries
import csv
import json

# Read vegetables.csv into a variable called vegetables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)
    vegetables = [dict(row) for row in vegetables] # Convert OrderedDict to regular dict
print(vegetables)

# Loop through vegetables and filter down to only green vegtables using a whitelist.
green_veggies=[]
for veggie in vegetables:
	if veggie["color"]=="green":
		green_veggies.append(veggie)

# Print veggies to the terminal
print(green_veggies)

# Write the veggies to a json file called greenveggies.json
with open('greenveggies.json', 'w') as f:
    json.dump(green_veggies, f, indent=1)

#Bonus
with open('green_vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    #writing the header
    writer.writerow(['name','color'])
    #writing the loop
    for i in range(0,len(green_veggies)):
    	writer.writerow([green_veggies[i]["name"],green_veggies[i]["color"]])
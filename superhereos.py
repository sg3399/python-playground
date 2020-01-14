#by Lucas and Siddhant

import json
import csv
from pprint import pprint

with open('superheroes.json', 'r') as f:
    superheroes=json.load(f)

# Creates an empty an array called power
powers=[]

# Loop thorough the members of the squad, 
# Append the powers of each to the powers array.
members = superheroes ['members']

for hero in members:
	hero_powers= hero['powers']
	powers.append(hero_powers)

# Prints those powers to the terminal
pprint(powers)

with open('superheroes.csv', 'w') as f:
    writer = csv.writer(f)
    #writing the header
    writer.writerow(['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active'])
    members = superheroes ['members']
    for hero in members:
    	hero_name = hero['name']
    	hero_age = hero['age']
    	hero_identity= hero['secretIdentity']
    	hero_power = hero['powers']
    	superhero_squad = superheroes['squadName']
    	superheroes_home = superheroes['homeTown']
    	superheroes_formed = superheroes['formed']
    	superheroes_secret = superheroes['secretBase']
    	superheroes_active = superheroes['active']
    	
    	writer.writerow([hero_name,hero_age, hero_identity,hero_power,superhero_squad, superheroes_home,superheroes_formed,superheroes_secret, superheroes_active])

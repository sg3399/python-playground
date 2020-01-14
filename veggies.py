#by Lucas and Siddhant 
import csv


vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#This writes a csv vegetables.csv which takes the dictionary and converts it to a csv
with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    #writing the header
    writer.writerow(['name','color'])
    #writing the loop
    for i in range(0,len(vegetables)):
    	writer.writerow([vegetables[i]["name"],vegetables[i]["color"]])

#This is an alternate way to do the excercise above
with open('vegetables1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name','color'])
    for veggie in vegetables:
    	writer.writerow([veggie["name"],veggie["color"]])


# addimg length of veg (bonus)
with open('vegetables2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name','color', 'length'])
    for veggie in vegetables:
    	writer.writerow([veggie["name"],veggie["color"],len(veggie["name"])])

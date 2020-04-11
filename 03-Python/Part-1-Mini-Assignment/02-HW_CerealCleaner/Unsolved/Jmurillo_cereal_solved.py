import os
import csv

cereal_csv = os.path.join(".." , "Resources", "cereal.csv")


with open(cereal_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    fields = next (csvreader, None)
    for row in csvreader:
        
        name = row[0]
        calories = row[3]
        protein	= row[4]
        fat	= row[5]
        sodium	= row[6]
        fiber = float(row[7])
        carbo = row[8]
        sugars = row[9]
        potass = row[10]
        vitamins = row[11]	
        shelf = row[12]
        weight = row[13]
        cups = row[14]
        rating = row[15]

               
        if fiber >= 5:
            print(row[0])
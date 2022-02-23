# Dictionary
# A dictionary is a collection of unordered data, which is stored in key-value pairs. 
# variable = { key: value }
# accessed through a key or value rather than index

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.items()
car['year'] = 2018
print(x)

car.get("brand")
car.get("year", "year not available")

# Dictionary with List or another Dictionary

data = {
    "Hold": "BE-IT S22 DA",
    "Undervisere": { 
        "Systemudvikling": "Jamsheid",
        "Softwarekonstruktion": "Mikkel"
     },
     "Lokaler": ["E412, E312, E212"]
}

print(data.items())

for uv in data.keys():
    print(uv)
for uv2 in data.values():
    print(uv2)

# Tekstfiler
f = open('fil.txt', 'w+')
f.write('Indhold i filen')
f.close()

f = open('fil.txt', 'r')
indhold = f.read()
print(indhold)

# CSV filer
# importer modulet csv
import csv
with open('static/test.csv', mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow( ["Name", "City"])
    writer.writerow( ["Mikkel", "Nørrebro"])

with open("static/test.csv", mode="r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(row)

# File modes
# 'r' This is the default mode. It opens the file for reading only.
# 'w' Opens file for writing. If file doesn't exist, it creates one.
# 'x' Creates a new file. If file exists, the operation fails.
# 'a' Open in append mode. If file doesn't exist, it creates one.
# 'b' Open in binary mode.
# '+' Will open a file for reading and writing. Good for updating.

import pandas as pd 
import random

names = [ "Jess", "Jordan", "Sandy", "Ted", "Barney", "Tyler", "Rebecca" ]
ages = [ random.randint(18, 35) for x in range(len(names))]
people = { "names" : names, "ages" : ages }
df = pd.DataFrame.from_dict(people)
print(df)


# importer matplotlib modulet
from matplotlib import pyplot as plt
plt.plot([1,2,3])
# brug savefig() til at gemme som png
plt.savefig('static/myfig')
plt.close()

# En anden model
# using savefig method to save the chart as a jpg to the local folder
x, y = [ 1600, 1700, 1800, 1900, 2000 ], [ 0.2, 0.5, 1.1, 2.2, 7.7 ]
plt.plot(x, y, "bo-")       # creates a blue solid line with circle
plt.title("World Population Over Time")
plt.xlabel("Year")
plt.ylabel("Population (billions)")
plt.savefig('static/population')
plt.close()
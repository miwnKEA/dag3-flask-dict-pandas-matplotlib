# Vi importerer modulet Flask ind i vores Python fil
from flask import Flask, render_template
from matplotlib import pyplot as plt
import pandas as pd 
import csv, random

# Vi laver en variabel "app" som er en instantiering af klassen Flask
app = Flask(__name__)

# Definere class
class Car:
    # Definere attributer for en bil i min bilhandler
    def __init__(self, brand, model, color, onSale, marketPrice, sellingPrice, kmPerLiter, reperationer):
        self.brand = brand
        self.model = model
        self.color = color
        self.onSale = onSale
        self.marketPrice = marketPrice
        self.sellingPrice = sellingPrice
        self.kmPerLiter = kmPerLiter
        self.reperationer = reperationer

    # Definere metode for at udregne salgsbonusen for en bil
    def calculateSalesBonus(self):
        salesBonus = int((self.marketPrice - self.sellingPrice) * 0.20)
        try:
            if salesBonus >= 2000 and salesBonus <= 5000:
                extraBonus = salesBonus + 500
                return extraBonus
            elif salesBonus <= 2000:
                extraBonus = salesBonus + 1000
                return extraBonus
            elif salesBonus >= 5000:
                salesBonus = 5000
                return salesBonus
            else:
                salesBonus = 0
                return salesBonus
        except:
            return 'Noget gik galt.'

# Instantiere objekter af vores klasse Car
car1 = Car('Volkswagen', 'Golf', 'Grøn', True, 28000, 24000, 18.1, ['Skifte gearkassen i 2018', 'Dækskifte til vintersæson'])
car2 = Car('Toyota', 'Prius', 'Blå', False, 50000, 40000, 15.8, [])
car3 = Car('Ford', 'Mustang', 'Rød', False, 44500, 30000, 16.5, ['Klargøring til sommersalg'])
car4 = Car('Tesla', '3', 'Rød', True, 70000, 40000, 16.5, ['Nyt batteri'])

# Vi vil gerne oprette en List med alle vores biler
# variable = [index[0], index[1], index[2]]
cars = [car1, car2, car3, car4]

# Åbner en csv fil med fil mode "w" så vi kan skrive til filen
with open('static/cars.csv', mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    # laver et for loop og skriver vores objekter i listen cars til filen
    for i in cars:
        writer.writerow([i.brand, i.model, i.color, i.onSale, i.marketPrice, i.sellingPrice, i.kmPerLiter, i.reperationer])

# tomme lister til matplotlib charts
car_price = []
car_category = []
car_bonus = []

# for loop for at fylde tomme lister op med data
for car in cars:
    car_price.append(car.marketPrice)
    car_category.append(car.brand)
    bonus = car.calculateSalesBonus()
    car_bonus.append(bonus)

# Matplotlib bar og plot diagram
plt.bar(car_category, car_price)
plt.title("Pris på biler")
plt.savefig('static/cars_price')
plt.close()

f, ax = plt.subplots(1)
ax.plot(car_category, car_bonus)
ax.set_ylim(ymin=0, ymax=5500)
plt.title("Bonus på biler")
plt.savefig('static/cars_bonus')
plt.close()

# laver en tom liste som jeg kan putte min Dictionaries ind i
# Opretter et loop som ud fra tilfældige værdier, smider data ind i en csv fil
carsListDict = []
for x in range(1000):
    randomBrand = ['Volkswagen', 'Tesla', 'Ford', 'Toyota', 'Volvo', 'Jeep']
    randomModel = ['Golf', 'Prius', 'Mustang', '3', 'Stationcar', 'Mini']
    randomColor = ['Grøn', 'Blå', 'Gul', 'Sort', 'Rød', 'Grå', 'Hvid']
    randomBool = [True, False]
    randomMarketPrice = int(round(random.randint(30000, 80000) / 500) * 500)
    randomSellingPrice = int((randomMarketPrice + round(random.randint(2000, 8000) / 500) * 500))
    randomKmPerLiter = round(random.uniform(13, 25), 1)
    randomRep = ['Nyt batteri', 'Klargøring til sommer', 'Skifte dæk', 'Sætte vinterdæk på', 'Sten i ruden', 'Skifte gearkasse', 'Ny olie']
    
    
    
    
    
    
    x = Car(random.choice(randomBrand), random.choice(randomModel), random.choice(randomColor), random.choice(randomBool), randomSellingPrice, randomMarketPrice, randomKmPerLiter, [random.choice(randomRep)])
    
    
    


    newCar = {
        'brand': x.brand,
        'model': x.model,
        'color': x.color,
        'onSale': x.onSale,
        'marketPrice': x.marketPrice,
        'sellingPrice': x.sellingPrice,
        'kmPerLiter': x.kmPerLiter,
        'reperationer': x.reperationer
    }






    carsListDict.append(newCar)





    with open('static/carsDict.csv', mode="w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        for i in carsListDict:
            writer.writerow([i['brand'], i['model'], i['color'], i['onSale'], i['marketPrice'], i['sellingPrice'], i['kmPerLiter'], i['reperationer']])

# Laver en DataFrame med pandas som læser min csv fil
df = pd.read_csv('static/carsDict.csv')

print(df)

# Decorator for en route så den får adressen http://127.0.0.1:5000/
@app.route('/')
# Definerer en funktion for vores route som hedder hello()
def index():
# creating a bar plot using x and y coords
       return render_template("index.html", cars=cars)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=9000)
import pandas as pd

dataset = pd.read_csv("2020-XTern-DS.csv", sep = ",", header = 0)
print(dataset)
print("\n")

entireDataSet = dict()
foodTypes = dict()
mostFoodTypes = dict()
popularFoodTypes = dict()
longestCookTime = dict()
expensiveFood = dict()

for index, row in dataset.iterrows():
    restID = row.iloc[0]
    lat = row.iloc[1]
    long = row.iloc[2]
    foodType = row.iloc[3].split(", ")
    for type in foodType:
        if type not in foodTypes:
            foodTypes[type] = 1
        else:
            foodTypes[type] = foodTypes[type] + 1
    avgCost = row.iloc[4][1:]
    minOrder = row.iloc[5][1:]
    rating = row.iloc[6]
    votes = row.iloc[7]
    review = row.iloc[8]
    cookTime = row.iloc[9]
    data = [lat, long, foodType, avgCost, minOrder, rating, votes, review, cookTime]
    entireDataSet[restID] = data

#print(entireDataSet)
#print(foodTypes)
mostFoodTypes = sorted(foodTypes.items(), key=lambda x: x[1], reverse=True)
print(mostFoodTypes)
print("The most common food type is North Indian food with 878 restaurants that carry it, with Chinese about 150 restaurants behind it with 631 restaurants that carry it.\n")

for key in entireDataSet:
    foodType = entireDataSet[key][2]
    rating = entireDataSet[key][5]
    #print(rating)
    if "." in rating:
        rating = float(rating)
    #print(foodType)
    if isinstance(rating, float):
        for type in foodType:
            if type not in popularFoodTypes:
                popularFoodTypes[type] = [float(rating), 1]
            else:
                popularFoodTypes[type][0] = popularFoodTypes[type][0] + float(rating)
                popularFoodTypes[type][1] = popularFoodTypes[type][1] + 1
#print(popularFoodTypes)
for key in popularFoodTypes:
    if(popularFoodTypes[key][1] >= 50):
        average = popularFoodTypes[key][0] / popularFoodTypes[key][1]
        popularFoodTypes[key] = round(average * 100) / 100
    else:
        popularFoodTypes[key] = 0

#print(popularFoodTypes)
popularFoodTypes = sorted(popularFoodTypes.items(), key=lambda x: x[1], reverse=True)
print(popularFoodTypes)

print("Of the restaurants that have 50 or more reviews, the type of food with the highest rating is Continental food with a rating of 3.98, with Italian as a very close second with a rating of 3.97.\n")

for key in entireDataSet:
    foodType = entireDataSet[key][2]
    cookTime = entireDataSet[key][8]
    cookTime = int(cookTime[0:2])
    #print(cookTime)
    #print(foodType)
    if isinstance(cookTime, int):
        for type in foodType:
            if type not in longestCookTime:
                longestCookTime[type] = [float(cookTime), 1]
            else:
                longestCookTime[type][0] = longestCookTime[type][0] + float(cookTime)
                longestCookTime[type][1] = longestCookTime[type][1] + 1
#print(longestCookTime)
for key in longestCookTime:
    average = longestCookTime[key][0] / longestCookTime[key][1]
    longestCookTime[key] = round(average * 100) / 100
#print(longestCookTime)
longestCookTime = sorted(longestCookTime.items(), key=lambda x: x[1], reverse=True)
print(longestCookTime)

print("The food type that takes the most time to cook on average is Belgian food taking 65 minutes with Kashmiri in second taking 10 minutes less.\n")

for key in entireDataSet:
    foodType = entireDataSet[key][2]
    price = entireDataSet[key][3]
    if "." in price:
        price = float(entireDataSet[key][3])
    #print(price)
    #print(foodType)
    if isinstance(price, float):
        for type in foodType:
            if type not in expensiveFood:
                expensiveFood[type] = [float(price), 1]
            else:
                expensiveFood[type][0] = expensiveFood[type][0] + float(price)
                expensiveFood[type][1] = expensiveFood[type][1] + 1
#print(expensiveFood)
for key in expensiveFood:
    average = expensiveFood[key][0] / expensiveFood[key][1]
    expensiveFood[key] = round(average * 100) / 100
#print(expensiveFood)
expensiveFood = sorted(expensiveFood.items(), key=lambda x: x[1], reverse=True)
print(expensiveFood)

print("The food type that is the most expensive on average is Cantonese food with an average price of $100, $20 more expensive than the second place of Korean food at $80.")







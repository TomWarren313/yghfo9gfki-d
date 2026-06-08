fav_foods = []
def getfavfoods():
    food = input('Enter a favourite food: ')
    fav_foods.append(food)
    return getfavfoods()
for i in range(5): 
    getfavfoods()
for food in fav_foods:
    print(len(food))
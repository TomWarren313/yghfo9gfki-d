ytic = []
def city():
    cities = input('Enter a city: ')
    ytic.append(cities)
    return cities
for i in range(5):
    city()
for cities in ytic:
  print(cities, len(cities), 'characters')
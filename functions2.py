ytic = []
def city():
    for i in range(5):
      cities = input('Enter a city: ')
      ytic.append(cities)
    return cities

city()
for cities in ytic:
  print(cities, len(cities), 'characters')
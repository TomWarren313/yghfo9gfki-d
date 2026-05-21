farm = []
def animals():
    zoo = input('Enter a animals: ')
    farm.append(zoo)
    return zoo
for i in range(5):
    animals()
for zoo in farm:
  print(zoo, len(zoo), 'characters')
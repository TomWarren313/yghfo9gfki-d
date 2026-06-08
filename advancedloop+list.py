best_time = 0
goal_time = 60
held_times = []

while True:
  try:
    time = int(input('How long did you hold your breath? '))
    if time > 0:
      held_times.append(time)
    if time > best_time:
      best_time = time
      print(f'A personal best! {best_time} seconds is your best time.')
    if time >= goal_time:
      print(f'A personal best! {best_time} seconds is your best time.')
      print('You reached your goal!!!')
      break
    
  except ValueError:
    break
print('Recording ended.')


if len(held_times) == 0:
  print('Sorry, you have not entered any valid times.')

print('Your results are:')
held_times.sort()
for num in held_times:
  print(num, 'seconds')
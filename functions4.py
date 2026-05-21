def check_weather(temperature):
    if temperature > 25:
        return 'Hot!'
    if temperature < 15:
        return 'Cold'
    else:
        return 'warm'
    
print(check_weather(30))
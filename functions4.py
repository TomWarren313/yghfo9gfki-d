def check_weather(temperature):
    if temperature > 25:
        return 'Hot!'
    if temperature < 15:
        return 'Cold'
    else:
        return 'warm'
    
weather = int(input("Check Weather: "))
print(check_weather(weather))
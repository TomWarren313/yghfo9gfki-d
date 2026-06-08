def check_size(number):
    if number < 10:
        return "Small"
    elif 10 <= number <= 99:
        return "Medium"
    else:
        return "Large"


num = int(input("Enter a number: "))
print(check_size(num))
#im like 90% sure this work
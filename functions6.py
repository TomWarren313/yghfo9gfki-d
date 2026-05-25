def check_size(number):
    if number < 10:
        return "Small"
    elif 10 <= number <= 99:
        return "Medium"
    else:
        return "Large"


# Example usage
num = int(input("Enter a number: "))
print(check_size(num))
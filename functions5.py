def check_age(age):
    if age < 13:
        return 'child'
    if age >= 18:
        return 'Adult'
    if age >= 13 and age <= 17:
        return 'Teenager'
skibi = int(input('Enter your age: '))    
print(check_age(skibi))
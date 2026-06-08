def get_input():
    people_name = []
    grades = []
    flag = True
    while flag:
        name = input('Please input your name: ')
        people_name.append(name)    
        grade = int(input('Please input your grade: '))
        grades.append(grade)      
        current_count = len(grades)
        if current_count >= 5:
            repeat = input('Do you want to add another person? (yes/no): ').strip().lower()
            if repeat == 'no':
                flag = False
        else:
            print(f"Minimum 5 entries required. ({current_count}/5 completed)")          
    total = sum(grades)
    average = total / len(grades)  
    return people_name, grades, average
names, scores, avg = get_input()
print(f"\nFinal Names: {names}")
print(f"Final Grades: {scores}")
print(f"Final Average: {avg:.2f}")
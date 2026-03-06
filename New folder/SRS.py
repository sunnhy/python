## Student Result System

students = {
    "Asha": 85,
    "Pasha": 72,
    "Lasha": 90,
    "Sasha": 60
}

# Add a new student and their score
name = input("Enter the name of the student: ")
score = int(input("Enter the score of the student: "))
students[name] = score

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return  'Fail'

for name, score in students.items():
    grade = calculate_grade(score)
 
    print(f"{name} scored {score} and got {grade}")

pass_marks = 60
students_passed = sum(1 for score in students.values() if score >= pass_marks)
print(f"Number of students passed: {students_passed}")

def calculate_highest_score(students):
    highest_score = max(score for score in students.values())
    return highest_score

highest_score = calculate_highest_score(students)
print(f"The highest score is: {highest_score}")
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.


# TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = {}

for name, score in student_scores.items():
    if score <= 70:
        grade = "Fail"
        student_grades[name] = grade

    elif 71 <= score <= 80:
        grade = "Acceptable"
        student_grades[name] = grade

    elif 81 <= score <= 90:
        grade = "Exceeds Expectations"
        student_grades[name] = grade

    elif 91 <= score <= 100:
        grade = "Outstanding"
        student_grades[name] = grade

# 🚨 Don't change the code below 👇
print(student_grades)

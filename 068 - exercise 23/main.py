students_marks = {
    "a":10,
    "b":20,
    "c":30,
    "d":40,
    "e":50,
    "f":60,
    "g":70,
    "h":80,
    "i":90,
    "j":100,
}

print(students_marks)

students_grades = {}

for student in students_marks:
    name,mark = student, students_marks[student]
    grade = ""
    if( mark > 90):
        grade = "A+"
    elif( mark > 80):
        grade = "A"
    elif(mark > 60):
        grade = "B"
    elif( mark > 40):
        grade = "C"
    else:
        grade = "f"
    
    students_grades[name] = grade

print(students_grades)
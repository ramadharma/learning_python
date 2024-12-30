student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# create an empty dictionary to collect new value
student_grades = {}

# looping a dictionary to collect the name of the student
for student in student_scores:

    # create new variable to collect the scores
    scores = student_scores[student]

    # program to collect the grades of each student
    if scores >= 91:
        student_grades[student] = "Outstanding"
    elif scores >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif scores >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    
print(student_grades)
    
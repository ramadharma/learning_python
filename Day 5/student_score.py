student_score = [123, 125, 152, 124, 156, 180, 105, 80, 90, 72, 120]

total_score = sum(student_score)

max_score = 0

for score in student_score:
    # searching/looping biggest number than previous number 
    if score > max_score:
        max_score = score

print(max_score)
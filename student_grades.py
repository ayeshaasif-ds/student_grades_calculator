# student_grades.py
# Calculate student grades based on marks

student_name = input("Enter student name: ")
marks = int(input("Enter marks (0-100): "))
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"
print(f"{student_name} got grade: {grade}")

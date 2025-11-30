# Student Grades Calculator 📝

## Overview
This Python project calculates the grade of a student based on their marks.  
It is a beginner-friendly project to practice **Python basics** and **conditional statements**.

## Project Details
- **Language:** Python
- **Level:** Beginner
- **Purpose:** Practice Python input, conditional statements, and basic logic.

## Code
```python
# student_grades.py
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

print(f"{student_name} got grade: {grade}")# student_grades_calculator
Beginner Python project to calculate student grades.

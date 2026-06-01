#Dictionary
student = {
    "name": "Nabaraj",
    "age": 20,
    "scores": [85, 92, 78],
    "department": "Computer Science",
    "is_active": True
}

print("Student Dictionary:")
print(student)

# Accessing Values
print("\nStudent Name:", student['name'])
print("Student Scores:", student['scores'])
print("Student Age:", student['age'])

# Adding New Values
student['address'] = "Kathmandu"
student['semester'] = 7

print("\nAfter Adding Values:")
print(student)

# Updating Existing Values
student['age'] = 21
student['department'] = "BCA"

print("\nAfter Updating Values:")
print(student)
nabaraj_score = student['scores']

# Function to determine grade using conditional statements
def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "Fail"


# Taking input from user
score = int(input("Enter your score: "))

# Calling function
grade = determine_grade(score)

# Display result
print("Your Grade is:", grade)
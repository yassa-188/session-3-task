
students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [70, 75, 80]},
    {"name": "Charlie", "grades": [92, 88, 95]}
]
for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades)/len(grades)
    print(f"{name}: Average Grade = {average:.2f}")
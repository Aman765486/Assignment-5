# Program to manage student marks with a dictionary

# Step 1: Create a dictionary of student names and marks
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92
}

# Step 2: Ask user for a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show error message
if name in students:
    print(f"{name}'s marks = {students[name]}")
else:
    print(f"Student '{name}' not found in the records.")

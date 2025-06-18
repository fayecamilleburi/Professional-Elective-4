# Prompt for last name, first name, section, program, and birth year
print("Student Information Collection")
last_name = input("Enter your last name: ")
first_name = input("Enter your first name: ")
section = input("Enter your section: ")
program = input("Enter your program: ")
birth_year = int(input("Enter your birth year: "))

# Compute the student's age
age = 2025 - birth_year

# Prompt to collect hobbies
print("\nHobbies Collection")
hobby1 = input("Enter your first hobby: ")
hobby2 = input("Enter your second hobby: ")
hobby3 = input("Enter your third hobby: ")

# Store hobbies in a list
hobbies = [hobby1, hobby2, hobby3]

# Create a dictionary to store student information
student_info = {
    "Last Name": last_name,
    "First Name": first_name,
    "Section": section,
    "Program": program,
    "Hobbies": hobbies,
    "Age": age
}

# Print content of the dictionary
print("\nStudent Information:")
print(f"Name: {student_info['Last Name']}, {student_info['First Name']}")
print(f"Program: {student_info['Program']}")
print(f"Section: {student_info['Section']}")
print(f"Hobbies: {', '.join(student_info['Hobbies'])}")
print(f"Age: {student_info['Age']}")

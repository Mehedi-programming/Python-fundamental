# Student Management System in Python

# List to store student records
students = []

# Function to add a new student
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    
    # Check if ID already exists
    if any(student['id'] == student_id for student in students):
        print("Student ID already exists.")
        return
    
    # Create a new student record
    student = {
        'id': student_id,
        'name': name,
        'age': age
    }
    
    # Add student to the list
    students.append(student)
    print("Student added successfully.")

# Function to delete a student by ID
def delete_student():
    student_id = input("Enter student ID to delete: ")
    
    # Find and remove the student
    for i, student in enumerate(students):
        if student['id'] == student_id:
            del students[i]
            print("Student deleted successfully.")
            return
    
    print("Student ID not found.")

# Function to find a student by ID
def find_student():
    student_id = input("Enter student ID to find: ")
    
    # Search for the student
    for student in students:
        if student['id'] == student_id:
            print(f"Student found: ID = {student['id']}, Name = {student['name']}, Age = {student['age']}")
            return
    
    print("Student ID not found.")

# Function to display all students
def display_students():
    if not students:
        print("No students to display.")
        return
    
    print("List of students:")
    for student in students:
        print(f"ID = {student['id']}, Name = {student['name']}, Age = {student['age']}")

# Main menu function
def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Find Student")
        print("4. Display Students")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            find_student()
        elif choice == '4':
            display_students()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu function
    menu()

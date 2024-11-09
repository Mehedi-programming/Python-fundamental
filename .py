'''The issue in your code arises because you used info in the find and display_student functions without properly defining it in the code. This will cause a NameError since info is not recognized as a variable or dictionary in the current scope. Here’s the relevant part where the error occurs:

Explanation of the info Method Misuse

1. info Misuse in find Function: In your find function, you have:

print(f'ID:{Student_Id},Name:{info[student_name]},Age:{info[student_age]},CGPA:{info[student_CGPA]}')

Here, info is intended to represent the student data, but it is not defined anywhere in your code. You likely meant to reference the student data stored in Student[Student_Id].


2. info Misuse in display_student Function: Similarly, in the display_student function, you have:

print(f'ID:{Student_Id},Name:{info[student_name]},Age:{info[student_age]},CGPA:{info[student_CGPA]}')

Here, info is being iterated over using for Student_Id, info in Student.items(). This is correct because info is actually referring to each dictionary of student details (like {'student_name': ..., 'student_age': ..., 'student_CGPA': ...}), but you should still use proper string keys within square brackets to access these dictionary elements.



How to Correct the Code

To fix the code, you need to correct how you reference the dictionary keys for student_name, student_age, and student_CGPA. Here's an improved version:'''

def display_menu():
    print('\nWelcome to the Student Management System:')
    print('1. Add student')
    print('2. Display student')
    print('3. Delete student')
    print('4. Find student')
    print('5. Exit')

def add_student(Student):
    student_name = input('Enter your name: ')
    student_age = int(input('Enter your age: '))
    student_CGPA = float(input('Enter your result: '))
    Student_Id = len(Student) + 1  # Assuming Student_Id is sequentially generated
    Student[Student_Id] = {'student_name': student_name, 'student_age': student_age, 'student_CGPA': student_CGPA}

def delete_student(Student):
    Student_Id = int(input('Enter your student id: '))
    if Student_Id in Student:
        del Student[Student_Id]
        print('Student id has been deleted')
    else:
        print('Student id not found here')

def find(Student):
    Student_Id = int(input('Enter your student id: '))
    if Student_Id in Student:
        info = Student[Student_Id]
        print(f'ID: {Student_Id}, Name: {info["student_name"]}, Age: {info["student_age"]}, CGPA: {info["student_CGPA"]}')
    else:
        print('Student id not found here')

def display_student(Student):
    if Student:
        print('The student list is:')
        for Student_Id, info in Student.items():
            print(f'ID: {Student_Id}, Name: {info["student_name"]}, Age: {info["student_age"]}, CGPA: {info["student_CGPA"]}')
    else:
        print('There does not have any student')

def main():
    Student = {}
    while True:
        display_menu()
        Choice = input('Enter your choice (1 to 5): ')
        if Choice == '1':
            add_student(Student)
        elif Choice == '2':
            display_student(Student)
        elif Choice == '3':
            delete_student(Student)
        elif Choice == '4':
            find(Student)
        elif Choice == '5':
            print('Exit')
            break
        else:
            print('Please enter among 1 to 5.')
main()

'''Key Changes:

Corrected Dictionary Key Access: The correct way to access dictionary values by key is info["student_name"] instead of info[student_name].

Ensured Proper Scope for Variables: info is properly defined as Student[Student_Id] when needed.

Added Missing add_student Function: I also added the missing add_student function to match your menu choice'''
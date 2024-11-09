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
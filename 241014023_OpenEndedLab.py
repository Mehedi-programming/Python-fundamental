
def display_all_students():
    print()
    print('welcome to student management system:')
    print('1.Add student')
    print('2.Display for all student')
    print('3.Delete student')
    print('4.Find student')
    print('5.Exit')
def added(STUDENT):
    Student_Id=int(input('Enter your id:'))
    if Student_Id in STUDENT:
        print('This student already added.')
    else:
        student_name=input('Enter your name:')
        student_age=int(input('Enter your age:'))
        student_CGPA=float(input('Enter your result:'))
        STUDENT[Student_Id]={'student_name':student_name,'student_age':student_age,'student_CGPA':student_CGPA}
def delete(STUDENT):
    Student_Id=int(input('Enter your student id:'))
    if Student_Id in STUDENT:
        del STUDENT[Student_Id]
        print('Student id has been deleted')
    else:
        print('Student id not found here')
def find(STUDENT):
    Student_Id=int(input('Enter your student id:'))
    if Student_Id in STUDENT:
        info = STUDENT[Student_Id]
        print("ID:{'Student_Id'}","Name:{info['student_name']}","Age:{info['student_age']}","CGPA:{info['student_CGPA']}")
    else:
        print('Student id not found here')
def display_all_student(STUDENT):
    if STUDENT:
        print('The student list is')
        #i have used info kepping data
        for Student_Id,info in STUDENT.items():
            # i have use f for do not using single cottation
            print('ID:{'Student_Id'}','Name:{info['student_name']}','Age:{info['student_age']}',' CGPA:{info['student_CGPA']}')
    else:
        print('There does not have any student')

def my():
    #here STUDENT used as a empty dictionary
    STUDENT={}
    while True:
        display_all_students()
        selection=input('Enter your selection from (1 to 5):')
        if selection=='1': 
            added(STUDENT)
        elif selection=='2':
            display_all_student(STUDENT)
        elif selection=='3':
            delete(STUDENT)
        elif selection=='4':
            find(STUDENT)
        elif selection=='5':
            print('Exit')
            break
        else:
            print('Please enter among 1 to 5.')
# i have used main function for call function
my()

   





























class hasan:
    series='TV series'
obj1=hasan()
obj2=hasan()
obj1.name='mehedi'
obj1.age=22
obj2.name='mozumder'
obj2.age=21
print(obj1.name)
print(obj1.age)
print(obj1.series)
print()
print(obj2.name)
print(obj2.age)
print(obj2.series)

#
class student:
    name=''

    def activity(item):
        print("mozumder")
obj1=student() 
m_obj1=student()
h_obj1=student()
r_obj1=student()
k_obj1=student()
j_obj1=student()
f_obj1=student()


k_obj1.name='khabib'
j_obj1.name='jashim'
f_obj1.name='faisal'
print(m_obj1.name,h_obj1.name,r_obj1.name,k_obj1.name,j_obj1.name,f_obj1.name)
obj1.activity() 

#
class cartoon:
    "This a cartoon class"
    series='TV series'#class variable
    name=''
    age=''

    def __init__(self,name,age):
        self.name=name
        self.age=age 
        print(self.name)
        print(self.age)
    '''#instance method 
    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)
    #static method
    @staticmethod
    def emnetai():
        print('emnetei print korlam')'''
print(cartoon.__doc__)
obj1=cartoon('mehedi',22)
obj2=cartoon('hasan',21)
obj3=cartoon('mozumder',215)
#this is way to change parameter:
'''obj1.age=19
#print(obj1.__dict__)
obj1.show()
obj2.show()
obj3.show()
cartoon.emnetai()'''

  
class Doreamon:
    def doreamon_self(self):
        print('i am doreamon')
    def gadget(self):
        print('new gadget')
class Nobita(Doreamon):
    def nobita_self(self):
        print('i am nobita')
class Shizuka(Nobita):
    def shizuka_self(self):
        print("hasan")

doreamon=Doreamon()
nobita=Nobita()
shizuka=Shizuka

#nobita.doreamon_self()
shizuka.gadget()
 
class cartoon:
    series='tv series'
    name=''
    age=''
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)
ob1=cartoon('mehedi',20)
#print(ob1.__dict__)
ob2=cartoon('hasan',21)
print(ob1.__dict__)
ob3=cartoon('mozumdeder',22)
#object modefy
ob1.age=30
ob1.show()
ob2.show()
ob3.show()
print(ob1.__dict__)


class student:
    age=''
    name=''
ob1=student()
print(ob1.age)
def activity(self):
    print('my name is',self.name)
    print('my activity')
ob1=student()
print(ob1.name)
#ob1.activity() 
ob2=student()
ob3=student()
ob4=student()
ob1.name='mehedi'
ob2.name='hasan'
ob3.name='mozumder'
ob4.name='md'
#print(ob1.name)
#rint(ob2.name)
ob1.activity()

class department:
    CSE=''
    #BBA=''
    #EEE=''

def activity(self):
    return 'this is too much beter'
cse=department()
bba=department()
eee=department()
cse.CSE='good'
print(cse.CSE)   
print(cse.activity())


class father:
    def show_father(self):
        print('fathetr')
class Mother:
    def show_mom(self):
        print('Mom')
class child(father):
    def show_child(self):
        print('i am children')
show_father=father()
show_child=child()
child.gadget()

















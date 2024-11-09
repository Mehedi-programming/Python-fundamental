 def mehedi():
    print('mehedi hasan')
mehedi()
mehedi()
mehedi()
def sum(a,b):
    sum1=a+b
    return sum1
def sub(c,d):
    sub1=c-d
    return sub1
a1=20
a2=23
a3=30
a4=40
summation=sum(a1,a2)
subtriction=sub(a3,a4)
print(summation)
print(subtriction)

def mehedi():
    return 'Hasan'
name=mehedi()
print(name)
def mehedi():
    return 'mehedi hasan'
print(mehedi())
print(mehedi())
print(mehedi())
def hello():
    yield 1
    yield 1
    yield 1
print()
def sum():
    sum1=2+3
    return (sum1)
def sub():
    sub1=2-3
    return (sub1)
print(sum())
print(sub())
def bazar(item1,item2,d):
    print(item1,item2,d)
    #return item1+item2+d
a='apple'
b='mango'
c='orange'
bazar(a,b,c)

#print(bazar(a,b,' 2'))
def bazar(*halal):
    c=halal
    return c
a='mango'
b=' apple'
d=' orange'
print(bazar(a+d+b))
def bazar(**world):
    for i in world:
        return i
item1=' mango' 
item2='bannana'
item3=' orange'
z=bazar(item1,item2,item3)
print(z)
def hello(a,b,c):
    pass

x=(lambda a,b,c:a+b+c) 
print(x(2,3,4))
print(type(x))
def mehedi(*world):
    c=world
    return c
a='mango'
b='apple'
c='dfss'
name=mehedi(b,a,c)
print(name)
print(name)
print(type(name))
#list comprehension
number=[2,3,4,5,6]
num=[]
'''for i in number:
    num.append(i**2)
print(num)'''
num=[i**2 for i in number if i>2]
print(num)
a=[1,2,3,4,3]
b=str(a)
print(b)
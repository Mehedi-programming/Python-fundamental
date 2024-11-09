'''Number1=int(input("Enter a number:"))
Number2=int(input("Enter a number:"))
Sum=' Number1+Number2
print("The sum is:",Sum)
print(type(Sum))
print(len(Sum))'''

#string:
a='mehedi hasan'
print(a)
a="mehedi hasan'mozumder'"
print(a)
print(type(a))

b="""mehedi
hasan
mozumder"""
print(b)
b='''Mehedi
Hasan
Mozumder'''
print(b)
print(b[3])
print(b[2])
print(b[-5])
b='mozumder'
print(b[-8])
b='calculus'
print(b[3:])
print(b[2:4])
print(b[:3])
#in string we cannot change any index but there has a logic like:
s='multiline'
s=s[:3]+'d'+s[4:]
print(s)
a='bashundhara'
a=a[:5]+'a'+a[5:]
print(a)
a='bashundhara'
a=a[:5]+a[6:]            
print(a)   
a='shajek'
print(len(a))
a='Eid day '
b='Gala day '
c='first day '
print(a+b+c+'off day')
print(a*4)
A='apple'
if 'apple'==A:
    print('matched')
else:
    print('something wrong')
#follow asci code:
a='abc'
b='ABC'
print(a>b)
a='coding line'
b=457
c=85.956389
#print(a.title())
d=a+" {} {:.2f}".format(b,c)
print(d)
a='apple'
print('l'not in a)
#string method()
 
print(a.find('z'))
print(a.find('s'))
print(a.rfind('B'))
b='   a   dhamaka   '
print(b.center(61,"$"))
print(b.rjust(30,'#'))
print(b.ljust(10,"#"))    
print(b.count("a"))
print(b.strip())
s='565657 fan father dad 777 father'
print(s)
#print(s.strip())
#print(s.lstrip('567')) 
#print(s.rstrip('567'))
#b=s.split() 
#print(b[0])
print(s.split())
print(s.split('father')) 
print(s.split("father",1))
print(s.rsplit('father',1))
s='565657 Father 777 father'
print(s.splitlines())
print(s.splitlines(True))
print(s.splitlines(False))
s='565657 Father 777 father Goru'
print(s.partition('father'))
print(s.partition('777'))
print(s.partition('father'))
print(s.swapcase())
print(s.endswith('u'))
print(s.endswith('goru'))
print(s.startswith('565657'))
print(s.zfill(50))
print(s.replace('father','mom'))  
print(s.islower())
print(s.istitle())  
print(s.isupper())
s='5/7 bjhb'
print(s.isnumeric())
print(s.isdigit())
print(s.isdecimal())
print(s.isalpha())
a='apple eat' 
print('e'in a)
a='1 2 3 4 5 6 7'
print(a[::-1])
b=('1 2 3 4 5 6 7').split()
#print(b)
sum=0
for i in b:
    num=int(i)
    sum=sum+num
print(sum)
 














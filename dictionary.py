informtion={'name':('mehedi',1,2,3),'age':'22','height':'5.9','education':'HSC','current':'dhaka'}
print(informtion['name'])
for i in informtion.values():
    print(i)
for i,j in informtion.items():
    print(i,":",j)
b=informtion.setdefault('name')
print(informtion,b,sep='\n')
#change
informtion['height']='5.10'
#add
#informtion["home"]="cumilla" 
#delete
informtion.clear()
print(informtion)
#del informtion["education"]
informtion.popitem()
#copy
b=informtion.copy()
print(b)
informtion={'name':('mehedi',1,2,3),'age':'22','height':'5.9','education':'HSC','current':'dhaka'}
#for i in informtion:
    #print(informtion[i])
#for i in informtion.values():
   # print(i)
for i,j in informtion.items():
    print(i,":",j)
print(informtion.keys())
print(informtion.values())
print(informtion.items())
# this is one kind of add
b={'email':'mehedimozumder',
'age':'21'}
informtion.update(b)
print(informtion)
details=('name','age','location')
c=dict.fromkeys(details)
for i in c:
    if i=='name':
        c['name']='mehedi'
    elif i=='age':
        c['age']='22'
    elif i=='location':
        c['location']='cumilla'
print(c)
print(sorted(b))


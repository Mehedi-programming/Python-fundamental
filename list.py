sarc=["bangdesh","india","pakistan","Nepal","Butan"]
name='mehedi hasan mozumder'
print(name,end='.')
print("This is:", sarc)
numbers=[6,4,2,1,3,2,32,34,79]
#print(sarc+numbers)
numbers.reverse()
print(numbers)
print(numbers[3])
print(sarc[2])
print(len(numbers))
print(len(sarc))
print(type(sarc))
#constructor
b=list(("bangdesh","india","pakistan","Nepal","Butan"))
print(b)
sarc=["bangladesh","india",["malayshia","singapur"],"pakistan","Nepal","Butan"]
print(sarc*2)
print('hey'*3)
#sarc=["bangdesh","india","pakistan","Nepal","Butan"]
#sarc[1:4]=['irak','rassai','maldip']
#print(sarc)
print(sarc[2]*2)
print(sarc[2:5])
print(sarc)
print(sarc[2])
print(sarc[2][1])
print(sarc[1][2])
print(sarc[-2]) 
print(sarc[0:1])
#add
sarc.append('maldip')
print(sarc)
sarc.append('srilanka')
print(sarc)
sarc.extend(['Hello','World'])
print(sarc)
sarc.insert(1,3.5)
print(sarc)
sarc.insert(3,'brunai')
print(sarc)
sarc=["bangdesh","india","pakistan","Nepal","Butan"]
sarc[2]='Iran'
print(sarc)
sarc[2]='shlha'
print(sarc)
if 'bangladesh' in sarc:
    print('yes')
else:
    print('no')

A=['hasan','mozumder',['mehedi','kusum'],'md',67,897,67.9]
del A[2][1]
print(A)
del A[2]
print(A)
del A[1:4] 
print(A)
B=['hasan','mozumder','mehedi','md',67,897,67.9]
B.remove('mozumder')
print(B)
B.pop()
print(B)
B.pop(2)
print(B)

C=['hasan','mozumder',['mehedi','kusum','rahman'],'md',67,897,679]
for i in C:
    print(i)
else:
    print(i)
D=['hasan','mozumder',['mehedi','kusum','rahman'],'md',67,897,6.79]
for i in D:
    if type(i) is list:
        for j in i:
            print(j)
    else:
        print(i)

H=['hasan','mozumder',['mehedi','kusum','rahman'],'md',67,897,6.7,7,9]
print(len(H))
print(H)
D=H[2].copy()
print(D)
C=H.copy()
print(C)
print(H*2)
print(H[2]*2)
print(len(H))       
print(len(H[1]))
print(len(H[2]))
print('mozumder'in H)
H.clear()
print(H)
print(H+D)
Q=[1,3,2,4,8,6,5,6,]
print(Q[6])
print(Q.count(6))
Q.reverse()
print(Q)
Q.sort()
print(Q)
print(max(Q))
print(min(Q))
print(sum(Q))
A=('64747637822626465453782828272736464674444444477777777777777777777777777777777777777777222222222222222222266666666666644444444444444555555555333333338888888811111111116')
print(len(A))
x=[[1,2,3,4,5],[6,7,8,9,10]]
print(x[1][2])
#print(len(x))
#print(len(x[0]))
for row in range(len(x)):
    #print(x)
    for col in range(len(x[row])):
        print(row,col)
        print(x[row][col])
for row in x:
    for col in row:
        print(col)
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
sum_list=[]
sum1,sum2,sum3,sum4=0,0,0,0
for row in range(len(a)):
    for col in range(len(a[row])):
        sum=a[row][col]+b[row][col]
        sum_list.append(sum)
print(sum_list)
















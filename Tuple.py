name=("md", "mehedi", "hasan",("shajal","rafi"), "mozumder",2,4,5,1)
print(len(name))
name2=("Md", "Mehedi", "Masan","shajal","rafi", "mozumder")
print(sorted(name2))
print(max(name2))
num=(1,2,3,4,5)
print(num.count(2))
print(sum(num))
print(num.index(4))
print(name[3])
print(name[0:3])
d=str(name)
print(d)
b=list(name)
b.append('russel')
print(b)
c=tuple(b)
print(c)
print(name)
print(name[2])
print(type(name))
name=("mehedi")
print(type(name))
name1=("mehedi",)
print(type(name1))
nam=("md", "mehedi", "hasan",["shajal","haji"], "mozumder",2,4,5,1)
#nam[3][0]="kamrul","rafi"
#print(nam)
for i in nam:
    if type(i) is list:
        for j in i:
            print(j)
    '''elif type(i) is tuple:
        for j in i:
            print(j)
    else:
        print(i) '''

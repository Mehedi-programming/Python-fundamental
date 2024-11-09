a=' mehedi hasan mozumder'
print(a.join("##"))
print(a.endswith('ha'))
print(a.replace('hasan','mom'))
print(a.partition('mozumder'))
print(type(a))
print(len(a))
print(a[-2])
print(a[4:])
m=a[:6]+' mozumder '+a[7:]
print(m)
print(a + m + ' mashfee')
print('mehedi '*2)
c='goni '
f=234
d=34.2342
e=c+'{} {:.2f}'.format(f,d)
sarc=["bangdesh","india","pakistan","Nepal","Butan"]
sarc[1:2]=["dubai","saudi arab"]
print(sarc)
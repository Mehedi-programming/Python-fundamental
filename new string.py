name='''   md
mehedi
hasan
mozumder
rahaman 
asrafunnesa
hasan
'''
print(name)
print(name[3])
print(name[:9])
print(name[11:])
print(name[17:9])
add=name[:9]+' muntaha '+name[17:]
print(add)
print(len(name))
print('hasan'in name)
#string format
a='HASAN'
b='faiza'
c=6346
d=2322.54
e=a+b+'{} {}'.format(c,d)
print(e)
w='sava '
x='husne'
print(x+w+'hasan')
print(w*5)
print(name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())
print(name.casefold())
print(name.join('##'))
print('*'.join(name))
print(name.center(50,'&'))
print(name.ljust(60,'$'))
print(name.rjust(50,'@'))
print(name.split())
print(name.split('hasan'))
print(name.rsplit('hasan',0))
print(name.partition('mozumder'))
print(name.replace('mozumder','ferdous'))

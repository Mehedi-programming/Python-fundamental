print('answer to the question number 1:')
charecter=input("Enter your text:")
count=0 
vowel='aeiouAEIOU'
for i in charecter:
    if i in vowel:
        count=(count+1)
print(count)
print('question number 2nd:')
number=input("enter number:").split()
#sise_of_number=len(number)
#size_of_lenth_of_number=len(number)
for i in number:
    num=int(i)
    print(i)
    if (num%2==0):
        print('even')
    else:
        print('odd')
print('answer to question number 3:')
Temperature=input('enter temperature:').split()
for i in Temperature:
    tem=int(i)
    print(i)
    F=(tem*(9/5))+32
    print(F,'degree farenheight')
print('answer to the question number 4:')
integer=input('enter your number:').split()
for i in integer:
    Num=int(i)
    print(i)
    if(Num>0):
        print('positive')
    elif(Num<0):
        print('negetive')
    else:
        print('zero')
print('answer to question 5:')
topic='Hello World'
print(topic[-1:-12:-1])
print(topic[::-1])
print('answer to the question 6:')
number=input('enter number:').split()
#size_of_number=len(number)
for i in number:
    num=int(i)
    for j in range(2,num):
        if num%j==0:
            print('this is not a prime number')
            break        
    else:
        print('this a prime number')
print('answer to the question number 7:')
Number=int(input('enter a number:'))
sum=1
for i in range(2,Number+1):
    sum=sum*i
print(sum)
'''print('answer to the question number 8:')
Topic=input('enter your string:').split
for i in Topic:
    topic=int(i)
    j=topic+1
#size_of_lenth=(len(Topic))+1
#Lenth=int(size_of_lenth)+1
print(Topic[-1:-j:-1])
print('answer to the question number 9:')
Number=int(input('Enter a number:'))
count=1
for i in range(2,Number,1):
    count=count+1
    print(count)
'''
    




 











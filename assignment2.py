product_price=int(input("Please enter your product price:"))

now_your_product_price=(product_price)-(product_price*15)/100
Time=float(input('Please enter this time:'))
if (Time<15):
    print("You have got 15%  discount and now your current product price =",now_your_product_price)
elif(18<Time>21):
    print('You have got 15% discount and now your current product price=',now_your_product_price)
else:
    print('You have not got any discount')

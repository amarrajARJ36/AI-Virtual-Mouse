
from package.function import *

x , y = map(int,input('Input the numbers for calculation (First input,Second input: )').split(','))
a = input("Enter the type of calculation \n addition \n substraction \n multiplication \n division \n" )
 
if (a == 'addition'):
    sum(x,y)

elif (a == 'substraction'):
    diff(x,y)

elif (a == 'multiplication'):
    mult(x,y)

elif (a == 'division'):
    div(x,y)

else:
    print('Invalid input')
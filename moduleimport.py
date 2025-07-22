from random import *
from sys import *
secret_number = randint(1,20)
print('guess the secret number')
ans= int(input())
for I in range(5,0,-1):
    print('you have '+ str(I) + ' tries remaining')
    if ans > secret_number:
        print("secret number is below this number")
    elif ans < secret_number:
        print("the secret number is above this number")
    else:
        print('congratulations, you found the secret nunber')
        exit()
    ans=int(input())
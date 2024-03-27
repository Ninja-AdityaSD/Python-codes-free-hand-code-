#wap program to print twin prime number from 1 to n digit.
a=int(input("Enter the last number of range:"))

for i in range(1,a+1):
    if a%i==0:
        print(i)

        '''
        for j in i:
            i%j==0
            print(j)
            '''
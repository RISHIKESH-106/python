#1- PROGRAM TO PRINT THE HALF DIAMOND (USING THE FUCNTION):

def halfdiamondstar(N):
    for i in range(N):
        for j in range(0,i+1):
            print('*',end="")
        print()

    for i in range(1,N):
        for j in range(i,N):
            print("*",end="")

        print()

N=int(input("enter a number:"))
halfdiamondstar(N)

#2-PROGRAM TO PRINT THE HALF DIAMOND (WITHOUT USING THE FUNCTION):

n=int(input("enter the number:"))
# to print the ordered star
for i in range(0,n):
    print((n-i)*" "+i *"*")
    
# to print the inverted star
for i in range(n,0,-1): 
    print((n-i)* ' '+i *"*")
 
        


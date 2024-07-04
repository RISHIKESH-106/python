#FUNCTIONS:
#EXAMPLE:
def fun():
    print("HELLO WORLD!")

fun()

#FUNCTION WITH PARAMETERS:
def add(num1:int,num2:int):
    #adding two numbers
    num3=num1+num2

    return num3
a=int(input("enter a number:"))
b=int(input("enter a number:"))
ans=add(a,b)
print("the addition of the",a,"and",b,"is:",ans)   


#PYTHON FUNCTION ARGUMENTS:
def evenOdd(x):
    if(x%2==0):
        print('the number is even number')
    else:
        print("the number is odd number")
evenOdd(99)
evenOdd(40)

#TYPES OF ARGUMENTS;
#DEFAULT ARGUMENT
#KEYWORD ARGUMENT
#POSITIONAL ARGUMENT
#ARBITRARY ARGUMENT

#DEFAULT ARGUMENTS:

def myfun(x,y=80):
    print("a:",x)
    print("b:",y)

myfun(50)

#KEYWORD ARGUMENT:
def student(firstname,lastname):
    print(firstname,lastname)

student(firstname="Geeks",lastname="Practice") #Order doesn't matters in keyword arguments
student(lastname="Practice",firstname="Geeks")

#POSITIIONAL ARGUMENTS:

def nameAge(name,age):
    print("hello everyone,my name is",name)
    print("My age is",age)

print("Case-1:")
nameAge("Madan",31)

print("\nCase-2:")
nameAge(31,"Madan")


#ARBITARY KEYWORDS
#VARIABLE LENGTH NON-KEYWORDS ARGUMENTS:

def myfun(*argv):
    for arg in argv:
        print(arg)

myfun("HELLO!","WELCOME","TO","GEEKS",'FOR','GEEKS')

#VARIABLE LENGTH WITH KEYWORD ARGUMENTS:

def myfun1(**kwargs):
    for key,value in kwargs.items():
        print("%s ==%s" % (key,value))

myfun1(first=" Geeks",mid=" For",last=" Geeks")

def myFun(x):
    print(x)
    x = [20, 30, 40]
    print(x)
# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


def swap(x, y):
    temp = x
    x = y
    y = temp
    return x,y
# Driver code
x = 2
y = 3
a,b=swap(x, y)
print(x,a)
print(y,b)



def max_of_two(x1,y1,z1):
    if x1>y1 and x1>z1:
        return x1
    elif y1>z1 and y1>x1:
        return y1  
    else:
        return z1
    
max=max_of_two(4,8,54)
print(max)



# Define a function named 'sum' that takes a list of numbers as input
def sum(numbers):
    # Initialize a variable 'total' to store the sum of numbers, starting at 0
    total = 0
    
    # Iterate through each element 'x' in the 'numbers' list
    for x in numbers:
        # Add the current element 'x' to the 'total'
        total += x
    
    # Return the final sum stored in the 'total' variable
    return total

# Print the result of calling the 'sum' function with a tuple of numbers (8, 2, 3, 0, 7)
print(sum((8, 2, 3, 40, 7))) 

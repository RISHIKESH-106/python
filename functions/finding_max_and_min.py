#1-Find Maximum of two numbers in Python:

def max(a,b):
    if a>b:
        return a
    else:
        return b
a=int(input("enter a number:"))
b=int(input("enter a number:"))

print("the maximum number is:",max(a,b))

#2-Minimum of two numbers in Python:

def min(x,y):
    if x<y:
        return x
    else:
        return y
x=int(input("enter a digit:"))
y=int(input("enter a digit:"))

print("the minimum digit is:",min(x,y))

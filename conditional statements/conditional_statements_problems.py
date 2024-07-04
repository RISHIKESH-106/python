#CONDITIONAL STATEMENTS PROBLEMS:

#ELECTRICITY PROBLEM:
bill=0
a=int(input("enter a unit:"))
if(a<=100):
    bill=0
    print("no charge")
    
elif(200>a and a>100 ):
    bill2=a-100
    bill12=bill2*5
    print("the charge is Rs.",bill12)
    
elif(200<a):
    bill3=a-200
    bill31=(bill3*10)+500
    print("the charge is Rs.",bill31)

else:
      pass

# FINDING THE LAST DIGIT OF THE  NUMBER:
num=int(input("enter a number:"))
print("last digit of the number is:",num%10)
pass

# FINDING THE FIRST DIGIT OF THE NUMBER :
num1=int(input("enter a number:"))
s= str(num1)
first_digit= int(s[0])
second_digit=int(s[1])
last_digit= int(s[-1])

print("the first digit of the number",num1,"is:",first_digit)
print("the second digit of the number",num1,'is:',second_digit)
print("the last digit of the number", num1,"is:",last_digit)

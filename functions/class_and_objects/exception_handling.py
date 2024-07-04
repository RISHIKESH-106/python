# A python program to create user-defined exception
# class MyError is derived from super class Exception
class MyError(Exception):

	# Constructor or Initializer
	def __init__(self, value):
		self.value = value

	# __str__ is to print() the value
	def __str__(self):
		return(repr(self.value))


try:
	raise(MyError(3+345))

# Value of Exception is stored in error
except MyError as error:
	print('A New Exception occurred: ', error.value)
 

# NetworkError has base RuntimeError
# and not Exception
class Networkerror(RuntimeError):
	def __init__(self, arg):
		self.args = arg
try:
	raise Networkerror("TRAFLAGLAR")

except Networkerror as e:
	print(e.args)



#Catching Specific error:

def fun(a):
	if a<4:
		b=a/(a-3)
		print("the value of b is:",b)
try:
	fun(3)
	fun(5)
except ZeroDivisionError:
	print("ZeroDivisionError is ocurred and Handled")
except NameError:
	print("NameError has ocurred and Handled..")


#Try with Else Clause:

def Ab(a,b):
	try:
		c=((a+b)/(a-b))
	except ZeroDivisionError:
		print("a/b is 0")
	else:
		print(c)

Ab(2,3)
Ab(3,3)

# Finally:

try:
	k=5//0
except ZeroDivisionError:
	print("It Cannot be divided by 0")
finally:
	print("This is always executed...")

#Raising Exception:
try: 
	raise NameError("Hi there")
except NameError:
	print ("An exception")
	raise






















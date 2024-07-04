# Python program to illustrate destructor

class A:
	def __init__(self,bb):
		bb=3
		self.b = bb
		self.c=c()
		print(self.b)
	def __del__(self):
		print("apple")	
class B:
	def __init__(self,z=5):
		self.z=z
		self.a = A(self)
		print(self.z)
	def __del__(self):
		print("die")

class c:
	def __init__(self):
		print(self)
	def __del__(self):
		print("king")
		
def fun():
	b=B()

fun()

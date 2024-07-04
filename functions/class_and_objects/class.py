# __init__() function:

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1= person ("John",32)

print(p1.name)
print(p1.age)

#2- __str__() function:
# WITHOUT USING __str__():

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1= person ("John",32)

print(p1)

# WITH USING THE __str__() function:

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"({self.name}){self.age}"
p1=Person("John",36)

print(p1)

class geeks:
    def __init__(self,name,school):
        self.name=name
        self.school=school

    def __str__(self):
        return f"My name is {self.name} and I am studying in {self.school}"
p2=geeks("John","school")

print(p2)

#Class and Instance Variables:
#Defining instance variables using a constructor:
class Dog:
    animal='dog'

    def __init__(self,colour,breed):
        self.colour=colour
        self.breed=breed

roger=Dog("brown","pug")
zoro=Dog("black","pitbull")

print("the name of the dog is roger")
print("colour:",roger.colour)
print("breed:",roger.breed)
print("the name of this dog is zoro")
print(f"colour:{zoro.colour}\nbreed:{zoro.breed}")







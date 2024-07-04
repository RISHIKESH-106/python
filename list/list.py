""" LIST MANIPULATION"""

""" APPEND"""
print("append")
x=[1,2,3,4,5,6,7,8,9,10,11]
x.append([12,13,14,15,161])
print(x)

"""EXTEND"""
print("extend")
y=[1,2,3,45,27,332]
z=("name","age","class")
y.extend(z)
print(y)

"""COPY"""
"""SHALLOW COPY"""

print("shallow copy")
import copy
b=["apple","vegetables","cars"]
c=copy.copy(b)
print(c)

""" DEEP COPY"""

print("deepcopy")
import copy
d=["BUGGATI","FERRARI","LAMBO"]
e=copy.copy(d)
print("D id:",id(d) ,"Value:",d)
print("E id:",id(e),"Value:",e)


"""CLEAR"""

print("clear")
a1=[22,33,44,55]
a1.clear()
print(a1)


"""COUNT"""

print("count")
a2=[11,22,34334,1232]
print(a2.count(11))

"""INDEX"""

print("index")
a3=["a","b","c"]
print(a3.index("c"))

""" INSERT"""

print("insert")
a4=["a","b","c","d","e","f","g","h"]
a4.insert(5,"z")
print(a4)


"""POP"""
print("pop")
a5=["a","b","c","d","e","f","g"]
a5.pop()
print(a5)

"""REMOVE"""
print("remove")
a6=["a","b","c"]
a6.remove("b")
print(a6)


"""REVERSE"""

print("reverse")
a7=[1,2,3,43,5,6,7,8,9]
a7.reverse()
print(a7)

"""SORT"""

print("sort")
a8=[2,35,62,46,87653,376873]
a8.sort()
print(a8)


"""MIN"""

print("min")
a9=[3,2,6,36]
print(min(a9))

"""MAX"""

print("max")
a10=[23,62,4356,235]
print(max(a10))


"""DELETE"""

print("Delete")
a11=[1,2,3,4,5,6,7,8,9,]
del a11[0]
print(a11)


"""len"""
print("len")
a12=[1,2,3,4,5,6,7,8,9,10]
print(len(a12))

"""SUM"""

print("sum")
a13=[1,2,3,4,45]
print(sum(a13))


"""MAX"""
print("Max")
a14=["john","car","apple"]
print(max(a14))


"""MIN"""
print("Min")
a14=["john","car","apple"]
print(min(a14))





























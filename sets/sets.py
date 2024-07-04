"""SET """

#INTERSECTION
print("intersection")
s1 = {1, 2, 3,4,60}
s2 = {2,3}
print(s1.intersection(s2))

#ADD
print("add")
s1.add(4)
print(s1)

#CLEAR
print("clear")
s2.clear()
print(s2)

#COPY
print("copy")
s3=s1.copy()
print(s3)

#DISCARD
print("discard")
s3.discard(4)
print(s3)

#DIFFERENCE UPDATE
print("difference update")
s1 = {1, 2, 3,4,60}
s4={10,20,30,40,50,60}
s4.difference_update(s1)
print(s4)

#DIFFERENCE
print("difference")
print(s1.difference(s4))
print(s4.difference(s1))

#ISSUPERSET
print("issuperset")
print(s1.issuperset(s4))
print(s4.issuperset(s1))

#ISSUBSET
print("issubset")
print(s1.issubset(s4))
print(s4.issubset(s1))

#UNION
print("union")
print(s1.union(s4))

#FROZENSET
print("frozenset")
a=frozenset({"giraffe","lion","cat"})
print("dog" in a)
print("lion" in a)




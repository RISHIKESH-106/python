#FOR LOOP

#FOR LOOP WITH STRINGS

s="aizen sosuke"
for i in s:
    print(i)

#FOR LOOP WITH RANGE
for a in range(2,30,3):
    print(a)

#FOR LOOP WITH ENUMERATE
l1=["apple","orange","watermelon"]

for index,x in enumerate(l1):
    print(index , x)

#FOR LOOP WITH NESTED
for b in range(1,4):
    for c in range(1,4):
        print(b,c) 

#FOR LOOP WITH OVER LIST
L=["geeks","for","geeks"]
for d in L:
    print(d)

#FOR LOOP IN ONE LINE
NUMBER=[e for e in range(59,29,-1)]
print(NUMBER)


#FOR LOOP WITH DICTIONARY
print("dicitionary iteration")

a1=dict()
a1['xyz']=1234
a1['abcd']=987

for f in a1:
    print(f,a1[f])

#FOR LOOP WITH TUPLE

t=((1,2,0),(3,4,5),(6,7,8))
for z,y,x in t:
    print(x,z,y)

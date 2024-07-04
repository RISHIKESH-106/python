# DICTIONARY MANIPULATION

#CLEAR
import copy
dict = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
print(dict)


#COPY
dict1=copy.deepcopy(dict) 
print(dict1)

#FROMKEYS
dict2 = {'A','Geeks', 'B','For', 'C','Geeks'}
dict22=[1,2,3,4,5,6,7,8,9]
print(dict.fromkeys(dict2,dict22))

#GET
dict = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
print(dict.get('A'))

# #ITEMS
print(dict.items())

# #KEYS
print(dict.keys())

# #VALUES
print(dict.values())

# #POP
dict11=dict.pop("A")
print(dict11)

# #POPITEM
dict111=dict.popitem()
print(dict111)

#SETDEFAULT
dict.setdefault(' ',543)
print(dict)

#UPDATE

dict4={'B':"cars"}
dict.update(dict4)
dict['B']= 'from'
print(dict)





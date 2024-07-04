#1-Python program to interchange first and last elements in a list:

def swaplist(newlist):
    size=len(newlist)
    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp
    return newlist
newlist=[12,35,9,56,4]
print(swaplist(newlist))

#2-Python Program to Swap Two Elements in a List:

def swap(list,position1,position2):
    temp=list[position1]
    list[position1]=list[position2]
    list[position2]=temp
    return list
list=[23,65,19,90]
position1,position2=1,3
print(swap(list,position1-1,position2-1))

def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[23,65,19,90]
pos1,pos2=1,3
print(swap(list,pos1-1,pos2-1))
swap(list,pos1,pos2)

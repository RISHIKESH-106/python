# super() function in Python :

class emp:
    def __init__(self,id,name,add):
        self.id=id
        self.name=name
        self.add=add

class freelancer(emp):
    def __init__(self,id,name,add,emails):
        super().__init__(id,name,add) #using super function
        self.emails=emails      
emp1=freelancer(106,"Sanji","chennai","Sanji@gmails")

print("the Id is:",emp1.id)
print("the name is:",emp1.name)
print("the address is:",emp1.add)
print("the email Id is:",emp1.emails)



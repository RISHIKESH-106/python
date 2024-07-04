# Overloading binary + operator in Python: 

class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,o):
        return self.a+ o.a
    
ob1=A(1)
ob2=A(3)
ob3=A("Edward")
ob4=A(" Newgate")

print(ob1+ob2)
print(ob3+ob4)
print(A.__add__(ob1,ob2))
print(A.__add__(ob3,ob4))
print(ob1.__add__(ob2))
print(ob3.__add__ (ob4))

# Python Program to perform addition of two complex numbers using binary :

class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self,other):
        return self.a+other.a,self.b+other.b
    
ob1=Complex(1,2) #self.a,self.b
ob2=Complex(4,3) #other.a,other.b
ob3=ob1+ob2 #self.a+other.a,self.b+other.b
print(ob3)

#Overloading comparison operators in Python : 
class B:
    def __init__(self,c):
        self.c=c
    def __gt__(self,other):
        if(self.c>other.c):
            return True
        else:
            return False
obj1=B(3)
obj2=B(7)
if (obj1>obj2):
    print("obj1 is greater than obj2")
else:
    print("obj2 is greater than obj1")


 # Python program to overload equality and less than operators:

class C:
    def __init__(self,a1):
        self.a1=a1

    def __lt__(self,other):
        if(self.a1<other.a1):
            return"ob1 is lesser than ob2"
        else:
            return "ob2 is lesser than ob1"
        
    def __eq__(self,other):
        if (self.a1 == other.a1):
            return "Both are equal"
        else:
            return "Both are not equal"
        
ob1=C(1)
ob2=C(19)

print(ob1<ob2)

ob3=C(4)
ob4=C(8)

print(ob1 ==ob2)




class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")


def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_ind = India()
obj_usa = USA()


for country in (obj_ind, obj_usa):
    func(country)

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter your move (row[1-3] column[1-3]): ").split())
        if board[row-1][col-1] == ' ':
            board[row-1][col-1] = current_player
            
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That cell is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()

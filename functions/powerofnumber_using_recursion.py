def powerofnum(number,power):

    if power==0:
        return 1
    else:
        return (number*pow(number,power-1))
    

number=int(input("enter a number:"))
power=int(input("enter a power of the number:"))

print(powerofnum(number,power))


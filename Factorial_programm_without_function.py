n = input("enter a number: ")
fact =1
try:
    n = int(n)
    if n < 0:
        print("Error! :  This is negative integer. Please enter non negative interger")
        
    elif n == 0:
        print (1)
    else:
        
        for i in range(1,n+1):
            fact = fact *i
        print("the factorial of given number is " , fact)
except ValueError:
    print("Error!: Invalid input.This is a float. Please enter a non-negative integer.")

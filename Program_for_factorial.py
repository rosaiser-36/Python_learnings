n = int(input("enter a number to knw the factorial: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print ("the factorial of",n, "is" ,factorial (n))  

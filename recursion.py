#defining the function
def factorial_recursive(n):
    #if the value is 1 or 0 the result will be 1
    if n == 0 or n==1:
        return 1
    #otherwise the result will be(n*(n-1))
    return n * factorial_recursive(n-1)
#for taking user input
f = int(input("enter the number you want the factorial:"))
#calling the function
r= factorial_recursive(f)
print(r)
#program to solve Euclid's Algorithm using recursion

def gcd(m,n):
    #check if either m or n is negative
    if m < 0 or n < 0:
        raise ValueError("\nError: Arguments passed must be positive integers only")
    elif n == 0: #if n is zero then m is the GCD
        return m
    else:
        remainder = m % n
        #call the function again then change n to m position and our remainder in n position
        return gcd(n, remainder)

#Lets test what we have done
print("\n*******EUCLID'S ALGORITHM SOLUTION USING RECURSION IN PYTHON*****\n")
# get the inputs from the user & calculate GCD
try:
    m = int(input('Enter the First Positive Integer: '))
    n = int(input('Enter the Second Positive Integer: '))
    
    #display the GCD of the two numbers    
    print(f'\nThe GCD of {m} and {n} is: {gcd(m,n)}')
except ValueError as e:
    print(e)

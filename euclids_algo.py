#program to solve Euclid's Algorithm

def gcd (m , n):
    #check if either m or n is negative
    if m < 0 or n < 0:
        raise ValueError("\nError: Input values must be positive integers only")
    else:
        #loop through until n is equals 0
        while n != 0:
            # store the remainder of the division of m by n
            remainder = m % n
            #update m to hold the value of n
            m = n
            #set n to hold value of the remainder of the division of m by n
            n = remainder
        
        # m contains the gcd, since n is 0 when the loop is executed    
        return m 

#Lets test what we have done
print("\n*******EUCLID'S ALGORITHM SOLUTION WITH WHILE LOOP IN PYTHON*****\n")
# get the inputs from the user & calculate GCD
try:
    m = int(input('Enter the First Positive Integer: '))
    n = int(input('Enter the Second Positive Integer: '))

    #display the GCD of the two numbers 
    print(f'\nThe GCD of {m} and {n} is: {gcd(m,n)}')
except ValueError as e:
    print(e)

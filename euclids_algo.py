#program to solve Euclid's Algorithm

def gcd (m , n):
    #check if either m or n is negative
    if m < 0 or n < 0:
        raise ValueError("\nError: Arguments passed must be positive integers only")
    else:
        #loop through until n is equals 0
        while n != 0:
            #store the initial value of n in a temp variable
            temp = n
            # store the remainder of the division of m by n
            remainder = m % n
            #update m to hold the previous value of n, temp
            m = temp
            #set n to hold value of the remainder of the division of m by n
            n = remainder
            
        return m #m contains the gcd, since n is now 0 after loop is completed


print("*******EUCLID'S ALGORITHM SOLUTION USING WHILE LOOP IN PYTHON*****\n")

try:
    m = int(input('Enter the First Positive Integer: '))
    n = int(input('Enter the Second Positive Integer: '))

    print(f'the gcd of {m} and {n} is: {gcd(m,n)}')
except ValueError as e:
    print(e)

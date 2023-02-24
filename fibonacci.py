# Python program to print the fibonacci series

# Pre-defining 1st and 2nd terms
term1 = 0
term2 = 1
count = 0

#Enter the terms to be printed
num = int(input("Enter the number of terms: "))

# Check for condition
if(num<=0):
    print("Fibonacci series for negative terms is not possible!")
    
elif(num == 1):
    print(term1)
    
# Print Fibonacci series
else:
    while count < num:
        print(term1)
        new_term = term1 + term2
        term1=term2
        term2=new_term
        count= count + 1
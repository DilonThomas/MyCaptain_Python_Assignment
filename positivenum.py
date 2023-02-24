# Python program to print all the positive numbers in a list

num = []
x = 0
n = int(input("Enter the number of values to be entered: "))
print("Enter the numbers: ")

# Creating the list to be sorted
for i in range(n):
    num.append(int(input()))
    
# Printing the finalised list
print("The final list is: ", num)
print("The positive terms are: ")

# Condition to sort out postive numbers only
while(x < len(num)):
    if (num[x]>=0):
        print(num[x])
    x+=1
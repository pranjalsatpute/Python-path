# for second step I am going to code a basic triangle pattern with numbers



n=int(input("Enter how many rows you want to print: ")) #takes user input which specifies the number of rows to be printed
print()
for i in range(1,n+1): # this loop decides the number of the rows
  for j in range(1,i+1): # this loop decides what number will be printed in the rows
    print(j,end=" ") # print's the numbers with space between them
  print()
 
# output:
# Enter how many rows you want to print: 10

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8 9 10 



# This code prints the required numbers in a triangular manner 
n=int(input("Enter how many numbers you want to print: ")) # takes total numbers to be printed as user input 
print()
num=1 #initialize num as 1
i=1 #initialize i as 1
while num<=n: # while num is less or equal to n while loop will keep on executing
  for j in range(1,i+1): #this loop decides which numbers are to be displayed
    if num>n: #if num is greater than n then the loop breaks 
      break
    print(num,end=" ")
    num+=1 #increment num 
  print()
  i+=1 #increment i

# output:

# Enter how many numbers you want to print: 10

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10
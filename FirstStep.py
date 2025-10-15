# Let us take n number of plates and in those n plates we need to place n number of cookies
# there are two conditions while placing the cookies:
#         1. nobody will mind if they get the same cookie twice or trice or their whole plate has the same cookie 
#         2. Everyone wants different cookie

# number of combinations which cookies can be placed in a plate for the 1st condition is: n^n 
#    as in 1 plate any n cookies can be kept: 1 plate -> n cookie
#                                             2 plates -> n cookie
#                                             n plates -> n^n cookies
def Repeated(n):
    return n**n

# number of combinations where cookies can be placed in a plate for the 2nd condition:
#    in a plate we can place any one of the n cookie, now we have n-1 variety of cookie which can be placed 
#    and according to this logic we can place all the different cookies till we have on other variety
#    i.e n, n-1, n-2....1
#    n x (n-1) x (n-2) x 1 = n!, this is known as n!
def notRepeated(n):
  arrangement=1
  for i in range(1,n+1):
    arrangement=arrangement*i
  return arrangement
  # we can also solve this by importing math library by [import math]and using [math.factorial(n)] command

numberOfLetters=int(input("How many Letters are to be arranged?: "))
print("Number of combinations where letters can be repeated are {0}".format(Repeated(numberOfLetters)))
print("Number of combinations where letters cannot be repeated are {0}".format(notRepeated(numberOfLetters)))

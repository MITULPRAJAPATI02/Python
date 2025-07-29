# n=5
# for i in range(n):
#     for j in range(n):
#         print("*" , end=" ")
#     print("")        
# output
# * * * * * 
# * * * * * 
# * * * * *
# * * * * *
# * * * * *


# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print(" ")
# output
# *  
# * *  
# * * *
# * * * *
# * * * * *


# n=int(input("Enter the number of rows"))
# for i in range (n):
#     print((str(i+1)+ ' ')*n)
        

# output:
# 1 1 1 
# 2 2 2 
# 3 3 3 

# n=int(input("Enter the number of rows"))

# for i in range(n):
#     for j in range (n-i):
#         print("*", end=" ")
#     print( )    
# output
#  * * * * * 
# * * * *
# * * *
# * *
# *

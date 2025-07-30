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


for i in range (1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print( )    
    
    
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print( )   

# output

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 


for i  in range   (1,6):
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()  

# output
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 
# 6 5 4 3 2 1 
for i in range (5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()   
        
# output
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1


# # Butterfly Effect
# rows = int(input("Enter the number of rows: "))


# for i in range(1, rows + 1):
#     print("*" * i, end="")
#     print(" " * (2 * (rows - i)), end="")
#     print("*" * i)


# for i in range(rows, 0, -1):
#     print("*" * i, end="")
#     print(" " * (2 * (rows - i)), end="")
#     print("*" * i)

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# **********
# ****  ****
# ***    ***
# **      **
# *        *


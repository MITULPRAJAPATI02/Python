n=int(input("Enter the number"))
digit = 0
b=n
while b>0:
    b=int(b/10)
    digit=digit +1

print("digit>>>",digit)
b=n
ans=0
while b>0:
    # print("digit----->>>", digit)
    rem=b%10
    ans=ans+(rem ** digit)
    b=int(b/10)
# else :
#     print("number is not a armstrong")


if ans==n:
    print(n,"is Armstrong Number")
else:
    print(n,"is not Armstrong Number")

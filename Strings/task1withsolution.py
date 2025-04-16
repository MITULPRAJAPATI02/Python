s="this is string example"

1)reverse the string

2) word wise reverse

3) 2 characters interchange

4)	space split
	join the string with *


5) replace is -> was
		substring->this this
					is  was



...............................................................
s="this is string example"
print(s[::-1])



s="this is string example"
old="is"
new="was"
m=s.replace(old,new)
print(s)
print(m)

s="this is string example"
print( s[-19:-23:-1] , s[-16:-18:-1] , s[-9:-15:-1] , s[-1:-8:-1])

s="this is string example"
a=s.replace (" is "," was ")
print(a)


s="this is string example"
c=s.split(" ")
print("split the string:",c)

a="*"
seq="c"
d=s.join(c)
print("join the string:",d)



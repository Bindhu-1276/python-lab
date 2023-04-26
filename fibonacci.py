n=int(input("enter the integer"))
f0,f1=0,1
f2=f0+f1
print(f0,f1,end=" ")
while n>2:
	print(f2,end=" ")
	f0=f1
	f1=f2
	f2=f0+f1
	n-=1




#output:enter the integer5
0 1 1 2 3

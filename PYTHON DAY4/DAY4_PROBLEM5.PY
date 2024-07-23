a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c,d=a,b
while b!=0:
    a,b=b,a%b
print((c*d)//a)

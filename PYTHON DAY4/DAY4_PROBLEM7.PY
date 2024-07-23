#WRITE A PROGRAM TO PRINT ALL THE PRIME NUMBERS IN AGIVEN RANGE
a=int(input("enter a number1"))
b=int(input("enter a number2"))      
for i in range(a,b+1):
    for j in range (2,i):
       if i%j==0:
          break
    else:
        print(i)

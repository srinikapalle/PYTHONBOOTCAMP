#FIND EVEN OR ODD
n=int(input())
if(1&n==0):
    print("even")
else:
    print("odd")
#FIND GREATEST OF THREE
my_list=list(map(int,input().split()))
greatest=0
for i in range(len(my_list)):
    if(my_list[i]>greatest):
        greatest=my_list[i]#modify the element
print(greatest)
#*FIND PEAK ELEMENT IN THE ARRAY
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
     if my_list[i]>my_list[i+1] and my_list[i]>my_list[i-1]:
        count=1
        break
print(my_list[count])
#FIND MAXIMUM ELEMENT IN THE ARRAY
my_list=list(map(int,input().split()))
max=0
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
print(max)        
#find the sum of squares of given number
n=234
sum=0
while n>0:
    r=n%10
    sum=sum+r**2
    n=n//10
print(sum)
#find sum of squares of even and odd digits
#check wheather the given number is palidrome or not using while loop
#write a program to print first n fabinoci series
#FIND SECOND MAX ELEMENT IN THE ARRAY
#REVERSE AN ARRAY WITHOUT USING BUILDING FUNCTIONS
#FIND SUM OF ELEMENTS IN THE ARRAY

#FIND THE SUM OF SQUARE OF A DIGIT IN A GIVEN NUMBER
#n=int(input())
#sum=0
#while n>0:
  #  r=n%10
  #  sum=sum+r**2
   # n=n//10
#print(sum)
#sum of even in a given number
n=1234
sum=0
while n>0:
    r=n%10
    if(r%2==0):
        sum+=r
    n=n//10
print(sum)
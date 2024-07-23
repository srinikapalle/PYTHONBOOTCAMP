#leap year
#divisible by400 not divisible by 100
#n=int(input())
#if(n%400==0):
 #  print("leap year")
#else:
#   print("not a leap year")
#LEAP YEAR FOR A GIVEN RANGE
n=int(input())
k=int(input())
for i in range(n,k):
 if(i%400==0 and i%100!=0):
      print(i)
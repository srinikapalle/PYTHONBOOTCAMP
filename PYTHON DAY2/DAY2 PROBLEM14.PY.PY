 #your given with a comma seperated natural numbers 1 to 10 .print only the even
#my_list=list(map(int,input().split()))
#for i in range(1,10):
   #if(i%2==0):
       # print(i):
my_list=list(map(int,input().split()))
for i in range(1,len(my_list),2):
    print(my_list[i])


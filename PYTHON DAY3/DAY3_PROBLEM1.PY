#FIND THE  ELEMENTS THAT IS PRESENT IN K+N INDEX 
#K=3
#N=2
#3 6 8 4 61 2
#OP:2
#K=3
#N=4
#80 70 54 36 72
#OP:ERROR
#USING CONDITIONAL STATEMENTS
my_list=list(map(int,input().split()))
N=int(input())
B=len(my_list)
if(B<K+N):
   print("error")
#else:
 #   print(my_list[K+N])
for i in range(len(my_list)):
    print(my_list[K+N],end=" ")
    break
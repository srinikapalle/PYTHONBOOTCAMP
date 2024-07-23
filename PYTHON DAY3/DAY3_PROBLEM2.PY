#PRINT THE ELEMENT IN A PARTICULAR INDEX
my_list=list(map(int,input().split()))
K=int(input())
B=K%len(my_list)                                                 #K=8,len(my_list)=7 remainder=1 idx=1
print(my_list[B])                                                 #70 65 67 89 54 32 63 op:65

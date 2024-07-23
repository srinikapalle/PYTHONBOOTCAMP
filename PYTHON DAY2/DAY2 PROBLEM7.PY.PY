# GIVEN A SPACE SEPERATED INTEGER LIST FIND THE AVERAGE OF ELEMENTS PRESENT IN EVEN INDEX
my_list=list(map(int,input().split(" ")))
#sum=0
#n=0
#for i in range(0,len(my
#avg=0_list),2):
  # sum+=my_list[i]
  # n+=1
#avg=sum/n
#print(avg)
sum=0
count=0
n=len(my_list)
for i in range(len(my_list)):
    sum+=my_list[i]
    count+=1

print(sum/count)

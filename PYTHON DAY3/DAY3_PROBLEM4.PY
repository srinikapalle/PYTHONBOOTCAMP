#FIND THE MINIMUM ELEMENT IN THE GIVEN LIST
my_list=list(map(int,input().split()))
per=0
for i in range(len(my_list)):
    if(my_list[i]<per):
        per=my_list[i]#modify the element
print(per)


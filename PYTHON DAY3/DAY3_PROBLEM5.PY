#REPLACE THE ELEMENTS IN THE ARRAY WITH AVERAGE OF MAXIMUM AND MINIMUM ELEMENTS
my_list=list(map(int,input().split()))
max=0
min=0
for i in range(len(my_list)):
 if(my_list[i]>max):
        max=my_list[i]#modify the element
for i in range(len(my_list)):
 if(my_list[i]<min):
        min=my_list[i]
avg=(max+min)/2
for i in range(len(my_list)):
       my_list[i]=avg
print(avg)       

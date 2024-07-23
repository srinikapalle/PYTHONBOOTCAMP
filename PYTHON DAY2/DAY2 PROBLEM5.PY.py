my_list=list(map(int,input().split(",")))
choice=int(input())
if(choice==1):
    my_list.append(9999)
    print(my_list)
elif(choice==2):
    my_list.pop(2)
    print(my_list)
elif(choice==3):
    my_list.sort()
    print(my_list)
elif(choice==4):
    print(len(my_list))
else:
    print("gd morning divya sri")


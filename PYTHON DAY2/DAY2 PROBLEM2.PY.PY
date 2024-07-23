#my_listlist(map(int,input().split("@")))
my_list=list(map(str,input().split(" ")))
my_list.append(9999)
print(*my_list)
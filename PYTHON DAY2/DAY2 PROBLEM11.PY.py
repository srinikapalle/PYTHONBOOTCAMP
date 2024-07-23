# your given with a space seperated interger list find the number of even elements and number of odd elements in the given list
my_list=list(map(int,input().split(" ")))
even_count=0
odd_count=0
for i in range(0,len(my_list)):
    if(my_list[i]%2==0):
      even_count+=1
    else:
      odd_count+=1
print(f"(even={even_count})")
print(f"(odd={odd_count})")

      
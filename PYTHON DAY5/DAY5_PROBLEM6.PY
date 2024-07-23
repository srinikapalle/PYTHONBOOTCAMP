#PRINT THE NON REPEATING CHARATER IN A GIVEN STRING
i=input()
inp=i.lower()
check=['a','e','i','o','u']
consonent="bcdfghjklmnpqrstvwxyz"
ans=" "
for i in inp:
    if( i not in ans):
      ans+=i
print(ans)
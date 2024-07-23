#INPUT=HELLO 123
#OUTPUT=6
i=input()
inp=i.lower()
check=['a','e','i','o','u']
consonent="bcdfghjklmnpqrstvwxyz"
numbers="0123456789"
ans=0
for i in inp:
    if( i in numbers):
      ans+=int(i)
print(ans)
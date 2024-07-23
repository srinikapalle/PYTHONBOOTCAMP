#INPUT:HELLO-----WOR----LD
#OUTPUT:-----HELLO WORLD
inp=input()
inp1=''
for i in inp:
    if(ord(i)==45):
         pass
    else:
         inp1+=i
print('-'*10+inp1)
#method2
inp=input()
count=0
ans=''
for i in inp:
    if(i=='-'):
         count+=1
    else:
         ans=ans+i
print('-'*count+ans)

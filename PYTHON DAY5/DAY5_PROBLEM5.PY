#PRINT ALL VOWELS FOLLOWED BY CONSONENTS
check=['a','e','i','o','u']
consonent="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i=input()#"hello world"
inp=i.lower()
for i in inp:
    if( i in check):
        print(i,end=" ")
for i in inp:        
    if(i in consonent):
        print(i,end=" ")      

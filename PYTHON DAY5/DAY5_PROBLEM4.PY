#VOWELS
string=input("enter a string")
vowels=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
print("number of vowels are:")
print(vowels)
#METHOD2:
check=['a','e','i','o','u']
count=0
inp="hello world"
for i in inp:
    if( i in check):
        count+=1
print(count)       
#CONSONENTS
check=['a','e','i','o','u']
consonent="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="hello world"
inp=i.lower()
for i in inp:
    if( i in check):
        count+=1
for i in inp:
    if(i in consonent): 
        c+=1      
print(count)
print(c)
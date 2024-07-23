#INPUT:ABC,SKIP4
# O/P:EFG
inp=input()
char=''
end=0
for i in inp:
    n=ord(i)
    char+=chr(n+4)
print(char)    